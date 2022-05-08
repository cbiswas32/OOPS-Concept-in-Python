class Employee:
    company = "Bharat Gas"
    salary=5600
    slarybonus=500
    #totalSalary=6100

    #property decorator \ Getter

    @property
    def totalSalary(self):
        return self.salary + self.slarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.slarybonus=val-self.salary    

e=Employee()
print(e.totalSalary)

e.totalSalary=5700

print(e.slarybonus)
