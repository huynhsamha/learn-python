st = {'nodejs', 'php', 'java', 'python', 'angularjs', 'reactjs', 'angular 2', 'vuejs'}

print(st)

print('php' in st)
print('laravel' in st)

st.add('nodejs')
st.add('c++')
st.remove('nodejs')

while st:
    lang = st.pop()
    print(lang)


st = set('this is string with set')
print(st)
# {'n', 't', 'w', ' ', 'i', 'g', 's', 'h', 'r', 'e'}

st = {int((x+1)/2) for x in range(20)}
print(st)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}