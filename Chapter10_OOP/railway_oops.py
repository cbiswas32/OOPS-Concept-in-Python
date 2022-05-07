class RailwayForm:
    formtype="RailwayForm"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

app = RailwayForm()
app.name="Chinmoy"
app.train="Rajdhani Express"
app.printData()  