class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x
        return self.x

    def set_y(self, new_y):
        self.y = new_y
        return self.y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(5, 4)
print(p)
p.set_x(10)
p.set_y(11)
print(p)
