import subprocess

from logger import Logger, LoggerStatus


class Executor:
    @staticmethod
    def execute_command(commands: list):
        full_command = Executor.build_command(commands)
        result = subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stderr and result.stderr.__contains__("error"):
            Logger.add_record(text=result.stderr, status=LoggerStatus.ERROR)
            raise ValueError(result.stderr)
        if result.stdout:
            Logger.add_record(text=result.stdout, status=LoggerStatus.SUCCESS)
        return result.stdout

    @staticmethod
    def build_command(commands: list):
        result = []
        new_command = ""
        for command in commands:
            new_command += command.strip()
            if new_command.endswith("="):
                continue
            result.append(new_command)
            new_command = ""
        return result