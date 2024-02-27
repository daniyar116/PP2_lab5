import re

def find_sequence(input_string):
    string = re.compile(r'[A-Z][a-z]+')
    return string.findall(input_string)