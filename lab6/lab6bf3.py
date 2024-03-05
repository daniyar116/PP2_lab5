def is_palindrome(input_string):
    return input_string == input_string[::-1]

input_string = input(str('Enter the string: '))
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")