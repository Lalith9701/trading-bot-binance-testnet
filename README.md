# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based command-line trading bot designed to place orders on the **Binance Futures Testnet (USDT-M)**.

The application allows users to place **MARKET** and **LIMIT** orders via a CLI interface, while maintaining a clean and modular code structure with proper input validation, logging, and error handling.

This project was developed as part of a **Python Developer Internship Application Task**.

---

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Support for **BUY and SELL** sides
- Command Line Interface (CLI) for user input
- Input validation for order parameters
- Structured and modular project architecture
- Logging of API requests, responses, and errors
- Exception handling for API and network failures

---

## Tech Stack

- Python 3.x
- python-binance library
- argparse (CLI interface)
- logging module
- Binance Futures Testnet API

---

## Project Structure
~~~
trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging configuration
│ └── cli.py # CLI entry point
│
├── logs/
│ └── trading.log
│
├── requirements.txt
└── README.md
~~~
---

## Setup Instructions

### 1. Clone the Repository

```bash
1. git clone https://github.com/yourusername/trading-bot-binance-testnet.git
cd trading-bot-binance-testnet

2. Install Dependencies
pip install -r requirements.txt

3. Create Environment File
Create a .env file in the project root.
---
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

These keys can be generated from:

https://testnet.binancefuture.com
Running the Trading Bot
Market Order Example
python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Example Output:

Order Request
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response
Order ID: 123456
Status: FILLED
Executed Quantity: 0.001
Average Price: 62000
Limit Order Example
python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
Logging

All API requests, responses, and errors are logged in:

logs/trading.log
---
Example log entry:

2026-03-06 INFO Order Response: {orderId: 123456, status: FILLED}
Error Handling

The application handles multiple error scenarios including:

Invalid CLI input

Invalid order parameters

Binance API errors

Network failures

Errors are printed in the CLI and also recorded in the log file.
---
Example Commands

Market Order:

python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
---
Limit Order:

python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
Assumptions

Binance Futures Testnet account is active

API credentials are valid

Sufficient test balance is available

Orders are placed on USDT-M Futures Testnet

Future Improvements

Possible enhancements include:

Stop-Limit orders

Advanced CLI interface

Position monitoring

Risk management module

Web UI for order management
