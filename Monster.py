import random
from NPC import NPC

DAMAGE_CAP = 20

class Monster(NPC):
    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self._name = "M%s" % str(index)
        self._power = random.randint(5, DAMAGE_CAP - 1)

    def actionOnWarrior(self, warrior):
        self.talk(("I am the monster %s. Here is my territory.  My damage power is %s." % (self._name, self._power)));
        self.talk(("Your health is %s." % warrior.health));
        self.talk("Do you really want to challenge me?");
        self.talk("You now have following options: ");

        print("1. Yes")
        print("2. No")
        a = int(input())

        if(a == 1):
            if(warrior.health > self._power):
                warrior.decreaseHealth(self._power)
                warrior.increaseCrystal(random.randint(5, 9))
                warrior.talk(("Nice, I have killed the monster %s." % self._name))
                self._map.decreaseNumOfAliveMonsters()
                return True
            warrior.decreaseHealth(self.power)
        return False
