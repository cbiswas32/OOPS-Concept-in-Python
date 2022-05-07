class Employee:
    company= "Google"
    

    #Static Method
    #don't need parameter 'self' fo static method
    @staticmethod #its a decorator - is a funcion which modify a function    
    def greet():
        print("Good morning")

    @staticmethod
    def time():
        print("It's 9AM in the Morning")

chinmoy = Employee()

chinmoy.greet() #Employee.greet()

chinmoy.time()
