import time
import math


def calculate_square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    return result

number = input('Enter the number')
milliseconds = input('Enter the time on milliseconds')

result = calculate_square_root_after_milliseconds(number, milliseconds)
print({result})