import subprocess


class Executor:
    @staticmethod
    def execute_command(command: list):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stderr:
            raise ValueError(result.stderr + "\n" + ''.join(command))
        return result.stdout