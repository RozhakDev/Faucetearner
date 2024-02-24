import logging
import aiohttp
import re
from .config import HTTP_HEADERS, FAUCET_URL, API_URL

class FaucetEarnerClient:
    """
    An asynchronous client to interact with Faucetearner.

    Manages the HTTP session, cookies, and the logic for claiming XRP tokens.
    """

    def __init__(self, cookie: str):
        """
        Initializes the client with the user's cookie.

        Args:
            cookie (str): The authentication cookie from the Faucetearner account.
        """
        if not cookie:
            raise ValueError("Cookie cannot be empty.")
        
        self._headers = HTTP_HEADERS.copy()
        self._headers['Cookie'] = cookie

        self._session = None
        self.total_claimed = 0
        self.total_failed = 0

    async def __aenter__(self):
        """
        Creates an aiohttp session when entering the context manager.
        This is the best practice for managing the session lifecycle.
        """
        self._session = aiohttp.ClientSession(headers=self._headers)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the aiohttp session when exiting the context manager.
        """
        if self._session:
            await self._session.close()
    
    async def claim_xrp(self) -> str:
        """
        Executes the process of claiming an XRP token.

        This process involves two steps:
        1. Visiting the faucet page, possibly to initialize a server-side session.
        2. Sending a POST request to the API to claim the reward.

        Returns:
            str: A status message from the claim result.
        """
        if not self._session:
            raise RuntimeError("Client session is not initialized. Use 'async with'.")
        
        try:
            async with self._session.get(FAUCET_URL) as response:
                response.raise_for_status()
                logging.info("Successfully accessed faucet page, proceeding to claim...")

            post_headers = self._session.headers.copy()
            post_headers.update({
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/json',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Origin': 'https://faucetearner.org',
            })

            async with self._session.post(API_URL, headers=post_headers, data={}) as response:
                response.raise_for_status()

                try:
                    response_data = await response.json()
                    message = response_data.get('message', '')
                except aiohttp.ContentTypeError:
                    message = await response.text()
                    response_data = message
                
                if 'congratulations' in message.lower():
                    try:
                        match = re.search(r'>([\d.]+) XRP</span>', message)
                        if not match:
                            raise ValueError("XRP amount pattern not found in the message.")
                        
                        amount_str = match.group(1)
                        amount = float(amount_str)
                        self.total_claimed += 1
                        return f"Claim successful! You received {amount:.6f} XRP. Total Success: {self.total_claimed}, Failed: {self.total_failed}"
                    except (IndexError, ValueError, AttributeError) as e:
                        logging.warning(f"Failed to parse XRP amount from message: '{message}'. Error: {e}")
                        self.total_claimed += 1
                        return f"Claim successful! (XRP amount could not be parsed). Total Success: {self.total_claimed}, Failed: {self.total_failed}"
                elif 'you have already' in message.lower():
                    self.total_failed += 1
                    return f"Failed: You have already claimed. Waiting for the next cycle. Total Success: {self.total_claimed}, Failed: {self.total_failed}"
                else:
                    self.total_failed += 1
                    return f"Unknown error: {response_data}. The cookie might be invalid."
        except aiohttp.ClientError as e:
            logging.error(f"A network error occurred: {e}")
            self.total_failed += 1
            return f"Failed: Network error. Total Success: {self.total_claimed}, Failed: {self.total_failed}"