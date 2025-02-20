class VMConfig:
    def __init__(
        self,
        name="example_name",
        image_size_gb="15",
        ram_gb="2",
        image_file_name="example.img",
        iso_file_name=""
    ) -> None:
        self.name = name
        self.image_size_gb = image_size_gb
        self.ram_gb = ram_gb
        self.image_file_name = image_file_name
        self.iso_file_name = iso_file_name

    def copy(self, idx):
        return VMConfig(
            name=self.name + f"_{idx}",
            image_size_gb=self.image_size_gb,
            ram_gb=self.ram_gb,
            image_file_name=self.image_file_name,
            iso_file_name=self.iso_file_name
        )

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
