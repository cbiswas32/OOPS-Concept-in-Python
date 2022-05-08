
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




e = Employee()
p=Programmer()

e.showDetails()

#overriding
p.showDetails()


print(Employee.company)      
print(Programmer.company)      
