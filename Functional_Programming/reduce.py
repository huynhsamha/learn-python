import functools

arr = ['a', 'b', 'c', 'd', 'e']

print(functools.reduce(lambda x, y: x + y, arr))
'''
abcde
'''

print(functools.reduce(lambda x, y: y + x, arr))
'''
edcba
'''