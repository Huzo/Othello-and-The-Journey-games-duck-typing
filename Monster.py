import random
from NPC import NPC

DAMAGE_CAP = 20

class Monster(NPC):
    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self.name = "M%s" % str(index)
        self.power = random.randint(4, DAMAGE_CAP - 1)

    def actionOnWarrior(self, warrior):
        self.talk(("I am the monster %s. Here is my territory.  My damage power is %s." % (self.name, self.power)));
        self.talk(("Your health is %s." % warrior.health));
        self.talk("Do you really want to challenge me?");
        self.talk("You now have following options: ");

        print("1. Yes")
        print("2. No")
        a = int(input())

        if(a == 1):
            if(warrior.health > self.power):
                warrior.decreaseHealth(self.power)
                warrior.increaseCrystal(random.randint(-1, 4))
                warrior.talk(("Nice, I have killed the monster %s." % self.name))
                self.mapp.decreaseNumOfAliveMonsters()
                return True
            warrior.decreaseHealth(self.power)
        return False
