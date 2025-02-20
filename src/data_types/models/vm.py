from typing import Dict, Any

class Vm:
    def __init__(
        self,
        iso_file: str,
        name: str = "example_name",
        ram_gb: str = "2"
    ) -> None:
        self.iso_file = iso_file
        self.name = name
        self.ram_gb = ram_gb

    def copy(self, idx: int) -> 'Vm':
        return Vm(
            name=self.name + f"_{idx}",
            ram_gb=self.ram_gb,
            iso_file=self.iso_file
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Vm':
        return cls(**data)
