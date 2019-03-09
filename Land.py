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