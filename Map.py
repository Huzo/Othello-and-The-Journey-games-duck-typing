from Land import Land
from Pos import Pos
from Elf import Elf
from Warrior import Warrior
from Monster import Monster
import random

D = 10
teleportable_obj = []
e = random.randint(2, 4)
m = random.randint(2, 4)
w = 1

class Map():

    def __init__(self):
        self._lands = [[Land() for i in range(D)] for j in range(D)]
        self.totalNum = m + e + w
        self._numOfAliveMonsters = m
        self._numOfAliveWarriors = w

    def initializeAll(self):
        print("Welcome to Kafustrok. Light blesses you. ")
        global teleportable_obj

        for i in range(self.totalNum):
            pos = self.getUnOccupiedPosition()
            if(i < m):
                self._lands[pos.x][pos.y].occupied_obj = Monster(pos.x, pos.y, i, self)
            elif(i < m+e):
                self._lands[pos.x][pos.y].occupied_obj = Elf(pos.x, pos.y, i-m, self)
            else:
                self._lands[pos.x][pos.y].occupied_obj = Warrior(pos.x, pos.y, i-m-e, self)
                teleportable_obj.append(self._lands[pos.x][pos.y].occupied_obj)

    def teleportAll(self):
        global teleportable_obj

        for i in range(len(teleportable_obj)):
            if(teleportable_obj[i] != None):
                teleportable_obj[i].teleport()

    def coming(self, posx, posy, warrior):
        return self._lands[posx][posy].coming(warrior)

    def setLand(self, pos, occupied_obj):
        self._lands[pos.x][pos.y].occupied_obj = occupied_obj

    def deleteTeleportableObj(self, obj):
        global teleportable_obj

        index = teleportable_obj.index(obj)
        teleportable_obj[index] = None

    def getUnOccupiedPosition(self):
        randx = random.randint(0, D - 1)
        randy = random.randint(0, D - 1)
        while(self._lands[randx][randy].occupied_obj != None):
            randx = random.randint(0, D - 1)
            randy = random.randint(0, D - 1)
        return Pos(randx, randy)

    def printBoard(self):
        printObject = [[None for i in range(D)] for j in range(D)]

        for i in range(D):
            for j in range(D):
                occupantName = self._lands[i][j].getOccupantName()
                if occupantName == None:
                    occupantName = "  "
                printObject[i][j] = occupantName

        print(" ",end="")
        for i in range(D):
            print(("| %s  " % str(i)),end="")

        print("|")

        for i in range(int(D * 5.5)):
            print("-",end="")
        print("")

        for row in range(D):
            print(row,end="")
            for col in range(D):
                print(("| %s " % printObject[row][col]), end="")
            print("|")
            for i in range(int(D * 5.5)):
                print("-",end="")
            print("")

    def decreaseNumOfAliveMonsters(self):
        self._numOfAliveMonsters = self._numOfAliveMonsters - 1

    def decreaseNumOfWarriors(self):
        self._numOfAliveWarriors = self._numOfAliveWarriors - 1

    @property
    def numOfAliveMonsters(self):
        return self._numOfAliveMonsters

    @numOfAliveMonsters.setter
    def numOfAliveMonsters(self, numOfAliveMonsters):
        self._numOfAliveMonsters = numOfAliveMonsters

    @property
    def numOfAliveWarriors(self):
        return self._numOfAliveWarriors

    @numOfAliveWarriors.setter
    def numOfAliveWarriors(self, numOfAliveWarriors):
        self._numOfAliveWarriors = numOfAliveWarriors
