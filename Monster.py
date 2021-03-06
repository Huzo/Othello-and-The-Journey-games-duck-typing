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

DAMAGE_CAP = 20

class Monster(NPC):
    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self._name = "M%s" % str(index)
        self._power = random.randint(5, DAMAGE_CAP - 1)

    def action_on_warrior(self, warrior):
        self.talk(("I am the monster %s. Here is my territory.  My damage power is %s." % (self._name, self._power)));
        self.talk(("Your health is %s." % warrior.health));
        self.talk("Do you really want to challenge me?");
        self.talk("You now have following options: ");

        print("1. Yes")
        print("2. No")
        a = int(input())

        if(a == 1):
            if(warrior.health > self._power):
                warrior.decrease_health(self._power)
                warrior.increase_crystal(random.randint(5, 9))
                warrior.talk(("Nice, I have killed the monster %s." % self._name))
                self._map.decrease_num_of_alive_monsters()
                return True
            warrior.decrease_health(self.power)
        return False
