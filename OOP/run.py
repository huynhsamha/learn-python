'''
Multiple Inheritance in Python

Like C++, a class can be derived from more than one base classes in Python. 

'''

class A:
    def __init__(self):
        print('A init')
    def c0(self):
        print('A -> c0')
    def a1(self):
        print('a1')
    def a2(self):
        print('a2')

class B:
    def __init__(self):
        print('B init')
    def c0(self):
        print('B -> c0')
    def b1(self):
        print('b1')
    def b2(self):
        print('b2')


class C(A, B):
    def __init__(self):
        print('C init')
    def a1(self):
        print('a1 -> c1')
    def b2(self):
        print('b2 -> c2')

c = C()
c.a1()
c.a2()
c.b1()
c.b2()
c.c0()

'''
Output:

C init
a1 -> c1
a2
b1
b2 -> c2
A -> c0
'''