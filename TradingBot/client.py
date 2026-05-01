from binance.client import Client

def get_binance_client(api_key, api_secret_key):
    return Client(api_key, api_secret_key, testnet=True)