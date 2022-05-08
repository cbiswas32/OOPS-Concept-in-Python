class Animal:
    animalType="Mamal"

class Pet(Animal):
    color="white"

class Dog(Pet):
    @staticmethod
    def bark():
        print("Bow bow!")

# Multilevel Inheritance
d=Dog()
d.bark()

print(d.color)
print(d.animalType)
