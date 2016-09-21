"""
FunctionWrapper is a design pattern used when dealing with relatively complicated functions.
The wrapper function typically performs some prologue and epilogue tasks like

* allocating and disposing resources
* checking pre- and post-conditions
* caching / recycling a result of a slow computation

but otherwise it should be fully compatible with the wrapped function, so it can be used instead of it.
"""


def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)
            return result
        return call
    return decorate


def trace_in(func, *args, **kwargs):
    print "Entering function", func.__name__


def trace_out(func, *args, **kwargs):
    print "Leaving function", func.__name__


@wrap(trace_in, trace_out)
def calc(x, y):
    return x + y

print(calc(5, 10))

# OUTPUT
# Entering function calc
# Leaving function calc
# 15
