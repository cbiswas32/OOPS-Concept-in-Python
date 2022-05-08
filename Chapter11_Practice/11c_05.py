class Vector:
    def __init__(self, i, j):
        self.i=i
        self.j=j
    def getVector(self):
        if self.j<0:
            print(f"{self.i}i - {-self.j}j")
        else:
             print(f"{self.i}i + {self.j}j")
    def __add__(obj1,obj2):
        return Vector(obj1.i + obj2.i, obj1.j + obj2.j)

    def __str__(self):
        if self.j<0:
            return f"{self.i}i - {-self.j}j"
        else:
             return f"{self.i}i + {self.j}j"        


v1=Vector(2,-3)
v2=Vector(5,10)
v3=v1 + v2

v1.getVector()
v2.getVector()

v3.getVector()
print(v3)
