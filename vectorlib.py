import math
import numpy as np


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return (self.x, self.y)

    def __add__(self, o):
        return Vector2D(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector2D(self.x - o.x, self.y - o.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, factor):
        if isinstance(factor, float) or isinstance(factor, int):
            return Vector2D(factor * self.x, factor*self.y)
        return Vector2D(self.x*factor.x, self.y*factor.y)

    def __truediv__(self, factor):
        if isinstance(factor, float) or isinstance(factor, int):
            return Vector2D(factor / self.x, factor/self.y)
        return Vector2D(self.x/factor.x, self.y/factor.y)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def __eq__(self, obj):
        return obj.x == self.x and obj.y == self.y

    def length(self):
        return self.distance(Vector2D(0, 0))

    def distance(self, vec):
        distVect = self - vec
        return math.sqrt(distVect.x**2 + distVect.y**2)

    def perpendicular(self):
        x1 = self.x
        y1 = self.y
        v1_coef = -x1/y1
        v1 = -1

        v2 = v1_coef*v1

        return Vector2D(v1, v2)

    def normalize(self):
        if abs(self.x) > abs(self.y):
            return self/self.x
        return self/self.y

    def dot(self, vec):
        return self.x*vec.x+self.y*vec.y
