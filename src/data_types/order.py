from data_types.configs.vm_config import VMConfig

class Order:
    def __init__(self, vm_config: VMConfig, quantity: int):
        self.vm_config = vm_config
        self.quantity = quantity
    
    @classmethod
    def from_dict(cls, data):
        vm_config = VMConfig.from_dict(data["vm_config"])
        return cls(vm_config, data["quantity"])