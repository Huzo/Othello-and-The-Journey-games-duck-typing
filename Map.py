from Land import Land
from Pos import Pos
from Elf import Elf
from Warrior import Warrior
from Monster import Monster
import random

D = 10
totalNum = 0
teleportable_obj = []

class Map():
    def __init__(self):
        self.lands = [[None for i in range(D)] for j in range(D)]
        e = random.randint(1, 3)
        m = random.randint(1, 3)
        w = 1
        totalNum = m + e + w
        self.numOfAliveMonsters = m
        self.numOfAliveWarriors = w

    def initializeAll(self):
        print("Welcome to Kafustrok. Light blesses you. ")
        global D, totalNum, teleportable_obj

        for i in range(D):
            for j in range(D):
                self.lands[i][j] = Land()

        for i in range(totalNum):
            pos = getUnOccupiedPosition()
            if(i < m):
                self.lands[pos.x][pos.y].setOccupied_obj(Monster(pos.x, pos.y, i, self))
            elif(i < m+e):
                self.lands[pos.x][pos.y].setOccupied_obj(Elf(pos.x, pos.y, i-m, self))
            else:
                self.lands[pos.x][pos.y].setOccupied_obj(Warrior(pos.x, pos.y, i-m-e, self))
                teleportable_obj.append(self.lands[pos.x][pos.x].occupied_obj)

    def teleportAll(self):
        global teleportable_obj

        for obj in teleportable_obj:
            if isinstance(obj, Warrior):
                obj.teleport()

    def coming(self, posx, posy, warrior):
        return self.lands[posx][posy].coming(warrior)

    def setLand(self, _pos, occupied_obj):
        self.lands[_pos.x][_pos.y].occupied_obj = occupied_obj

    def deleteTeleportableObj(self, obj):
        global teleportable_obj

        index = teleportable_obj.index(obj)
        teleportable_obj[index] = None

    def getUnOccupiedPosition(self):
        randx = random.randint(-1, D - 1)
        randy = random.randint(-1, D - 1)
        while(self.lands[randx][randy].occupied_obj != None):
            randx = random.randint(-1, D - 1)
            randy = random.randint(-1, D - 1)
        return Pos(randx, randy)

    def printBoard(self):
        printObject = [[None for i in range(D)] for j in range(D)]

        for i in range(D):
            for j in range(D):
                occupantName = self.lands[i][j].getOccupantName()
                if occupantName == None:
                    occupantName = " "
                printObject[i][j] = occupantName

            print(" ")
            for i in range(D):
                print(("| %s " % str(i)),end="")

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
        self.numOfAliveMonsters = self.numOfAliveMonsters - 1

    def decreaseNumOfWarriors(self):
        self.numOfAliveWarriors = self.numOfAliveWarriors - 1
