# Example of Hybrid Inheritance 
class BaseClass:
  def __init__(self,name):
    self.name = "ghulam shabbir"
    print(f"The name of a person is :  {self.name}")
    

class Derived1(BaseClass):
  def __init__(self,age):
    self.age = 20
    print(f"The age of a person is :  {self.age}")
    super().__init__(age) 

class Derived2(BaseClass):
  def __init__(self,height):
    self.height = 180
    print(f"The height of a person is :  {self.height}")
    super().__init__(height)

class Derived3(Derived1, Derived2):
  def __init__(self,gender):
    self.gender = gender
    print(f"The gender of a person is :   {self.gender}")
    super().__init__(gender)
  
d=Derived3("male")

print(d)
