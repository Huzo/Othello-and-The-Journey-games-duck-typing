# CSCI3180 Principles of Programming Languages
 #
 # --- Declaration ---
 #
 # I declare that the assignment here submitted is original except for source
 # material explicitly acknowledged. I also acknowledge that I am aware of
 # University policy and regulations on honesty in academic work, and of the
 # disciplinary guidelines and procedures applicable to breaches of such policy
 # and regulations, as contained in the website
 # http://www.cuhk.edu.hk/policy/academichonesty/
 #
 # Assignment 2
 # Name : Huzeyfe Kiran
 # Student ID : 1155104019
 # Email Addr : 1155104019@link.cuhk.edu.hk
import random
from NPC import NPC

AMOUNT_CAP = 10

class Potion(NPC):
    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self._name = "P%s" % str(index)
        self._amount = random.randint(5, AMOUNT_CAP - 1)

    def action_on_warrior(self, warrior):
        warrior.increase_health(self._amount)
        warrior.talk(("Very good, I got additional healing potion %s." % self.name))
        warrior._map.set_land(warrior._pos, None)
        warrior._pos.set_pos(self.pos.x, self.pos.y)
        warrior._map.set_land(warrior.pos, warrior)
        self._pos.set_pos(None, None)

        self._map.delete_teleportable_obj(self)

        return False

    def teleport(self):
        posx = random.randint(0,9)
        posy = random.randint(0,9)

        while(self._map._lands[posx][posy].occupied_obj != None):
            posx = random.randint(0,9)
            posy = random.randint(0,9)

        self._map.set_land(self._pos, None)
        self._pos.set_pos(posx, posy)
        self._map.set_land(self._pos, self)

