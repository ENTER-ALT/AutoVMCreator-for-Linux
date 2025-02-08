from data_types.configs.vm_config import VMConfig
from data_types.configs.storage_controller_config import StorageControllerConfig
from data_types.configs.medium_attachment_config import MediumAttachmentConfig, DriveType
from data_types.configs.medium_config import MediumConfig, HDDMediumConfig
from shell_executor import ShellExecutor
from string_extractor import StringExtractor
from command_shortcuts import *


class VMManager:
    
    @staticmethod
    def vm_exists(vm_name: str):
        command_message = [
            VBOXMANAGE_COMMAND,
            LIST_COMMAND,
            VM_OPTION
        ]

        output = ShellExecutor.execute_command(command_message)
        return StringExtractor.vm_exists(vm_name, output)
    
    @staticmethod  
    def delete_vm(vm_name: str):
        command_message = [
            VBOXMANAGE_COMMAND,
            UNREGISTERVM_COMMAND,
            vm_name,
            DELETE_OPTION
        ]

        ShellExecutor.execute_command(command_message)
    
    @staticmethod
    def create_vm(vm_config: VMConfig):
        command_message = [
            VBOXMANAGE_COMMAND,
            CREATEVM_COMMAND,
            NAME_OPTION, vm_config.name,
            OSTYPE_OPTION, vm_config.os_type,
            REGISTER_OPTION
        ]

        output = ShellExecutor.execute_command(command_message)
        vm_config.folder = StringExtractor.extract_folder_path_from_create_vm_output(output)

    @staticmethod
    def init_vm(vm_config: VMConfig):
        command_message = [
            VBOXMANAGE_COMMAND,
            MODIFYVM_COMMAND,
            vm_config.name,
            DESCRIPTION_OPTION, vm_config.description,
            MEMORY_OPTION, vm_config.ram,
            VRAM_OPTION, vm_config.vram,
            CPUS_OPTION, vm_config.cpus,
            NIC1_OPTION, vm_config.nic1,
            AUTOSTART_ENABLED_OPTION, vm_config.autostart_enabled,
            DRAG_AND_DROP_OPTION, vm_config.drag_and_drop,
            BRIDGE_ADAPTER1_OPTION, vm_config.bridge_adapter
        ]

        ShellExecutor.execute_command(command_message)

    @staticmethod
    def create_storage_controller(vm_config: VMConfig, storage_controller_config: StorageControllerConfig):
        command_message = [
            VBOXMANAGE_COMMAND,
            STORAGECTL_COMMAND,
            vm_config.name,
            NAME_OPTION, storage_controller_config.name,
            ADD_OPTION, storage_controller_config.add,
            CONTROLLER_OPTION, storage_controller_config.controller
        ]

        ShellExecutor.execute_command(command_message)

    @staticmethod
    def create_hdd_medium(medium_config: HDDMediumConfig):
        command_message = [
            VBOXMANAGE_COMMAND,
            CREATEMEDIUM_COMMAND,
            medium_config.medium_type,
            FILENAME_OPTION, medium_config.filename,
            SIZE_OPTION, medium_config.size,
            FORMAT_OPTION, medium_config.format,
            VARIANT_OPTION, medium_config.variant
        ]

        ShellExecutor.execute_command(command_message)

    @staticmethod
    def attach_medium_to_controller(
            vm_config: VMConfig,
            storage_controller_config: StorageControllerConfig,
            medium_config: MediumConfig,
            medium_attachment_config: MediumAttachmentConfig):
        command_message = [
            VBOXMANAGE_COMMAND,
            STORAGEATTACH_COMMAND,
            vm_config.name,
            STORAGECTL_OPTION, storage_controller_config.name,
            PORT_OPTION, medium_attachment_config.port,
            TYPE_OPTION, medium_attachment_config.drive_type,
            MEDIUM_OPTION, medium_config.filename
        ]

        ShellExecutor.execute_command(command_message)