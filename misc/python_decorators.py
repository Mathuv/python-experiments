"""
By definition, a decorator is a function that takes another function and
extends the behavior of the latter function without explicitly modifying it.
"""

import time

def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute
    :param some_function:
    :return wrapper:
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run this function: " + str((t2 - t1)) + "\n"

    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in range(100000000):
        num_list.append(num)
    print "\nSum of all the numbers: " + str(sum(num_list))


print my_function()

# OUTPUT
# Sum of all the numbers: 4999999950000000
# Time it took to run this function: 10.4305279255