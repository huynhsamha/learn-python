"""
Document:
"""


import functools
import operator

lmax = lambda xs: functools.reduce(lambda x, y: x if x > y else y, xs)
lmin = lambda xs: functools.reduce(lambda x, y: x if x < y else y, xs)

lsum = lambda xs: functools.reduce(operator.add, xs)
lmul = lambda xs: functools.reduce(operator.mul, xs)

lany = lambda pred, xs: functools.reduce(lambda x, y: x or pred(y), xs, False)
lall = lambda pred, xs: functools.reduce(lambda x, y: x and pred(y), xs, True)

lmap = lambda func, xs: functools.reduce(lambda x, y: x + [func(y)], xs, [])
lfilter = lambda func, xs: functools.reduce(lambda x, y: x + [y] if func(y) else x, xs, [])