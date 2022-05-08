
#To change Class Attribute
class Employee:
    company="Camel"
    salary=100
    location="Delhi"
    
    #method 2
    # @classmethod
    # def changeSalary(cls,sal):
    #     cls.salary=sal
    
    def changeSalary(self,sal):
        #self.__class__.salary=sal #Method1
        self.salary=sal

e= Employee()
print(e.salary)
e.changeSalary(200)
print("e.changeSalary",e.salary)
# It will create an instance of salary .. 
# Will not change/update  the salary in Employee
print("Employee.salary =",Employee.salary) 


# We can solve this Problem using two Ways

'''
class Employee:
    company="Camel"
    salary=100
    location="Delhi"

    def changeSalary(self,sal):
        self.__class__.salary=sal

e= Employee()
print(e.salary)
e.changeSalary(200)
print("e.changeSalary",e.salary)

'''  

'''
class Employee:
    company="Camel"
    salary=100
    location="Delhi"

    @classmethod
    def changeSalary(self,sal):
        self.salary=sal

e= Employee()
print(e.salary)
e.changeSalary(200)
print("e.changeSalary",e.salary)


'''