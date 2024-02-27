import re

def match_string(input_string):
    string = re.compile(r'^a(bb|bbb)$')
    if string.match(input_string):
        return True
    else:
        return False

        