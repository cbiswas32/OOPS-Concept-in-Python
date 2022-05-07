# DRY - Donot Repeat yourself

# This principal works in both function and OOPs Concept


# Procedural Language
# a=10
# b=34
# print("this sum of a and b is ", a+b)


# Object Oriented Programming Concept

# Class is Blue Print or Template
# Class doesnot consume Memory
# Class is written on PascalCase
'''
Class contains variable and Method

'''


'''
Object is a instanciation of class
Object is written in camelCase

Memory allocation is done only after object instanciation

Abstraction

Encapsulation


'''

class Number:
    def sum(self):
        return self.a + self.b
num = Number()
num.a=12
num.b=34
s=num.sum()
print(s)

