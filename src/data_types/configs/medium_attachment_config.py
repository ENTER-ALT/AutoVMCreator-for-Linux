from enum import Enum
from data_types.configs.storage_controller_config import StorageControllerConfig
from data_types.configs.medium_config import MediumConfig

class DriveType(Enum):
    HDD = "hdd"
    DVD_DRIVE = "dvddrive"


class MediumAttachmentConfig:
    def __init__(self, storage_name: str, drive_type: DriveType, port: int, medium: str):
        self.storage_name = storage_name
        self.drive_type = drive_type.value
        self.port = str(port)
        self.medium = medium
        
    @staticmethod
    def create_attachment_config(
            controller: StorageControllerConfig
            , medium: MediumConfig
            , drive_type: DriveType
            , port: int):
        attachment = MediumAttachmentConfig(controller.name, drive_type, port, medium.filename)
        return attachment