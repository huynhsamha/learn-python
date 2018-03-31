a = dict(hello='xin chao', awesome='kinh hoang', lovely='de thuong')

b = {x: x**2 for x in range(10)}


print(a, b)

print(a.get('lovely'))
print(a['lovely'])

print(a.items())
# dict_items([('lovely', 'de thuong'), ('awesome', 'kinh hoang'), ('hello', 'xin chao')])
print(a.values())
# dict_values(['de thuong', 'kinh hoang', 'xin chao'])
print(a.keys())
# dict_keys(['awesome', 'lovely', 'hello'])

g = a.pop('hello')
print(g, a)
# xin chao {'lovely': 'de thuong', 'awesome': 'kinh hoang'}

a.update({'lovely': 'dang so', 'good': 'gioi'})
print(a)
# {'awesome': 'kinh hoang', 'good': 'gioi', 'lovely': 'dang so'}


for k, v in a.items(): print(k, v)

for k in sorted(a): print(k)