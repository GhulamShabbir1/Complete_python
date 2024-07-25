# Their is no concept of public private and protected in python they only use as convention


#public
class person:
    def __init__(self):
        self.name="Ghulam Shabbir"

a=person()
print("print using public" ,a.name)

#private  syntax: __vaiable name 

class employee:
    def __init__(self):
        self.__name="Ghulam Shabbir"

b=employee()
print("print using private ",b._employee__name)  #name mangling


#protected  syntax : _variable name

class student:
    def __init__(self):
        self._name="Ghulam Shabbir"  #protected

c=student()
print("print using protected",c._name)
