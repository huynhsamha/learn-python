s = 'Hello world'
print(s)
print(str(s))
print(repr(s))
# Hello world
# Hello world
# 'Hello world'



# right-justified
print('|', repr(15).rjust(7), '|')
# center layout
print('|', repr(15).center(7), '|')
# left-justified
print('|', repr(15).ljust(7), '|')
# |      15 |
# |    15   |
# | 15      |



print('{0} * {1} = {2}'.format(8, 15, 120))
print('{0:2d} * {1:2d} = {2:3d}'.format(8, 15, 120))
print('{a:2d} + {b} = {0}'.format(120, a = 8, b = 15))

print('{:.9f}'.format(3.497984709824089132))
# 3.497984710

m = {'a': 1, 'b': 2}
print('value of b: {b:d}, value of a: {a:d}'.format(**m))
# value of b: 2, value of a: 1


print('12'.zfill(5)) # zero fill
# 00012


print('''this is old format string:
    int: %05d
    float: %.3f
    string: %s
''' % (15, 3.141414, 'stupid'))
'''
this is old format string:
    int: 00015
    float: 3.141
    string: stupid
'''