import random
from Pos import Pos

HEALTH_CAP = 40

class Warrior():
    def __init__(self, posx, posy, index, mapp):
        self._pos = Pos(posx, posy)
        self._index = index
        self._map = mapp
        self._name = ("W%s" % str(index))
        self._health = HEALTH_CAP
        self._magic_crystal = 10

    def action_on_warrior(self, warrior):
        self.talk("Hi, bro. You can call me %s. I am very happy to meet you. I have %s magic crystals." % (self.name, int(self._magic_crystal)))
        self.talk("The number of your magic crystals is %s." % int(warrior.magic_crystal))
        self.talk("Need I share with you some magic crystals?")
        self.talk("You now have following options: ")
        print("1. Yes")
        print("2. No")
        a = int(input())
        if(a == 1):
            value = random.randint(1, self._magic_crystal)
            self.decrease_crystal(value)
            warrior.increase_crystal(value)
            warrior.talk("Thanks for your shared %s crystals! %s." % (int(value), self.name))
        return False

    def teleport(self):
        print(("Hi, %s. Your position is (%s,%s) and health is %s." % (self._name, self._pos.x, self._pos.y, self._health)))
        print("Specify your target position (Input 'x y').")
        inp = input()
        inp = inp.split(' ')
        posx = int(inp[0])
        posy = int(inp[1])
        while(posx == self._pos.x and posy == self._pos.y):
            print("Specify your target position (Input 'x y'). It should not be the same as the original one.")
            inp = input()
            inp = inp.split(' ')
            posx = int(inp[0])
            posy = int(inp[1])
        result = self._map.coming(posx, posy, self)
        if result:
            self._map.set_land(self._pos, None)
            self._pos.set_pos(posx, posy)
            self._map.set_land(self._pos, self)
            self._map.print_board()

        if self.health <= 0:
            print("Very sorry, %s has been killed." % self.name)
            self._map.set_land(self.pos, None)
            self._map.delete_teleportable_obj(self)
            self._map.decrease_num_of_warriors()

    def talk(self, content):
        print("%s: %s" % (self._name, content))

    def increase_crystal(self, value):
        self._magic_crystal = self._magic_crystal + value

    def decrease_crystal(self, value):
        self._magic_crystal = self._magic_crystal - value

    def increase_health(self, value):
        self._health = self._health + value
        if self._health > HEALTH_CAP:
            self._health = HEALTH_CAP

    def decrease_health(self, value):
        self._health = self._health - value

    @property
    def pos(self):
        return self._pos

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def magic_crystal(self):
        return self._magic_crystal

    @magic_crystal.setter
    def magic_crystal(self, magic_crystal):
        self._magic_crystal = magic_crystal
