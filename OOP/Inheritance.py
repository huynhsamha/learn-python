class Animal:
    def __init__(self):
        print('Animal is ready')
    def whoami(self):
        print('is Animal')
    def callAnimal(self):
        print('Animal is called')
    def overrideCall(self):
        print('Animal not overide')

class Dog(Animal):
    def __init__(self):
        super().__init__() # call super class
        print('Dog is ready')
    def whoami(self):
        print('is Dog')
    def callDog(self):
        print('Dog is called')
    def overrideCall(self):
        print('Dog overide Animal call')

an = Animal()
an.whoami()
an.callAnimal()

dg = Dog()
dg.whoami()
dg.callAnimal()
dg.callDog()
dg.overrideCall()

'''
Output:

Animal is ready
is Animal
Animal is called
Animal is ready
Dog is ready
is Dog
Animal is called
Dog is called
Dog overide Animal call
'''