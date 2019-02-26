from NPC import NPC

class Land():
    def __init__(self):
        self.occupied_obj = None

    def coming(self, warrior):
        return actionOnWarrior(warrior)

    def getOccupantName(self):
        if(isinstance(self.occupied_obj, NPC)):
            return self.occupied_obj.name
