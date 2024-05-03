class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2

s_= Shape()
print(s_.area())
s1 = Circle(5)
s2 = Square(10)
print(s1.area())
print(s2.area())
