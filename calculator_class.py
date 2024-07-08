import math
class Calculator:
    def __init__(self, num):
        self.num = num 
        self.split = None
        self.total_amt = 0
        print(self.num)
        
    def sumfunction(self):
       self.total_amt = int(self.splited_data[0]) + int(self.splited_data[1])
       print(self.total_amt)
    

    def subFunction(self):
         self.total_amt = int(self.splited_data[0]) - int(self.splited_data[1])
         print(self.total_amt)

    def multFubnction(self):
         self.total_amt = int(self.splited_data[0]) * int(self.splited_data[1])
         print(self.total_amt)
    
    def divFunction(self):
         self.total_amt = int(self.splited_data[0]) / int(self.splited_data[1])
         print(self.total_amt)

    def squrefunction(self):
        self.total_amt = int(self.splited_data[0]) * int(self.splited_data[0])
        print(self.total_amt)



    def splitFunction(self):
        if '+' in self.num:
            print(self.num.split("+"))
            self.splited_data = self.num.split("+")
            print(self.splited_data)
            self.sumfunction()

        elif '-' in self.num:
            self.splited_data = self.num.split("-")
            self.subFunction()

        elif '*' in self.num:
            self.splited_data = self.num.split("*")
            self.multFubnction()

        elif '/' in self.num:
            self.splited_data = self.num.split("/")
            self.divFunction()
        
        else:
            print(math.sqrt(int(self.num)))
while True:
    print("Please Enter exit to exit")
    user_input = input("Enter a number")
    if user_input =="exit":  
       break  

    else:

        obj4 = Calculator(user_input)
        print(obj4.splitFunction())
            
