from data_types.configs.vm_config import VMConfig

class Order:
    def __init__(self, vm_config: VMConfig, quantity: int):
        self.vm_config = vm_config
        self.quantity = quantity

    @staticmethod
    def from_json(json: dict):
        vm_config = VMConfig.from_json(json["vm_config"])
        quantity = json["quantity"]
        return Order(vm_config, quantity)
    
    @classmethod
    def from_dict(cls, data):
        vm_config = VMConfig.from_dict(data["vm_config"])
        return cls(vm_config, data["quantity"])