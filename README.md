# Faucetearner: Async XRP Claimer Tool

![Faucetearner Banner](https://github.com/user-attachments/assets/22af88b8-7b2c-41ec-bccb-b9ad2f7bcccb)

> An efficient and professional command-line tool for automatically claiming XRP tokens from Faucetearner.org.

This project is a complete refactor of the original Faucetearner script, rebuilt from the ground up with modern industry standards. It leverages asynchronous programming for high efficiency, object-oriented principles for clean and maintainable code, and professional logging for clear, structured output.

## ✨ Features

- **Professional & Clean Code**: Refactored into a well-structured, object-oriented architecture that is easy to read, maintain, and extend.
- **Asynchronous Core**: Built with `asyncio` and `aiohttp` for non-blocking operations, ensuring minimal resource consumption while waiting.
- **Standard CLI Interface**: Uses Python's `argparse` for straightforward command-line argument handling.
- **Reliable & Robust**: Includes proper error handling and session management to ensure stable, long-running operation.
- **Minimal Dependencies**: Only requires `aiohttp`, keeping the setup lightweight and simple.

## 🚀 Getting Started

Follow these steps to get the Faucetearner CLI up and running on your system.

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)

### Installation & Usage

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/RozhakDev/Faucetearner.git
   cd Faucetearner
   ```

2. **Install the required dependencies:**
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   Execute the script from the root directory using the following command. You must provide your Faucetearner account cookie as an argument.
   
   ```bash
   python -m src.main "your_cookie_string_here"
   ```
   
   **Example:**
   
   ```bash
   python -m src.main "reg=1; login=1; user=932154187127"
   ```

4. **Stopping the script:**
   Press `CTRL+C` at any time to gracefully stop the application.

## ⚠️ Disclaimer

This tool is designed to automate the process of claiming tokens on Faucetearner.org. It is intended for educational purposes and personal use only. The developers are not responsible for any actions taken on your account. Please use this tool responsibly and in accordance with the website's terms of service.

## 🤝 Contributing

Contributions are welcome! Whether it's bug fixes, feature enhancements, or documentation improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## ⚖️ License

See [LICENSE](LICENSE) file for more information about the software license.