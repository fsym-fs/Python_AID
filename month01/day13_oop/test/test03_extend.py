class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y-other.y)

    def __str__(self):
        return "向量的x为%d,向量的y为%d" % (self.x, self.y)

    def __mul__(self, other):
        return Vector(self.x*other.x, self.y*other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self


v1 = Vector(3, 6)
v2 = Vector(2, 3)
print(v1-v2)
print(v1*v2)
v1 -= v2
print(v1)
