from user_interface import UserInterface
from vm_manager import VMManager
from data_types.configs.vm_config import VMConfig
from file_validator import FileValidator

class OrderExecutor:
    def __init__(self, orders):
        self.orders = orders

    def execute_all(self):
        UserInterface.display_message("Executing orders...")
        UserInterface.show_orders(self.orders)

        for idx, order in enumerate(self.orders): 
            UserInterface.display_message(f"Executing order {idx}")
            self.execute_order(order, idx)

    def execute_order(self, order, idx):
        stage = 1
        vm1: VMConfig = order.vm_config
        vm_manager: VMManager = VMManager(vm1)

        pipeline = [
            (self.throw_error_if_exists, [vm1.name]),
            (vm_manager.create_image),
            (vm_manager.install_OS),
            (vm_manager.create_linked_images, [order.quantity]),
            (vm_manager.run_VM),
        ]

        for func, args in pipeline:
            try:
                self.before_stage(stage, func)
                func(*args)  
                self.after_stage(stage, func)
                stage += 1  
            except Exception as e:
                UserInterface.display_error_message(f"Error at stage {stage} in order {idx}: {e}")
                if stage > 2:
                    self.delete_vm_if_exists(vm_manager)
                break   
            
    def before_stage(self, stage, func):
        UserInterface.display_message(f"Starting Stage {stage}: {func.__name__}")

    def after_stage(self, stage, func):
        UserInterface.display_message(f"Completed Stage {stage}: {func.__name__}")

    @staticmethod
    def throw_error_if_exists(name: str):
        if FileValidator.validate_file_exists(name):
            raise ValueError(f"Image with name {name} already exists")

    @staticmethod
    def delete_vm_if_exists(vm_manager: VMManager):
        if vm_manager.vm_exists:
            vm_manager.delete_vm()
            UserInterface.display_message(f"Deleted {vm_manager.vm_config.name} VM")
