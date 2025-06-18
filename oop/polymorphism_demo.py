import math

class Shape:

  def area(self):
    raise NotImplementedError
  

class Rectangle(Shape):
  
  def __init__(self, length: float, width: float):
    self.length = length
    self.width = width
    super().__init__()

  def area(self):
    return self.length * self.width

class Circle(Shape):
  
  def __init__(self, radius: float):
    self.radius = radius
    super().__init__()

  def area(self):
    return math.pow(self.radius, 2) * math.pi
