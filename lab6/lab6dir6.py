import string

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        file.write(f"This is the content of {file_name}")


