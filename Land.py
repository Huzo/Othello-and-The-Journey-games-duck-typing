from NPC import NPC

class Land():
    def __init__(self):
        self._occupied_obj = None

    def coming(self, warrior):
        if(self._occupied_obj != None):
            return self._occupied_obj.action_on_warrior(warrior)
        return True

    @property
    def occupied_obj(self):
        return self._occupied_obj

    @occupied_obj.setter
    def occupied_obj(self, occupied_obj):
        self._occupied_obj = occupied_obj

    def get_occupant_name(self):
        if(self._occupied_obj != None):
            return self._occupied_obj.name