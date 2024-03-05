import os

def check_access(path):
    print(f"Checking access for path: {path}")
    if os.path.exists(path):
        print("Path exists")
        if os.access(path, os.R_OK):
            print("Readable")
        else:
            print("Not readable")
        if os.access(path, os.W_OK):
            print("Writable")
        else:
            print("Not writable")
        if os.access(path, os.X_OK):
            print("Executable")
        else:
            print("Not executable")
    else:
        print("Path does not exist")

path = "your_specified_path_here"
check_access(path)