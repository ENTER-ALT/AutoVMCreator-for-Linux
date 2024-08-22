from configs.vm_config import VMConfig
from configs.storagecontroller_config import StorageControllerConfig
from configs.medium_attachment_config import MediumAttachmentConfig, DriveType
from configs.medium_config import MediumConfig, HDDMediumConfig
from executor import Executor
from string_extractor import StringExtractor
from logger import Logger, LoggerStatus
from command_shortcuts import *


class Creator:
    @staticmethod
    def create_vm(vm_config: VMConfig):
        command_message_list = [
            VBOXMANAGE_COMMAND, CREATEVM_COMMAND,
            NAME_OPTION, vm_config.name,
            OSTYPE_OPTION, vm_config.os_type,
            REGISTER_OPTION
        ]
        command_message = ' '.join(command_message_list)
        output = Executor.execute_command(command_message_list)
        vm_config.folder = StringExtractor.extract_folder_path_from_create_vm_output(output)
        Logger.add_record(text=command_message, status=LoggerStatus.SUCCESS)

    @staticmethod
    def modify_vm(vm_config: VMConfig):
        command_message_list = [
            VBOXMANAGE_COMMAND, MODIFYVM_COMMAND,
            vm_config.name,
            DESCRIPTION_OPTION, vm_config.description,
            MEMORY_OPTION, str(vm_config.ram),
            VRAM_OPTION, str(vm_config.vram),
            CPUS_OPTION, str(vm_config.cpus),
            NIC1_OPTION, vm_config.nic1,
            AUTOSTART_ENABLED_OPTION, str(vm_config.autostart_enabled),
            DRAG_AND_DROP_OPTION, vm_config.drag_and_drop,
            BRIDGE_ADAPTER1_OPTION, vm_config.bridge_adapter
        ]
        command_message = ' '.join(command_message_list)
        Executor.execute_command(command_message_list)
        Logger.add_record(text=command_message, status=LoggerStatus.SUCCESS)

    @staticmethod
    def create_storage_controller(vm_config: VMConfig, storage_controller_config: StorageControllerConfig):
        command_message_list = [
            VBOXMANAGE_COMMAND, STORAGECTL_COMMAND,
            vm_config.name,
            NAME_OPTION, storage_controller_config.name,
            ADD_OPTION, storage_controller_config.add,
            CONTROLLER_OPTION, storage_controller_config.controller
        ]
        command_message = ' '.join(command_message_list)
        Executor.execute_command(command_message_list)
        Logger.add_record(text=command_message, status=LoggerStatus.SUCCESS)

    @staticmethod
    def create_hdd_medium(medium_config: HDDMediumConfig):
        command_message_list = [
            VBOXMANAGE_COMMAND, CREATEMEDIUM_COMMAND,
            medium_config.medium_type,
            FILENAME_OPTION, medium_config.filename,
            SIZE_OPTION, str(medium_config.size),
            FORMAT_OPTION, medium_config.format,
            VARIANT_OPTION, medium_config.variant
        ]
        command_message = ' '.join(command_message_list)
        Executor.execute_command(command_message_list)
        Logger.add_record(text=command_message, status=LoggerStatus.SUCCESS)

    @staticmethod
    def attach_medium_to_controller(
            vm_config: VMConfig,
            storage_controller_config: StorageControllerConfig,
            medium_config: MediumConfig,
            medium_attachment_config: MediumAttachmentConfig):
        command_message_list = [
            VBOXMANAGE_COMMAND, STORAGEATTACH_COMMAND,
            vm_config.name,
            STORAGECTL_OPTION, storage_controller_config.name,
            PORT_OPTION, str(medium_attachment_config.port),
            TYPE_OPTION, medium_attachment_config.drive_type,
            MEDIUM_OPTION, medium_config.filename
        ]
        command_message = ''.join(command_message_list)
        Executor.execute_command(command_message_list)
        Logger.add_record(text=command_message, status=LoggerStatus.SUCCESS)

    @staticmethod
    def create_attachment_config(
            controller: StorageControllerConfig,
            medium: MediumConfig,
            drive_type: DriveType):
        attachment = MediumAttachmentConfig(controller.name, drive_type, 1, medium.filename)
        return attachment