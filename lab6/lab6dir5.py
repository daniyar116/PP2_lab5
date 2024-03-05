def write_list_to_file(file_path, input_list):
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')

