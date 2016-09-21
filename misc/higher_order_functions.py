"""
Higher-order function is a function which does either (Functions that act on or return other functions
    1). takes one or more functions as arguments
    2). returns a function as it's result
"""


def twice(function):
    return lambda x: function(function(x))


def f(x):
    return x + 3

g = twice(f)

print g(7)

# OUTPUT
# 13
