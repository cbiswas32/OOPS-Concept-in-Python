class Calculator:
    def __init__(self,num):
        self.num=num

    def sqare(self):
        print(f"The value of sqare of {self.num} is {self.num**2}")


    def sqareRoot(self):
         print(f"The value of sqare ROOT of {self.num} is {self.num**.5}") 


    def cube(self):
        print(f"The value of cube of {self.num} is {self.num**3}")  

    @staticmethod
    def greet():
        print("Hello")


cal=Calculator(4)
cal.greet()
cal.sqare()
cal.sqareRoot()
cal.cube()
cal.greet()