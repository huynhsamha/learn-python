a = 'hello "double" \'single\''
a = "hello 'single' \"double\""
a = 'hello \n'
a = r'hello \n' # raw string
a = '''
    function solve(...args) {
        var a = [...args]
        console.log(a)
    }
'''
a = 'con' + 'cat'
a = 'con' 'cat ' 'without ' '+'
a = ('useful for paragraph '
    'with ' 'multiline.')

# print(a)

word = 'Python'
'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''
print(word[-1]) # n
print(word[-2]) # o
print(word[2:5]) # tho
print(word[-5:-2]) # yth
print(word[:2]) # Py
print(word[2:]) # thon
print(word[2:100]) # thon
print(word[:100]) # Python
print(word[100:]) #

print(len(word))

for c in word: print(c)
for i in range(len(word)): print(word[i])


s = 'Hello Python, I\'m Stupid-Dog'
print(s.capitalize())
print(s.upper())
print(s.lower())