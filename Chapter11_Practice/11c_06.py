class Vec:
    def __init__(self,list):
        self.list=list

    def __str__(self):
        return f"{self.list[0]}i + {self.list[1]}j + {self.list[2]}k"

v= Vec([200,5,23])
print(v)