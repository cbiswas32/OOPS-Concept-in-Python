def readFile(filename):
        try:
             with open(filename) as f:
                print(f.read())
        except Exception as e:
            print(f'{filename} is not Found')        

   


readFile('D:/assignments/python/Chapter12_Practice/1.txt')
readFile('D:/assignments/python/Chapter12_Practice/2.txt')
readFile('D:/assignments/python/Chapter12_Practice/3.txt')