from enum import Enum

class MediumType(Enum):
    DISK = "disk"

class FormatType(Enum):
    VMDK = "VMDK"

class VariantType(Enum):
    STANDARD = "Standard"


class MediumConfig:
    def __init__(self, file_path: str):
        self.filename = file_path

class HDDMediumConfig(MediumConfig):
    def __init__(self, folder_path: str, size: str = "10240"):
        super().__init__(folder_path)
        self.medium_type = MediumType.DISK.value
        self.size = size
        self.format = FormatType.VMDK.value
        self.variant = VariantType.STANDARD.value