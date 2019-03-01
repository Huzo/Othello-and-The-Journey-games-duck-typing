from Pos import Pos

HEALTH_CAP = 10

class Warrior():
    def __init__(self, posx, posy, index, mapp):
        self._pos = Pos(posx, posy)
        self._index = index
        self._map = mapp
        self._name = ("W%s" % str(index))
        self._health = HEALTH_CAP
        self._magic_crystal = 10

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
            self._map.setLand(self._pos, None)
            self._pos.setPos(posx, posy)
            self._map.setLand(self._pos, self)

        if self.health <= 0:
            print("Very sorry, %s has been killed." % self.name)
            self._map.setLand(self.pos, None)
            self._map.deleteTeleportableObj(self)
            self._map.decreaseNumOfWarriors()

    def talk(self, content):
        print("%s: %s" % (self._name, content))

    def increaseCrystal(self, value):
        self._magic_crystal = self._magic_crystal + value

    def decreaseCrystal(self, value):
        self._magic_crystal = self._magic_crystal - value

    def increaseHealth(self, value):
        self._health = self._health + value
        if self._health > HEALTH_CAP:
            self._health = HEALTH_CAP

    def decreaseHealth(self, value):
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
