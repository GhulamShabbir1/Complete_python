class person:
    def __init__(self):
        self.name = "ali"
        self.age = 10
    def show(self):
        print(f"the name of a person is {self.name} and its age is {self.age}")   
#getter
    @property 
    def value(self):
        return self.name
#setter   
    @value.setter
    def value(self, newname):
        self.name = newname

a=person()
a.show()
a.value = "hasan"
print(a.value)
a.show()

