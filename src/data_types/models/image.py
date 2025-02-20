from typing import Optional, Dict, Any
from src.data_types.models.vm import VM

class Image:
    def __init__(
        self,
        vm: VM,
        image_file_name: str = "example.img",
        backup_image: Optional[Image] = None,
        size_gb: str = "15",
        installed: bool = False
    ) -> None:
        self.image_file_name = image_file_name
        self.backup_image = backup_image
        self.size_gb = size_gb
        self.vm = vm
        self.installed = installed

    def copy(self, idx: int) -> 'Image':
        return Image(
            image_file_name=self.image_file_name + f"_{idx}",
            backup_image=self.backup_image,
            size_gb=self.size_gb,
            vm=self.vm,
            installed=self.installed
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Image':
        return cls(**data)
