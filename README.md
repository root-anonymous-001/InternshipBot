# Binance Futures Trading Bot

A simple CLI application to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M). 

## Project Structure
```text
InternshipBot/
├── bot/
│   ├── __init__.py
│   ├── client.py        # Handles Binance testnet connection
│   └── orders.py        # Order placement and validation logic
├── cli.py               # Main CLI entry point
├── requirements.txt     # Project dependencies
└── TradingBot.log       # Auto-generated log file


#Setup Instructions

1. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

2. Install dependencies: 
pip install -r requirements.txt

3. Configure API Keys:
Open cli.py and replace API_KEY and SECRET_API_KEY variables with your actual Binance Testnet credentials, I have used my own Test Keys


#How to Run
The bot uses standard terminal arguments to execute trades.

1:- Place a Market Order:
python cli.py --symbol BTCUSDT --type MARKET --side BUY --quantity 0.001

2:- Place a Limit Order:
python cli.py --symbol BTCUSDT --type LIMIT --side SELL --quantity 0.001 --price 65000


#Assumptions & Notes

-The client strictly connects to the Binance Testnet (testnet=True).

-For LIMIT orders, the --price argument is mandatory. The timeInForce parameter is automatically set to GTC (Good Till Canceled) as per Binance requirements.

-Validation Handled: Added a basic edge-case validation for BTCUSDT. It blocks limit orders with extremely low bounds (e.g., < 1000) to prevent accidental faulty trades, while keeping other symbols (like low-priced altcoins) unaffected.