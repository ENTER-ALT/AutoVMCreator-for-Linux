import json
import sys
from data_types.order import Order
from user_interface import UserInterface

def load_orders(json_path) -> list[Order]:
    with open(json_path, "r") as file:
        data = json.load(file)

    orders = [Order.from_dict(order) for order in data["orders"]]
    return orders

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python load_orders.py <path_to_json>")
        sys.exit(1)

    json_path = sys.argv[1]
    orders = load_orders(json_path)

    UserInterface.show_orders(orders)

    
