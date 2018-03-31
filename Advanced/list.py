a = [x**2 for x in range(4, 10)]
print(a)
# [16, 25, 36, 49, 64, 81]

a = [(x, y) for x in [1, 2, 3] for y in [-2, 3, -1] if x != y]
print(a)
# [(1, -2), (1, 3), (1, -1), (2, -2), (2, 3), (2, -1), (3, -2), (3, -1)]

v = [-5, -7, 1, 0, -3, 5, 2, 0]
a = [x for x in v if x >= 0]
a = [abs(x) for x in v]
a = [(x, 2*x+5) for x in v if 2*x+5 < 0]

print(a)