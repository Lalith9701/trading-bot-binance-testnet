from bot.client import client
from bot.logging_config import logger

def place_order(symbol, side, order_type, quantity, price=None):

    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise
def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):

    try:

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        logger.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise    