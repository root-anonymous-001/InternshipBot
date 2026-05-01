import argparse
from TradingBot.client import get_binance_client
from TradingBot.orders import place_order

# API KEYS
API_KEY = "ekJtpPlbcM05tjhEbF2MA2iNQD3LZk0XoQLR7RP9Mc06vYeA67V9GCEiCbh3ins7"
SECRET_API_KEY = "Djb79JzsVYEFM3LniC8990UQj5mkoGxAaVlMnh60V560DeEinra0DyK3oR1ak0vt"

def main():
    parser = argparse.ArgumentParser(description="CLI Controlled Binance Futures Trading Bot !")
    parser.add_argument("--symbol", type=str, required=True, help="Trading Pair, e.g., BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=['BUY', 'SELL'], help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, choices=['MARKET', 'LIMIT'], help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Trading Amount")
    parser.add_argument("--price", type=float, required=False, help="Price for --type = LIMIT orders!")
    
    args = parser.parse_args()
    # calling the function from client.py
    client = get_binance_client(API_KEY, SECRET_API_KEY)

    try:
        print(f"Executing {args.type} order!")
        # calling the function from orders.py
        res = place_order(client, args.symbol, args.side, args.type, args.quantity, args.price)
        print(f"Trade Completed! >>> 🚀!")
        print(f"Order id: {res['orderId']}  |  Order Status: {res['status']}")
        print("Check TradingBot.log for log details!")
    except Exception as e:
        print("Order Failed!")
        print(f"Exception Occurred while placing the Order: {e}")
        print("Kindly Check TradingBot.log for much details!")



# Calling out the main Function
if __name__ == '__main__':
    main()