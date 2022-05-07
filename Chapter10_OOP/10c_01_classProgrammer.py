class Programmer:
    company = 'Microsoft'

    #building a Constractor
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def get(self):
        print('name',self.name)
        print('product ',self.product)
        print('company ',self.company)
        

        print()

chinmoy=Programmer("Chinmoy","Skype")
alka=Programmer("Alka","Git")
harry=Programmer("Harry","Skype")

chinmoy.get()
alka.get()
harry.get()