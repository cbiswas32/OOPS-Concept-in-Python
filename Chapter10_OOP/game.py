from os import remove


class Remote:
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass

    def moveTop(self):
        pass

r=Remote()
p=Player()


if(r.isLeftPressed()):
    p.moveLeft()