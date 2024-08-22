import os


class InputValidator:
    @staticmethod
    def validate_file_exists(filepath: str):
        if os.path.exists(filepath):
            return True
        else:
            return False