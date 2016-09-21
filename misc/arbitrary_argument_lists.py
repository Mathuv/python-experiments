# use * (*args, *vars) when you are not sure how many arguments might be passed to your function
def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}.{1}'.format(count, thing)

print_everything('apple', 'banana', 'cabbage')

# output
# 0.apple
# 1.banana
# 2.cabbage

# Use ** to handle named arguments that you have not defined in advance
def table_things(**kwargs):
    print('\n')
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)

table_things(apple='fruit', cabbage='vegetable')

# output
# cabbage = vegetable
# apple = fruit

# arbitrary argument lists can be used together with names arguments
def table_things2(titlestring, **kwargs):
    print '\n' + titlestring
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)

table_things2('Healthy stuffs', apple='fruit', cabbage='vegetable')

# output
# Healthy stuffs
# cabbage = vegetable
# apple = fruit


# * and ** syntax can be used when calling functions
def print_three_things(a, b, c):
    print 'a = {0}, b = {1}, c = {2}'.format(a, b, c)

my_list = ['aadvark', 'baboon', 'cat']
print '\n'
print_three_things(*my_list)

# output
# a = aadvark, b = baboon, c = cat
