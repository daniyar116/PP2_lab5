import re

def find_sequence(input_string):
    string = re.compile(r'[a-z]+_[a-z]+')
    return string.findall(input_string)
 