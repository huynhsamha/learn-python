from collections import deque

a = deque([8, 5, 1, 2, 9])
print(a)

a.appendleft(3)
a.pop()

while a:
    i = a.pop()
    if (i < 7): a.appendleft(i + 1)
    print(i)

print(a)