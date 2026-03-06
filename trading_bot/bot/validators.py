def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()

def validate_quantity(qty):
    qty = float(qty)
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    return qty
def validate_order_type(order_type):
    allowed = ["MARKET", "LIMIT", "STOP_LIMIT"]
    
    if order_type.upper() not in allowed:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")
    
    return order_type.upper()