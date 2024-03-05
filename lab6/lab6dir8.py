import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully")
        else:
            print(f"No write access to {file_path}")
    else:
        print(f"File {file_path} does not exist")

file_path = "file_to_delete.txt"
delete_file(file_path)
