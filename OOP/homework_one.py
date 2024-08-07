print("--Line--")
class Line:
    x1 = 0
    y1 = 0

    x2 = 0
    y2 = 0

    def __init__(self, cord1, cord2):
        (self.x1, self.y1) = cord1
        (self.x2, self.y2) = cord2

    def distance(self):
        x_difference = (self.x2 - self.x1)**2
        y_difference = (self.y2 - self.y1)**2
        distance = (x_difference + y_difference)**0.5
        return distance

    def slope(self):
        m = (self.y2-self.y1) / (self.x2 - self.x1)
        return m

cordinate1 = (3,2)
cordinate2 = (8,10)

li = Line(cord1=cordinate1, cord2=cordinate2)
print(li.distance())
print(li.slope())

print("--Cylinder--")
class Cylinder:
    pi = 3.142

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v = self.pi * (self.radius)**2 * self.height
        return v

    def surface_area(self):
        sa = 2 * self.pi * self.radius * (self.radius + self.height)
        return sa

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())