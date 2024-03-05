def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"File copied successfully from {source_file} to {destination_file}")
    except FileNotFoundError:
        print("File not found")

source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
