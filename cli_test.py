import argparse
from binance.client import Client

parser = argparse.ArgumentParser(description="CLI Controlled Binance Futures Trading Bot !")
parser.add_argument("--symbol", type=str, required=True, help="Trading Pair, e.g., BTCUSDT")
parser.add_argument("--side", type="str", required=True, choices=['Buy', 'Sell'], help="Buy or Sell")
parser.add_argument("--type", type="str", required=True, choices=['MARKET', 'LIMIT'], help="MARKET or LIMIT")
parser.add_argument("--quantity", type=float, required=True, help="Trading Amount")
parser.add_argument("--price", type=float, required=False, help="Price for LIMIT orders")

args = parser.parse_args()

API_KEY = "ekJtpPlbcM05tjhEbF2MA2iNQD3LZk0XoQLR7RP9Mc06vYeA67V9GCEiCbh3ins7"
SECRET_API_KEY = "Djb79JzsVYEFM3LniC8990UQj5mkoGxAaVlMnh60V560DeEinra0DyK3oR1ak0vt"

client = Client(API_KEY, SECRET_API_KEY, testnet=True)

# try:
#     print(f"Executing: {args.type} order for {args.}")