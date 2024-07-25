class Shape:
  def __init__(self, x, y ,z): #this  constructor is inherited and used
    self.x = x
    self.y = y
    self.z= z
    
  def area(self):     #this  Function is inherited and used
      return self.x * self.y * self.z

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius ,radius)  #inherited constructor or method

    def area(self):
        return 3.14 *  super().area()  #function used
      
rec = Shape(3, 5, 6)
print(rec.area())

c = Circle(5)
print(c.area())