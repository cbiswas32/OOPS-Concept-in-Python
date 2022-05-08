class Complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i

    def __add__(self,c):
        return Complex(self.real +c.real, self.img + c.img)
    
    def __mul__(self,c):
        mulReal= self.real*c.real - self.img*c.img
        mulImg= self.real*c.img + self.img*c.real

        return Complex(mulReal,mulImg)

    def __str__(self):
        return f"{self.real} + {self.img}i"

c1=Complex(3,2)
c2=Complex(1,7)

print(c1+c2)
print(c1*c2)