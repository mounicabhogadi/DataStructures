import os.path

# 1 try except
# def copy_file(source_file, destination_file):
#     """
#     copy source file to target file
#     :param source_file: absolute/relative path of source file
#     :type source_file: string
#     :param destination_file: absolute/relative path of source file
#     :type destination_file: string
#     :return: None
#     :rtype: None
#     :raises: handling exception
#     """
#     try:
#         # if not source_file:
#         #     print("Source file not found")
#         #     return 0
#         with open(source_file, 'r') as source:
#             contents = source.read()
#
#         with open(destination_file, 'w') as destination:
#             destination.write(contents)
#
#         print(f"Contents of {source_file} copied to {destination_file} successfully.")
#
#     except FileNotFoundError:
#         print("File not found")
#
#
# source_file_path = 'C:\\Users\\mouni\\IdeaProjects\\datastructures\\Python\\Files\\student.txt'
# destination_file_path = 'C:\\Users\\mouni\\IdeaProjects\\datastructures\\Python\\Files\\students1copy.txt'
#
# copy_file(source_file_path, destination_file_path)


# 2

def check_for_empty_or_none(*args):
    for arg in args:
        if arg is None:
            raise Exception("One of the argument is None")
        if arg == "":
            raise Exception("One of the argument is None")


def copy(source_file, target_file):
    """
    copy source file to target file
    :param source_file: absolute/relative path of source file
    :type source_file: string
    :param target_file: absolute/relative path of target file
    :type target_file: string
    :return: None
    :rtype: None
    :raises: Exception when inputs or bad or cannot copy a file
    """
    if source_file is None or target_file is None:
        raise Exception("Source or Target file is Null/None")
    if source_file == "" or target_file == "":
        raise Exception("Source or target file are empty strings")

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, 'r') as source:
        contents = source.read()

    with open(target_file, 'w') as target:
        target.write(contents)


def move(source_file, target_file):
    """
    move source file to target file
    :param source_file: absolute/relative path of source file
    :type source_file: string
    :param target_file: absolute/relative path of target file
    :type target_file: string
    :return: None
    :rtype: None
    :raises: Exception when inputs or bad or cannot copy a file
    """
    check_for_empty_or_none(source_file, target_file)
    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, 'r') as source:
        contents = source.read()

    with open(target_file, 'w') as target:
        target.write(contents)
        os.remove(source_file)



if __name__ == '__main__':
    source_file_path = 'C:\\Users\\mouni\\IdeaProjects\\datastructures\\Python\\Files\\students.txt'
    # creates a new .txt
    target_file_path = 'C:\\Users\\mouni\\IdeaProjects\\datastructures\\Python\\Files\\students_copy.txt'
    copy(source_file=source_file_path, target_file=target_file_path)
    #move(source_file=source_file_path, target_file=target_file_path)
    print("Copied Successfully")


