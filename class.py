class ClassWithDate:
    def _init_(self, name, address):
        self.name = name
        self.address = address

        print(self.name)
        print(self.address)
    
obj2 = ClassWithDate('Anuj', "Sundarijal")

class mulipleFunctionClass:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def printName(self):
        print(self.name)
    
    def printAge(self):
        print(self.age)

    def printAddress(self):
        print(self.address)
        
obj3 = mulitpleFunctionClass('Anuj', 20, 'Sundarijal')


       
    

