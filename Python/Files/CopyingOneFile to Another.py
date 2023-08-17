def copy_file(source_file, destination_file):
    try:
        # if not source_file:
        #     print("Source file not found")
        #     return 0
        with open(source_file, 'r') as source:
            contents = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(contents)

        print(f"Contents of {source_file} copied to {destination_file} successfully.")

    except FileNotFoundError:
        print("File not found")


source_file_path = 'C:\\Users\\mouni\\IdeaProjects\\datastructures\\Python\\Files\\students.txt'
destination_file_path = 'C:\\Users\\mouni\\IdeaProjects\\datastructures\\Python\\Files\\students1copy.txt'

copy_file(source_file_path, destination_file_path)





