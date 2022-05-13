# Using enumerate function we have to print 3rd Fifth and Seventh element

list=[100,200,300,400,500,600,700,800] 
for index, val in enumerate(list):
    if index==2 or index==4 or index==6:
        print(val,index)