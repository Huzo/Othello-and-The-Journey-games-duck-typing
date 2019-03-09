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

class Elf(NPC):

    MAGIC_CAP = 20

    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self._name = "E%s" % str(index)
        self._power = random.randint(5, self.MAGIC_CAP - 1)

    def action_on_warrior(self, warrior):
        self.talk(("My name is %s. Welcome tomy home.  My magic power is %s." % (self._name, str(self._power))))
        self.talk(("Your magic crystal is %s." % warrior.magic_crystal))
        self.talk("Do you need my help?")
        self.talk("You now have following options: ")
        print("1. Yes")
        print("2. No")
        a = int(input())
        if(a == 1):
            value = random.randint(1, self._power - 1)
            if(warrior.magic_crystal > value):
                warrior.decrease_crystal(value)
                warrior.increase_health(value)
                warrior.talk(("Thanks for your help! %s" % self.name))
            else:
                warrior.talk("Very embarrassing, I don't have enough crystals.")
        return False


