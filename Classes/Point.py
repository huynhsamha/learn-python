import random
import math

class Point:
    "Point in 2D plane"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def __random_value__():
        return random.randint(-10, 10)

    @staticmethod
    def random():
        x = Point.__random_value__()
        y = Point.__random_value__()
        return Point(x, y)

    @staticmethod
    def distance(A, B):
        return math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)

    def display(self):
        print('(x ; y) = ({x} : {y})'.format(x = self.x, y = self.y))

    def dist(self, o):
        return Point.distance(self, o)