from binance.client import Client

API_KEY = "ekJtpPlbcM05tjhEbF2MA2iNQD3LZk0XoQLR7RP9Mc06vYeA67V9GCEiCbh3ins7"
SECRET_API_KEY = "Djb79JzsVYEFM3LniC8990UQj5mkoGxAaVlMnh60V560DeEinra0DyK3oR1ak0vt"

client = Client(API_KEY,SECRET_API_KEY, testnet=True)

try:
    account_info = client.futures_account()
    print(f"Connection Successfull!")
    print(f"Demo Balance: {account_info['totalWalletBalance']} USDT")
except Exception as e:
    print(f"Exception Occurred while making Connection & fetching Balance to Demo Account: {e}")