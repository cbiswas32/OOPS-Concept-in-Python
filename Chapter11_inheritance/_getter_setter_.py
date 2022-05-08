#Getter Setter

class Student:
    name="chinmoy"
    age=21
    salary=int(input("Enter Salary: "))
    bonus=int(input("Enter Bonus: "))
    

    #getter
    @property
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.bonus=val-self.salary
     


s=Student()

print(s.totalSalary)
s.totalSalary=5050
print(s.bonus)