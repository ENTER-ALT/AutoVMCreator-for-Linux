from enum import Enum

class BusType(Enum):
    SATA = "sata"

class ControllerType(Enum):
    INTEL_AHCI = "IntelAHCI"

class StorageControllerConfig:
    def __init__(self):
        self.name = "SC"
        self.add = BusType.SATA.value
        self.controller = ControllerType.INTEL_AHCI.value