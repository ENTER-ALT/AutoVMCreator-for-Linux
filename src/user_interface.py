import sys

from string_extractor import StringExtractor
from file_validator import FileValidator
from data_types.order import Order


class UserInterface:
    @staticmethod
    def start():
        if len(sys.argv) <= 1:
            raise ValueError("You should give the path to the order file as an argument, e.g. python main.py order.json")
        
        order_file = sys.argv[1]
        
        if not order_file.endswith('.json'):
            raise ValueError("The order file must be a JSON file with a .json extension")
        
        file_exists = FileValidator.validate_file_exists(order_file)
        if not file_exists:
            raise ValueError(f"File '{order_file}' does not exist.")

        return order_file

    @staticmethod
    def show_orders(orders: list[Order]):
        print("Orders:")
        for idx, order in enumerate(orders, start=1):
            print(f"{idx}. Order: {order.quantity} x {order.vm_config.name} ({order.vm_config.ram_gb} GB RAM) with {order.vm_config.image_size_gb} GB disk, iso: {order.vm_config.iso_file_name}")

    @staticmethod
    def display_message(message: str):
        print(message)

    @staticmethod
    def display_error_message(message: str):
        print(f"Error: {message}")

    @staticmethod
    def end():
        UserInterface.display_message("VM Creation Completed Successfully 󰄛")

