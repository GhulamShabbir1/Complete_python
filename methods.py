#dir method

print("List")
x = [1, 2, 3]
print(dir(x))

print("Tuple")
y = (1, 2, 3)
print(dir(x))

print("Dictionary")
z = {1, 2, 3}
print(dir(x))

#__dict__

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)
print(p.__dict__)


# help method
print(help(Person))
print(help(x))