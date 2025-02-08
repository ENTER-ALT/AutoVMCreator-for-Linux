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
    def __init__(
        self,
        name="o10",
        folder="",
        os_type=OSType.LINUX_64.value,
        description="allo",
        hdd_size="10240",
        ram="1024",
        vram="8",
        cpus="1",
        nic1=NICMode.BRIDGED.value,
        autostart_enabled="off",
        drag_and_drop=DragAndDropMode.BIDIRECTIONAL.value,
        bridge_adapter="wlan0",
        iso_file="",
        disk_name="disk.vmdk"
    ) -> None:
        self.name = name
        self.folder = folder
        self.os_type = os_type
        self.description = description
        self.hdd_size = hdd_size
        self.ram = ram
        self.vram = vram
        self.cpus = cpus
        self.nic1 = nic1
        self.autostart_enabled = autostart_enabled
        self.drag_and_drop = drag_and_drop
        self.bridge_adapter = bridge_adapter
        self.iso_file = iso_file
        self.disk_name = disk_name

    def copy(self, idx):
        return VMConfig(
            name=self.name + f"_{idx}",
            folder=self.folder,
            os_type=self.os_type,
            description=self.description,
            hdd_size=self.hdd_size,
            ram=self.ram,
            vram=self.vram,
            cpus=self.cpus,
            nic1=self.nic1,
            autostart_enabled=self.autostart_enabled,
            drag_and_drop=self.drag_and_drop,
            bridge_adapter=self.bridge_adapter,
            iso_file=self.iso_file,
            disk_name=self.disk_name
        )

    @classmethod
    def from_dict(cls, data):
        return cls(**data)