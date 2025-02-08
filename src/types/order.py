from types.configs.vm_config import VMConfig

class Order:
    def __init__(self, vm_config: VMConfig, quantity: int):
        self.vm_config = vm_config
        self.quantity = quantity