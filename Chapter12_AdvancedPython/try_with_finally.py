try:
    i=int(input("Enter a number "))
    print(1/i)
except Exception as e:
    print(e)
    exit()


# Finally Always executes in a program

finally:
    print("We are done ")

print("Thanks for using the program")