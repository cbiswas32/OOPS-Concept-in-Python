class Sample:
    a = "Harry"

obj=Sample()
obj.a="Vicky"   


#It does not change Class attribute 
#It just add an instance attribute
#To change Class Attribute we have to use Samole.a="Vicky"


print(Sample.a)
print(obj.a)