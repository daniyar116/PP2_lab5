def snake_to_camel(snake_string):
    comp= snake_string.split('_')
    camel_string = comp[0] + ''.join(x.title() for x in comp[1:])
    return camel_string 