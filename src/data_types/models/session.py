from typing import Dict, Any
from enum import Enum
from image import Image

class Status(Enum):
    RUNNING = "Running"
    LOADING = "Loading"
    ISSUE = "Issue"

class Session:
    def __init__(self, status: Status, image: Image, ssh_port: int) -> None:
        self.status = status
        self.image = image
        self.ssh_port = ssh_port

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Session':
        return cls(
            status=Status(data['status']),
            image=Image.from_dict(data['image']),
            ssh_port=data['ssh_port']
        )
