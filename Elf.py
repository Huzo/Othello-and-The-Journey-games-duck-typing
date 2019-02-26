import random
from NPC import NPC

class Elf(NPC):

    MAGIC_CAP = 20

    def __init__(self, posx, posy, index, mapp):
        super().__init__(posx, posy, index, mapp)
        self.name = "E%s" % str(index)
        self.power = random.randint(4, self.MAGIC_CAP - 1)

    def actionOnWarrior(warrior):
        self.talk(("My name is %s. Welcome tomy home.  My magic power is %s." % (self.name, str(self.power))))
        self.talk(("Your magic crystal is %s." % warrior.magic_crystal))
        self.talk("Do you need my help?")
        self.talk("You now have following options: ")
        print("1. Yes")
        print("2. No")
        a = int(input())
        if(a == 1):
            value = random.randint(1, self.power - 1)
            if(warrior.magic_crystal > value):
                warrior.decreaseCrystal(value)
                warrior.increaseHealth(value)
                warrior.talk(("Thanks for your help! %s" % self.name))
            else:
                warrior.talk("Very embarrassing, I don't have enough crystals.")
            return False

