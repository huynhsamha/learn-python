def doc_func():
    """This is document for function"""

print(doc_func.__doc__)
# This is document for function


def print_fib(n):
    """Print fibonaci sequence"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print_fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597


def build_fib(n):
    """Return fibonaci sequence"""
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a+b
    return res

a = build_fib(2000)
print(a)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]


def default_argument(a, b = 5, c = 'awesome', d = 9):
    print(a, b, c, d)

default_argument(123) 
# 123 5 awesome 9
default_argument(123, b = 0) 
# 123 0 awesome 9
default_argument(123, 0)
# 123 0 awesome 9
default_argument(123, d = 0, c = 'good luck')
# 123 5 good luck 0
default_argument(123, 1, 2, 'what')
# 123 1 2 what


def args_func(*args):
    for arg in args: print(arg, end=' ')
    print()
args_func(1, 'A', 5)

def key_func(**keys):
    for key in keys: print(key, ':', keys[key])
key_func(a = 1, b = 2, c = 'c')

def combine_func(rad = 0, *args, **keys):
    print(rad)
    for i in args: print(i, end=' ')
    print()
    for key in keys: print(key, ':', keys[key])
combine_func(123, 1, 'a', 2, a = 5, b = 6, c = 'c')