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