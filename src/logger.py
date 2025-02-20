from time import ctime
from enum import Enum, auto
import os

class LoggerStatus(Enum):
    ERROR = auto()
    SUCCESS = auto()

class Logger:
    filename = os.path.join(os.path.dirname(__file__), "build_debug.log")

    @staticmethod
    def add_record(text: str, *, status: LoggerStatus) -> None:
        formatted_text = f"[{status}] | {text} | {ctime()}\n"
        print(formatted_text, end='')

        with open(Logger.filename, "a", encoding="UTF-8") as file:
            file.write(formatted_text)

