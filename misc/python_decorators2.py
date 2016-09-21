"""
This decorator can be used with a function that takes any number of parameters
"""

from time import sleep

def sleep_decorator(function):

    """
    Limits how fast the function is called.
    :param function:
    :return:
    """

    def func_wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)

    return func_wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print print_number(num)


@sleep_decorator
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(10,15))

# OUTPUT
# 222
# 1
# 2
# 3
# 4
# 5
# 25

