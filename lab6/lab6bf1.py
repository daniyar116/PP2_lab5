from functools import reduce

def multiply_numbers_in_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result
