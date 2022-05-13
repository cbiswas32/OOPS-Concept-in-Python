num=int(input("Enter a number: "))


ans=[i*num  for i in range(1,11) ]
ans = str(ans)
with open('D:/assignments/python/Chapter12_Practice/multable.txt','a') as f:
    f.write(ans)
    f.write("\n")
    