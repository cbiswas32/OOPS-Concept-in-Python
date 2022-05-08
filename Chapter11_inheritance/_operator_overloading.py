#dunderMethod


class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num


n1=Number(3)
n2=Number(4)
print(n1+n2)