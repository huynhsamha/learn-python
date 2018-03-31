a = [1, 5, 9, 2, 5, 6]
b = [56, 13, 12, 65, 34, 26]

print(len(a))
print(a[2])
print(a[-5])
print(a[:])

c = a+b
print(c)

a[2] = 15
a.append(35)
a[3:5] = [0, 5] # a[3] = 0, a[4] = 5
a[1] = [] # assign empty array for a[1]
print(a)
# [1, 5, 0, [], 0, 5, 6, 35]

a[1:2] = [] # remove a[3]
print(a)
# [1, 15, 0, 5, 6, 35]

sum = 0
for i in range(len(a)): sum += a[i]
print(sum) # 62
for v in a: sum -= v
print(sum) # 0

r = range(4, 9)
print(r) # range(4, 9)
l = list(r)
print(l) # [4, 5, 6, 7, 8]


a.clear() # make a empty
print(a)
del a # destroy a


sep = ', '
lang = ['en', 'vi', 'ru', 'ja', 'ko', 'fr']
s = sep.join(lang)
print(s) # en, vi, ru, ja, ko, fr


a = [(1, 'f'), (2, 'c'), (3, 'd'), (4, 'k')]
a.sort(key = lambda v: v[1])
print(a)
# [(2, 'c'), (3, 'd'), (1, 'f'), (4, 'k')]


a = [9, 8, 1, 1, 5, 6, 1, 3]
a.append(12)
a.insert(3, 15)
a.remove(1) # first apperance
print(a)
print(a.count(1))
print(a.index(5)) # 4
a.append(5)
print(a.index(5, 5)) # start from index 5 # 9
a.reverse()
print(a)
a.sort()
print(a)
b = a.copy() # shallow copy
c = a