import sys

from string_extractor import StringExtractor


class UserInterface:
    @staticmethod
    def start():
        if len(sys.argv) <= 1:
            raise ValueError("You should give the path to the ISO file as an argument using --iso=PATH_TO_ISO_FILE")
        user_input = " ".join(sys.argv[1:])
        iso_path = StringExtractor.extract_iso_path_from_user_input(user_input)
        return iso_path


    @staticmethod
    def end():
        print("VM Creation Completed Successfully 󰄛")

