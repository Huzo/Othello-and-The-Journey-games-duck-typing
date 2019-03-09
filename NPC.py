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
from Pos import Pos

class NPC():
    def __init__(self, posx, posy, index, mapp):
        self._map = mapp
        self._pos = Pos(posx, posy)
        self._index = index
        self._name = None
        self._power = None

    def talk(self, content):
        print("%s: %s" % (self._name, content))

    def action_on_warrior(self, warrior):
        return False

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power
