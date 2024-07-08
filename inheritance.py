class ParentClass:
    def __init__(self, name):
        self.name = name
        self.class_type ="BSCIT"
        print("This is prent class")

class ChildClass(ParentClass):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

obj1= ChildClass("Anuj")
print(obj1.class_type)
obj1.printName()

class Parent2:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        print("this is parent class")
        print(f"{self.name} {self.address}")

class Child2(Parent2):
    def printNumber(self):
        print("This is number")

obj3 = Child2("Bibek", "Bouddha")