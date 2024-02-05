import os


def get_file_path_in_same_folder(__file__: str, file_name: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
