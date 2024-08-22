

from enum import Enum

class DriveType(Enum):
    HDD = "hdd"
    DVD_DRIVE = "dvddrive"


class MediumAttachmentConfig:
    def __init__(self, storage_name: str, drive_type: DriveType, port: int, medium: str):
        self.storage_name = storage_name
        self.drive_type = drive_type.value
        self.port = str(port)
        self.medium = medium