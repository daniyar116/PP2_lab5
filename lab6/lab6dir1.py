import os

def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(f"  {item}")
    
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(f"  {item}")

    print("\nAll directories and files:")
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(f"  {os.path.join(root, directory)}")
        for file in files:
            print(f"  {os.path.join(root, file)}")

path = "your_specified_path_here"
list_directories_files(path)