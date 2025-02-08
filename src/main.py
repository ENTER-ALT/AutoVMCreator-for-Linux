from data_types.configs.medium_attachment_config import DriveType
from data_types.configs.storagecontroller_config import StorageControllerConfig
from data_types.configs.vm_config import VMConfig
from creator import Creator
from data_types.configs.medium_config import HDDMediumConfig, MediumConfig
from user_interface import UserInterface

def main():
    order_file = UserInterface.start()
    orders_json = load_orders(order_file)
    UserInterface.show_orders(orders_json)
    
    order = Order.from_json(order_file)

    vm1 = VMConfig()
    Creator.create_vm(vm1)
    Creator.modify_vm(vm1)
    hdd_medium = HDDMediumConfig(vm1.folder + "/" + vm1.name + "_" + vm1.disk_name)
    Creator.create_hdd_medium(hdd_medium)

    storage_controller1 = StorageControllerConfig()
    Creator.create_storage_controller(vm1, storage_controller1)

    medium_attachment_hdd = Creator.create_attachment_config(storage_controller1, hdd_medium, DriveType.HDD, 1)
    Creator.attach_medium_to_controller(vm1, storage_controller1, hdd_medium, medium_attachment_hdd)

    iso_medium = MediumConfig(vm1.iso_file)
    medium_attachment_iso = Creator.create_attachment_config(storage_controller1, iso_medium, DriveType.DVD_DRIVE, 2)
    Creator.attach_medium_to_controller(vm1, storage_controller1, iso_medium, medium_attachment_iso)
    UserInterface.end()

def load_orders(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)

    orders = [Order.from_dict(order) for order in data["orders"]]
    return orders

if __name__ == "__main__":
    main()
