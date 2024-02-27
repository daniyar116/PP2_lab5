import re

def camel_to_snake(input_string):
    snake_string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', input_string).lower()
    return snake_string
