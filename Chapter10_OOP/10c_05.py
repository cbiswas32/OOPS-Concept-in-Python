from tkinter import Y


class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    
    
    def bookTicket(self):
        #print(f"you want to book {no_of_ticket} no of Tickets")
        if(self.seats>0):
            print("your ticket have been booked")
            print("your ticket no is: ",self.seats)
            
            
            self.seats=self.seats-1
            return self.seats  
        else:
            print("Seats are not Available")
    def getStatus(self):
        print(f"the name of the train is {self.name}")
        print(f"Available Seats in the train are {self.seats}")
    
    
    def getFareInfo(self):
        print(f"fare is {self.fare}")

    def cancelTicket(self):
        pass


rajdhani=Train("Rajdhani Express",1000,300)

rajdhani.getStatus()
rajdhani.getFareInfo()

user=input("Do you want to Book Ticket? (Y/N): \n")
tno=int(input("How many Tickets? \n"))
l=[]
if user=="y" or "Y":
    for i in range(tno,0,-1):
        m=rajdhani.bookTicket()
        l.append(m+1)
else:
    print("Thank You!")

print(l)


