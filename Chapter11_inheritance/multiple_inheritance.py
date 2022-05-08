class Employee:
    company="visa"
    ecode=120
class Freelancer:
    company="fiver"
    level=0

    def upgradeLevel(self):
        self.level=self.level +1


class Programmer(Employee, Freelancer):
    name="Rohit"    

p=Programmer()
print(p.name)
print(p.level)
print(p.ecode)

# There are ambiguity 
#this will give output 'visa' becaluse we put Programmer(Employee, Freelancer)
#if we put Programmer( Freelancer, Employee) it will give 'fiver
print(p.company)

p.upgradeLevel()
print(p.level)
