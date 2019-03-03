import random
from NPC import NPC

AMOUNT_CAP = 10

class Potion(NPC):
    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self._name = "P%s" % str(index)
        self._amount = random.randint(5, AMOUNT_CAP - 1)

    def actionOnWarrior(self, warrior):
        warrior.increaseHealth(self._amount)
        warrior.talk(("Very good, I got additional healing potion %s." % self.name))
        warrior._map.setLand(warrior._pos, None)
        warrior._pos.setPos(self.pos.x, self.pos.y)
        warrior._map.setLand(warrior.pos, warrior)
        self._pos.setPos(None, None)

        self._map.deleteTeleportableObj(self)

        return False

    def teleport(self):
        posx = random.randint(0,9)
        posy = random.randint(0,9)

        while(self._map._lands[posx][posy].occupied_obj != None):
            posx = random.randint(0,9)
            posy = random.randint(0,9)

        self._map.setLand(self._pos, None)
        self._pos.setPos(posx, posy)
        self._map.setLand(self._pos, self)

