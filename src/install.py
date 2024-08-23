from configs.medium_attachment_config import DriveType
from configs.storagecontroller_config import StorageControllerConfig
from configs.vm_config import VMConfig
from creator import Creator
from configs.medium_config import HDDMediumConfig, MediumConfig
from user_interface import UserInterface

def main():

    iso_file = UserInterface.start()
    vm1 = VMConfig()
    Creator.create_vm(vm1)
    Creator.modify_vm(vm1)
    hdd_medium = HDDMediumConfig(vm1.folder + "disk2.vmdk")
    Creator.create_hdd_medium(hdd_medium)

    storage_controller1 = StorageControllerConfig()
    Creator.create_storage_controller(vm1, storage_controller1)

    medium_attachment_hdd = Creator.create_attachment_config(storage_controller1, hdd_medium, DriveType.HDD, 1)
    Creator.attach_medium_to_controller(vm1, storage_controller1, hdd_medium, medium_attachment_hdd)

    iso_medium = MediumConfig(iso_file)
    medium_attachment_iso = Creator.create_attachment_config(storage_controller1, iso_medium, DriveType.DVD_DRIVE, 2)
    Creator.attach_medium_to_controller(vm1, storage_controller1, iso_medium, medium_attachment_iso)
    UserInterface.end()

if __name__ == "__main__":
    main()
