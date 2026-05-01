import logging

logging.basicConfig(
    filename='TradingBot.log',
    level=logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s'
)

def place_order(client, symbol, side, order_type, quantity, price=None):
    
    try:
        order_params = {
            'symbol' : symbol,
            'side' : side,
            'type': order_type,
            'quantity' : quantity,
        }
        
        if order_type == 'LIMIT':
            if not price:
                logging.info("LIMIT order ke liye --price mandatory hai!")
                raise ValueError("Order Type is LIMIT, so --price is required!")
            
            # price check: Sirf BTCUSDT ke liye check karega
            minimum_price = 1000
            if symbol == 'BTCUSDT' and price < minimum_price:
                logging.info(f"Price cannot be less than {minimum_price}, because {symbol} actual price is around 60000+")
                raise ValueError(f"Price {price} is too low BTC Orders! Order rejected.")
            order_params['price'] = price
            order_params['timeInForce'] = 'GTC'
                
                
            
        print("Initializing Order Placing...!")
        logging.info(f"Order placing Initialized Successfully:  {order_params}")
        response = client.futures_create_order(**order_params)
        
        logging.info(f"Order Successfully placed: {response['orderId']}")
        return response
        
        
    except Exception as e:
        print("Order Failed!")
        print(f"Exception Occurred while placing the Order")
        raise e