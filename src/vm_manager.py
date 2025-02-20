from data_types.configs.vm_config import VMConfig
from shell_executor import ShellExecutor
from string_extractor import StringExtractor
from file_validator import FileValidator
from command_shortcuts import *


class VMManager:
    
    def __init__(self, vm_config: VMConfig):
        self.vm_config: VMConfig = vm_config
        self.linked_images = []

    def vm_exists(self):
        return FileValidator.validate_file_exists(self.vm_config.image_file_name)
    
    def delete_vm(self):
        command_message = [
            VBOXMANAGE_COMMAND,
            UNREGISTERVM_COMMAND,
            self.vm_config.name,
            DELETE_OPTION
        ]

        ShellExecutor.execute_command(command_message)
    
    def create_vm(self):
        command_message = [
            VBOXMANAGE_COMMAND,
            CREATEVM_COMMAND,
            NAME_OPTION, self.vm_config.name,
            OSTYPE_OPTION, self.vm_config.os_type,
            REGISTER_OPTION
        ]

        output = ShellExecutor.execute_command(command_message)
        self.vm_config.folder = StringExtractor.extract_folder_path_from_create_vm_output(output)

    def init_vm(self):
        command_message = [
        ]

        ShellExecutor.execute_command(command_message)

    def create_image(self):
        # Implementation for creating an image
        pass

    def install_OS(self):
        # Implementation for installing the OS
        pass

    def create_linked_images(self, quantity):
        # Implementation for creating linked images
        pass

    def run_VM(self):
        # Implementation for running the VM
        pass