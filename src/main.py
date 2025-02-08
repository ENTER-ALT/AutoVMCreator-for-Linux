from user_interface import UserInterface
from data_types.order import Order
from order_executor import OrderExecutor
from object_loader import load_orders

def main():
    order_file = UserInterface.start()
    orders = load_orders(order_file)
    order_executor = OrderExecutor(orders)
    order_executor.execute_all()
    UserInterface.end()

if __name__ == "__main__":
    main()
