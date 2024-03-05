def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in the file: {line_count}")
    except FileNotFoundError:
        print("File not found.")
    except IsADirectoryError:
        print("The path provided is a directory, not a file.")

file_path = "your_text_file_path_here"
count_lines_in_file(file_path)
