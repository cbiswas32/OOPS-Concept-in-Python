from functools import reduce


import functools
hi=lambda a,b: a+b
l=[1,2,3,4,5, ]
print(functools.reduce(hi,l))