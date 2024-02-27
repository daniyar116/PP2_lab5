import re

def split_string(input_string):
    words = re.findall('[A-Z][^A-Z]*', input_string)
    return words