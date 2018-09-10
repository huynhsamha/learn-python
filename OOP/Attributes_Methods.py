class User:
    '''Doccument about class User'''

    # Class Attributes
    version = '1.2.42'
    
    # Instance Attributes
    def __init__(self, username, password):
        self.username = username
        self.password = self.hashPassword(password)

    # Instance Methods
    def hashPassword(self, password):
        return password + self.username
    
    def authenticatePassword(self, password):
        return self.password == self.hashPassword(password)


user = User('nty5246', 'HF8930HF390FJ29HT239J')

print(user.username)
print(user.password)
print(user.version) # 1.2.42
print(user.__class__.version) # 1.2.42

user.version = '2.0.0'

print(user.version) # 2.0.0
print(user.__class__.version) # 1.2.42

print(user.__doc__) # Doccument about class User

print(user.authenticatePassword('wrong')) # False
print(user.authenticatePassword('HF8930HF390FJ29HT239J')) # True
