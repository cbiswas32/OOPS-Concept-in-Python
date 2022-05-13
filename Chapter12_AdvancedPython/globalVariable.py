


from traceback import print_tb


a=54 #Global variable

def func1():
    global a
    print(a)
    a=100 # vchanges the global variable
    print(a)
func1()    
print(a)