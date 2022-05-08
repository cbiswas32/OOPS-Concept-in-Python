# Inheritance is a way of creating a new class from an existing class

#      DRY - Do Not Repeat    Principal

# -- Base class / Parent class
'''
class Employee:
    code
    ......

'''

# ------ Child class / Derived class

'''
class Program(Employee):
    #code

'''


class Employee:
    company="Gooogle"
    def showDetails(self):
        print("This is an employeee")
class Programmer(Employee):
    company="Facebook"
    lang="python"
    def getLanguage(self):
        print(f"the language is {self.lang}")    
    def showDetails(self):
        print("This is an Programmer")

class Programmer2(Employee):
    hi="hiiiii"


e = Employee()
p=Programmer()

e.showDetails()

#overriding
p.showDetails()


print(Employee.company)      
print(Programmer.company)      
print(Programmer2.company)      