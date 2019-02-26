from NPC import NPC

class Land():
    def __init__(self):
        self.occupied_obj = None

    def coming(self, warrior):
        if(self.occupied_obj != None):
            return self.occupied_obj.actionOnWarrior(warrior)

    def getOccupantName(self):
        if(self.occupied_obj != None):
            return self.occupied_obj.name
