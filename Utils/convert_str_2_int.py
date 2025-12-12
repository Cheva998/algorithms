
from typing import Callable

def convert_string_to_int(string: str) -> int:
    N = len(string) - 1

    sign = 1
    index = 0
    if string[0] == '-':
        sign = -1
        index += 1

    number = 0
    while index <= N:
        char = string[index]
        if char < '0' or char > '9':
            raise Exception("String contains non digit characters")
        
        digit = ord(char) - ord('0')
        number = number * 10 + digit
        index += 1
    return number * sign
  

def test_function(func_to_test: Callable[str]) -> None:
    string_test1 = '-1'
    string_test2 = '0'
    string_test3 = '0143'
    string_test4 = '0-1-d2'

    expected1 = -1
    expected2 = 0
    expected3 = 143

    assert func_to_test(string_test1) == expected1
    assert func_to_test(string_test2) == expected2
    assert func_to_test(string_test3) == expected3
    try:
        func_to_test(string_test4)
        print("Test 4 didn't pass")
    except:
        print('All passed')


test_function(convert_string_to_int)