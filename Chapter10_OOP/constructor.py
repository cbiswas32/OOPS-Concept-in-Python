class Employee:
    company= "Google"


    #Special method 
    #it automatically run
    #its called constractor
    def __init__(self, name, salary,subunit):
        self.name= name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getDetails(self):
        print(f"Salary {self.salary}")
        print(f"Company {self.company}")
         

   

chinmoy = Employee("Harry",20120,"Youtube")
# chinmoy = Employee() This throws an error .. 3 arg are needed
chinmoy.getDetails()