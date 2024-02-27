import re

def insert_spaces(input_string):
    changed_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', input_string)
    return changed_string