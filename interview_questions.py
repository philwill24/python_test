original_string = "hello"
reversed_string = reversed(original_string)
reversed_string_using_loop = ''
for i in reversed_string:
    reversed_string_using_loop = reversed_string_using_loop + i
print(reversed_string_using_loop)

def reverse_string(word):
    return '' .join(reversed(word))

def test_reverse_string():
    input_str = "Tripleten"
    reversed_str = reverse_string(input_str)
    assert reversed_str == 'netelpirT'
    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)

def is_palindrome(word):
    reversed_str = '' .join(reversed(word))
    return word == reversed_str

def test_is_palindrome():
    input_str = "racecar"
    result = is_palindrome(input_str)
    assert result == True
    print("Test Passed! '" + input_str + "' is a palindrome.")

import math
print(math.factorial(5))

import math
def compute_factorial(number):
    return math.factorial(number)

def test_compute_factorial():
    input_number = 5
    result = compute_factorial(input_number)
    assert result == 120
    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))


