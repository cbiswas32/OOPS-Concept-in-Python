class Dadu():
    def __init__(self):
        print("initializing Dadu")

    def getName(self):
        print("Dadu")
        

class Baba(Dadu):

    def __init__(self):
        
        print("initializing Baba")
        super().__init__( )

    
    
    def getName(self):
        print("Baba")
        super().getName()


class Chele(Baba):

    def __init__(self):
        
        print("initializing Chele")
        super().__init__()

    def getName(self):
        print("Chele")
        #   super keyword
        super().getName()


ami=Chele()
