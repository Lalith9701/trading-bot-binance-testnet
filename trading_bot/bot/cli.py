import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import logger

def main():

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = args.price

        print("\nOrder Request")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if order_type == "LIMIT" and not price:
            raise ValueError("LIMIT order requires --price")

        order = place_order(symbol, side, order_type, quantity, price, args.stop_price)

        print("\nOrder Response")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Quantity:", order.get("executedQty"))
        print("Average Price:", order.get("avgPrice"))

        print("\nOrder placed successfully!")

    except Exception as e:
        logger.error(str(e))
        print("Error:", str(e))

if __name__ == "__main__":
    main()
parser.add_argument("--stop_price", required=False)