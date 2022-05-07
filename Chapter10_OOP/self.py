class Employee:
    company= "Google"
    def getSalary(self):
        print("Salary is 100k")
        print(f"Salary for this employee working in {self.company} is {self.salary}")
    

    #Static Method
    #don't need parameter 'self' fo static method
    @staticmethod #its a decorator - is a funcion which modify a function
    
    def greet():
        print("Good morning")




harry=Employee()
harry.salary=20000
harry.getSalary() #Employee.getSalary(harry)
harry.greet()

'''
The Upper line converted in the Bello Line

Employee.getSalary(harry)



What is self?

Self is a parameter.
Self automatincally called when function is accessed using obj


'''
