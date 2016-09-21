"""
A lambda function is a function that takes any numbe rof arguments (including optional) and returns value of asingle
expression. They cant contain commands or more than one expressions.
"""


def f(x):
    return x*2

print f(3)
# OUTPUT
# 6

# Way 1
g = lambda x: x*2
print g(3)
# OUTPUT
# 6

# Way 2
print (lambda x: x*2)(3)
# OUTPUT
# 6

# multiple arguments
h = lambda x, y: x*y
print h(3, 5)

# optional arguments
i = lambda x, y, z=1: x*y*z
print i(3, 5)
print i(3, 5, 5)

# OUTPUT
# 15
# 75
