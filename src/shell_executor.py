import subprocess
from logger import Logger, LoggerStatus

class ShellExecutor:
    @staticmethod
    def execute_command(commands: list):
        full_command = ShellExecutor.build_command(commands)
        
        # Log the command before execution
        command_str = " ".join(full_command)
        Logger.add_record(text=f"Executing command: {command_str}", status=LoggerStatus.INFO)

        result = subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if (result.stderr and "error" in result.stderr.lower()):
            Logger.add_record(text=result.stderr, status=LoggerStatus.ERROR)
            raise ValueError(result.stderr)
        
        if result.returncode != 0:
            Logger.add_record(text=result.stdout, status=LoggerStatus.ERROR)
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
