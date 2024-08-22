from enum import Enum

class NICMode(Enum):
    BRIDGED = "bridged"
    NAT = "nat"

class DragAndDropMode(Enum):
    DISABLED = "disabled"
    BIDIRECTIONAL = "bidirectional"

class OSType(Enum):
    LINUX_64 = "Linux_64"

class VMConfig:
    def __init__(self) -> None:
        self.name = "o10"
        self.folder = ""
        self.os_type = OSType.LINUX_64.value
        self.description = "allo"
        self.ram = "1024"
        self.vram = "8"
        self.cpus = "1"
        self.nic1 = NICMode.BRIDGED.value
        self.autostart_enabled = "off"
        self.drag_and_drop = DragAndDropMode.BIDIRECTIONAL.value
        self.bridge_adapter = "wlan0"
        