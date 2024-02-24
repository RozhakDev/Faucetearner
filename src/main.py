import argparse
import asyncio
import logging
import time
from .client import FaucetEarnerClient
from .logger_setup import setup_logging

async def main_loop(cookie: str):
    """
    The main loop that periodically claims XRP.

    Args:
        cookie (str): The user's authentication cookie.
    """
    logging.info("Starting Faucetearner Client...")
    logging.info("Press CTRL+C to stop the program.")

    async with FaucetEarnerClient(cookie=cookie) as client:
        while True:
            try:
                start_time = time.time()

                status_message = await client.claim_xrp()
                logging.info(status_message)

                wait_time = 60
                logging.info(f"Will attempt the next claim in {wait_time} seconds.")
                
                for i in range(wait_time, 0, -1):
                    print(f"   Waiting... {i} seconds remaining   ", end='\r')
                    await asyncio.sleep(1)
                print("                                       ", end='\r')
            except asyncio.CancelledError:
                logging.info("Program stopped by user.")
                break
            except Exception as e:
                logging.error(f"An unexpected error occurred in the main loop: {e}")
                logging.info("Retrying in 60 seconds...")
                await asyncio.sleep(60)

def run():
    """
    Function to run the application from the command line.
    """
    parser = argparse.ArgumentParser(
        description="Asynchronous bot to claim XRP tokens from Faucetearner.",
        epilog="Ensure the provided cookie is valid and enclosed in quotes."
    )
    parser.add_argument(
        "cookie",
        type=str,
        help="Authentication cookie from your Faucetearner account."
    )
    args = parser.parse_args()

    setup_logging()

    try:
        asyncio.run(main_loop(args.cookie))
    except KeyboardInterrupt:
        logging.info("\nProcess stopped manually. Goodbye!")

if __name__ == '__main__':
    run()