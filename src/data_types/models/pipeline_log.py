from typing import Dict, Any
from enum import Enum
from image import Image

class Status(Enum):
    SUCCESS = "Success"
    ERROR = "Error"

class PipelineLog:
    def __init__(
        self,
        playbook_file: str,
        status: Status,
        image: Image
    ) -> None:
        self.playbook_file = playbook_file
        self.status = status
        self.image = image

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PipelineLog':
        return cls(
            playbook_file=data['playbook_file'],
            status=Status(data['status']),
            image=Image.from_dict(data['image'])
        )
