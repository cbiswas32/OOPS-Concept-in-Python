class Vector:
    def __init__(self,list):
        self.list=list
    
    def __add__(self,vec2):
        if len(self.list) != len(vec2.list):
            return "Sorry Length is not Same"
        else:
             newList=[]
             for i in range(len(self.list)):
                newList.append(self.list[i] +vec2.list[i])
             return Vector(newList)

    def __mul__(self,vec2):
        if len(self.list) != len(vec2.list):
            return "Sorry Length is not Same"
        else:
            sum=0
            for i in range(len(self.list)):
                sum=sum+ self.list[i]*vec2.list[i]
            return sum

    def __str__(self):
        str1=""
        index=0
        for i in self.list:
            str1 = str1 + f" {i}a{index} +"
            index=index+1
        return str1[:-1]




v1=Vector([1,4,5,8])
v2=Vector([5,6,8,2,3])
 
print(v1+v2)

print(v1*v2)