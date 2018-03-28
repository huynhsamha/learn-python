a = 5
b = 6
s = 'Hello Python, I\'m Stupid-Dog'

print(a, '+', b, '=', a+b)

print(s)
print(s.capitalize())
print(s.upper())
print(s.lower())

split = ', '
array = ['Windows', 'Linux', 'MacOS']
print(split.join(array))

for i in range(3, 8): print(i)
for i in range(len(array)): print(i, ':', array[i])

class OS:
    'This is Operating Systems'

    windowsCount = 0
    linuxCount = 0
    macOSCount = 0

    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MACOS = 'MacOS'

    def __init__(self, name, version):
        self.name = name
        self.version = version
        if (name == OS.WINDOWS): OS.windowsCount += 1
        elif (name == OS.LINUX): OS.linuxCount += 1
        elif (name == OS.MACOS): OS.macOSCount += 1

    def display(self):
        print(self.name, self.version)

os = []

os.append(OS('Windows', '7'))
os.append(OS('Windows', '8'))
os.append(OS('Windows', '8.1'))
os.append(OS('Windows', '10'))

os.append(OS('Linux', '12'))
os.append(OS('Linux', '13'))
os.append(OS('Linux', '14'))
os.append(OS('Linux', '15'))
os.append(OS('Linux', '16'))

os.append(OS('MacOS', '10.0'))
os.append(OS('MacOS', '10.1'))
os.append(OS('MacOS', '10.2'))
os.append(OS('MacOS', '10.3'))

print(OS.__doc__)

print(OS.windowsCount)
print(OS.linuxCount)
print(OS.macOSCount)

for i in range(len(os)):
    o = os[i]
    o.display()