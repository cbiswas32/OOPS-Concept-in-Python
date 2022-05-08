class Person:
    country="India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def takeBreath(self):
        print("I am an Employee and I am luckily breathing...")

class Programmer(Employee):
    company="Fiver"
    def getSalary(self):
        print("no salary for programmer! ")

    def takeBreath(self):
        print("Programmer breathing")    

p=Person()
emp=Employee()
pr=Programmer()

p.takeBreath()
emp.takeBreath()
pr.takeBreath()

