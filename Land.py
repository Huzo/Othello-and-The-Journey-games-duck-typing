from NPC import NPC

class Land():
    def __init__(self):
        self._occupied_obj = None

    def coming(self, warrior):
        if(self._occupied_obj != None):
            return self._occupied_obj.actionOnWarrior(warrior)
        return True

    @property
    def occupied_obj(self):
        return self._occupied_obj

    @occupied_obj.setter
    def occupied_obj(self, occupied_obj):
        self._occupied_obj = occupied_obj

    def getOccupantName(self):
        if(self._occupied_obj != None):
            return self._occupied_obj.name
