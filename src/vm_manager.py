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

    def create_image(self):
        command_message = [
            CREATE_IMAGE_SCRIPT,
            self.vm_config.image_size_gb,
            self.vm_config.image_file_name,
        ]

        ShellExecutor.execute_command(command_message)

    def install_OS(self):
        command_message = [
            INSTALL_OS_SCRIPT,
            self.vm_config.iso_file_name,
            self.vm_config.image_file_name,
            RAM_OPTION,self.vm_config.ram_gb,
        ]

        ShellExecutor.execute_command(command_message)

    def create_linked_images(self, quantity):
        for i in range(quantity):
            linked_image_name = self.vm_config.image_file_name
            self.linked_images.append(linked_image_name)
            command_message = [
                CREATE_LINKED_IMAGES_SCRIPT,
                self.vm_config.image_file_name
            ]

            ShellExecutor.execute_command(command_message)

    def run_main_image(self):
        command_message = [
            RUN_MAIN_IMAGE_SCRIPT,
            self.vm_config.image_file_name,
        ]

        ShellExecutor.execute_command(command_message)

    def delete_vm(self):
        command_message = [
            DELETE_VM_SCRIPT,
            self.vm_config.image_file_name,
        ]

        ShellExecutor.execute_command(command_message)