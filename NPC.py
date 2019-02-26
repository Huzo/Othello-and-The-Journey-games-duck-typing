from Pos import Pos

class NPC():
    def __init__(self, posx, posy, index, mapp):
        self.mapp = mapp
        self.pos = Pos(posx, posy)
        self.index = index
        self.name = None
        self.power = None

    def talk(self, content):
        print("%s: %s" % (self.name, content))

    def actionOnWarrior(self, warrior):
        return False
