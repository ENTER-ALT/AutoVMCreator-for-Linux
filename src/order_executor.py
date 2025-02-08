from user_interface import UserInterface
from vm_manager import VMManager
from data_types.configs.medium_attachment_config import MediumAttachmentConfig, DriveType
from data_types.configs.medium_config import HDDMediumConfig, MediumConfig
from data_types.configs.storage_controller_config import StorageControllerConfig

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
        for i in range(order.quantity):    
            stage = 1
            vm1 = order.vm_config.copy(i)

            pipeline = [
                (self.throw_error_if_exists, [vm1.name]),
                (VMManager.create_vm, [vm1]),
                (VMManager.init_vm, [vm1]),
                (self.create_hdd_and_attach, [vm1]),
                (self.attach_iso, [vm1])
            ]

            for func, args in pipeline:
                try:
                    self.before_stage(stage, func)
                    func(*args)  
                    self.after_stage(stage, func)
                    stage += 1  
                except Exception as e:
                    UserInterface.display_message(f"Error at stage {stage} in order {idx}: {e}")
                    if stage > 2:
                        self.delete_vm_if_exists(vm1.name)
                    break  

    def before_stage(self, stage, func):
        UserInterface.display_message(f"Starting Stage {stage}: {func.__name__}")

    def after_stage(self, stage, func):
        UserInterface.display_message(f"Completed Stage {stage}: {func.__name__}")
        
    def create_hdd_and_attach(self, vm1):
        hdd_medium = self.create_hdd_medium(vm1)
        storage_controller1 = self.create_storage_controller(vm1)
        self.attach_hdd_to_controller(vm1, storage_controller1, hdd_medium)

    def create_hdd_medium(self, vm1):
        hdd_filename = vm1.folder + "/" + vm1.name + "_" + vm1.disk_name
        hdd_medium = HDDMediumConfig(hdd_filename)
        VMManager.create_hdd_medium(hdd_medium)
        return hdd_medium

    def create_storage_controller(self, vm1):
        storage_controller1 = StorageControllerConfig()
        VMManager.create_storage_controller(vm1, storage_controller1)
        return storage_controller1

    def attach_hdd_to_controller(self, vm1, storage_controller1, hdd_medium):
        medium_attachment_hdd = MediumAttachmentConfig.create_attachment_config(
            storage_controller1, hdd_medium, DriveType.HDD, 1
        )
        VMManager.attach_medium_to_controller(vm1, storage_controller1, hdd_medium, medium_attachment_hdd)

    def attach_iso(self, vm1):
        storage_controller1 = StorageControllerConfig()  # Recreate or store in vm1
        iso_medium = MediumConfig(vm1.iso_file)
        medium_attachment_iso = MediumAttachmentConfig.create_attachment_config(
            storage_controller1, iso_medium, DriveType.DVD_DRIVE, 2
        )
        VMManager.attach_medium_to_controller(vm1, storage_controller1, iso_medium, medium_attachment_iso)

    @staticmethod
    def throw_error_if_exists(vm_name: str):
        if VMManager.vm_exists(vm_name):
            raise ValueError(f"VM with name {vm_name} already exists")

    @staticmethod
    def delete_vm_if_exists(vm_name: str):
        if VMManager.vm_exists(vm_name):
            VMManager.delete_vm(vm_name)
            UserInterface.display_message(f"VM {vm_name} already exists. Deleting it...")
