class Employee:
   

    def __init__(self,salary,increment):
        self.salary= salary
        self.increment=increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.increment=val -self.salary


e=Employee(5000,300)
print(e.salaryAfterIncrement)

e.salaryAfterIncrement=5560

print(e.increment)
