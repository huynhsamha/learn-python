class Computer:

    def __init__(self):
        # private attribute, cannot change directly
        # only change in class scope
        # prefix with __
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    # setter for change private attribute
    def setMaxPrice(self, price):
        self.__maxprice = price # change private attribute in class

c = Computer()
c.sell()

# change the price => not working with private attribute
c.__maxprice = 1000
c.sell()

# using setter function => working for change
c.setMaxPrice(1000)
c.sell()


'''
Output:

Selling Price: 900
Selling Price: 900
Selling Price: 1000
'''
