class Circle:
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def area(self):
        return self.pi * self.radius**2

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __gt__(self, other):
        print('gt')
        return self.radius > other.radius

    def __lt__(self, other):
        print('lt')
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


c1 = Circle(2)
c2 = Circle(5)
c3 = c1 + c2
print(c3)
print(c1 == c2)
print(c1 < c2)
print(c1.area())
print(Circle.pi)
print(dir(Circle))
