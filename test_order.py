from binance.client import Client

API_KEY = "ekJtpPlbcM05tjhEbF2MA2iNQD3LZk0XoQLR7RP9Mc06vYeA67V9GCEiCbh3ins7"
SECRET_API_KEY = "Djb79JzsVYEFM3LniC8990UQj5mkoGxAaVlMnh60V560DeEinra0DyK3oR1ak0vt"

client = Client(API_KEY,SECRET_API_KEY, testnet=True)

try:
    print("Placing Market Orders... >>>")
    response = client.futures_create_order(
        symbol = "BTCUSDT",
        side = "BUY",
        type = "MARKET",
        quantity = 0.001
    )
    
    print("Trade Completed!")
    # print(response)
    print(f"Order ID: {response['orderId']}")
    print(f"Status: {response['status']}")
    print(f"Executed Quantity: {response['executedQty']}")
    print(f"Ordered Quantity: {response['origQty']}")
    
except Exception as e:
    print(f"Order Failed due to an Exception: {e}")