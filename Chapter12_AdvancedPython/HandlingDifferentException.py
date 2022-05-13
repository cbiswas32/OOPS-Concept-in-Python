while(True):
    
    try:
        print("Enter 9999 for exit")
        a=int(input("Enter a Number "))
        if a==9999:
            break
        c=1/a
        print(c)
    except ValueError as e:
        print("Please enter a valid number")    
    except ZeroDivisionError as e:
        print("Please Enter NonZero")       
    except Exception as e:
        print(e)
    # We can handle different exception differently      
print("Thanks for using the code ")        