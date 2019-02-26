import random
from Pos import Pos

HEALTH_CAP = 10

class Warrior():
    def __init__(self, posx, posy, index, mapp):
        self.pos = Pos(posx, posy)
        self.index = index
        self.mapp = mapp
        self.name = ("W%s" % str(index))
        self.health = HEALTH_CAP
        self.magic_crystal = 10

    def teleport(self):
        print(("Hi, %s. Your position is (%s,%s) and health is %s." % (self.name, self.pos.x, self.pos.y, self.health)))
        print("Specify your target position (Input 'x y').")
        inp = input()
        inp = inp.split(' ')
        posx = int(inp[0])
        posy = int(inp[1])
        while(posx == self.pos.x and posy == self.pos.y):
            print("Specify your target position (Input 'x y'). It should not be the same as the original one.")
            posx = int(input())
            posy = int(input())
        result = self.mapp.coming(posx, posy, self)
        if result:
            self.mapp.setLand(self.pos, None)
            self.pos.x = posx
            self.pos.y = posy
            self.mapp.setLand(self.pos, self)
        if self.health <= 0:
            print("Very sorry, %s has been killed." % self.name)
            self.mapp.setLand(self.pos, None)
            self.mapp.deleteTeleportableObj(self)
            self.mapp.decreaseNumOfWarriors()

    def talk(self, content):
        print("%s: %s" % (self.name, content))

    def increaseCrystal(self, value):
        self.magic_crystal = self.magic_crystal + value

    def decreaseCrystal(self, value):
        self.magic_crystal = self.magic_crystal - value

    def increaseHealth(self, value):
        self.health = self.health + value
        if self.health > HEALTH_CAP:
            self.health = HEALTH_CAP

    def decreaseHealth(self, value):
        self.health = self.health - value
