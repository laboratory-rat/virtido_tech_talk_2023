import os


def read_file_as_string(file_path: str) -> str:
    """
    Read file from disk.
    :param file_path: path to file
    :return: file content as string
    """

    with open(file_path, "r") as f:
        return f.read()


def write_file(file_path: str, file_content: str):
    """
    Safe write file to disk.
    :param file_path: path to file
    :param file_content: content to write
    """

    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w", encoding='utf8') as f:
        f.write(file_content)


def get_file_name_with_no_extension(full_file_name: str) -> str:
    """
    Get file name with no extension.
    :param full_file_name: full file name
    :return: file name with no extension
    """

    return os.path.splitext(os.path.basename(full_file_name))[0]
