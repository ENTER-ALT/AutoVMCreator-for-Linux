import os
import re

from input_validator import InputValidator


class StringExtractor:

    @staticmethod
    def extract_folder_path_from_create_vm_output(output: str):
        pattern = r"Settings file: '(.*/)"
        folder_path = StringExtractor.extract_from_string_with_pattern(output, pattern)
        if not folder_path:
            raise ValueError("Folder path not found in " + folder_path)
        folder_path = folder_path.replace(" ", "\ ")
        return folder_path

    @staticmethod
    def extract_iso_path_from_user_input(user_input: str):
        pattern = r"--iso=(.*.iso)"
        iso_file = StringExtractor.extract_from_string_with_pattern(user_input, pattern)
        iso_file = os.path.expanduser(iso_file) # in case the user uses ~ in the path
        file_exists = InputValidator.validate_file_exists(iso_file)
        if not file_exists:
            raise ValueError(f"ISO file '{iso_file}' does not exist.")
        return iso_file

    @staticmethod
    def extract_from_string_with_pattern(text: str, pattern: str):
        # Search for the pattern in the text
        match = re.search(pattern, text)

        if match:
            return match.group(1)
        else:
            return False