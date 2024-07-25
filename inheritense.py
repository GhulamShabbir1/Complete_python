class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"the name of a person is {self.name} and age is {self.age}")    

class language(person):
     def showlang(self):
        print(f"the name of a person is  and age is and the language of person is python")
a=person("ali",20) 
a.show()
b=language
b.showlang("hassan")
b.show()
