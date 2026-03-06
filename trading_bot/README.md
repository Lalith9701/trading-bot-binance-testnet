# Binance Futures Testnet Trading Bot

## Setup

1. Clone repository or unzip folder
2. Install requirements

pip install -r requirements.txt

3. Create .env file

BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret

## Run

Market order:

python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:

python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

Logs are stored in logs/trading.log
