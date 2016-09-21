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


# Returning a function from another function
def transform(n):
    return lambda x: x + n

f2 = transform(3)
print f2(4)

# OUTPUT
# 7
# Combining elements of an iterable sequence with reduce()
x = reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print x

# OUTPUT
# 1, 2, 3, 4, 5, 6, 7, 8, 9

# Sorting by an alternate key
rel = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
print rel

# OUTPUT
# [5, 4, 6, 3, 7, 2, 8, 1, 9]