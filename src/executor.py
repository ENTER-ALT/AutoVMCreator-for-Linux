import subprocess
from operator import rshift

from logger import Logger, LoggerStatus


class Executor:
    @staticmethod
    def execute_command(command: list):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stderr:
            Logger.add_record(text=result.stderr, status=LoggerStatus.ERROR)
            raise ValueError(result.stderr + "\n" + ' '.join(command))
        return result.stdout