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
from Land import Land
from Pos import Pos
from Elf import Elf
from Warrior import Warrior
from Monster import Monster
from Potion import Potion
import random

D = 10
teleportable_obj = []
e = random.randint(2, 4)
m = random.randint(2, 4)
p = random.randint(2, 4)
w = random.randint(2, 4)

class Map():

    def __init__(self):
        self._lands = [[Land() for i in range(D)] for j in range(D)]
        self.totalNum = m + e + p + w
        self._num_of_alive_monsters = m
        self._num_of_alive_warriors = w

    def initialize_all(self):
        print("Welcome to Kafustrok. Light blesses you. ")
        global teleportable_obj

        for i in range(self.totalNum):
            pos = self.get_unoccupied_position()
            if(i < m):
                self._lands[pos.x][pos.y].occupied_obj = Monster(pos.x, pos.y, i, self)
            elif(i < m+e):
                self._lands[pos.x][pos.y].occupied_obj = Elf(pos.x, pos.y, i-m, self)
            elif(i < m+e+w):
                self._lands[pos.x][pos.y].occupied_obj = Warrior(pos.x, pos.y, i-m-e, self)
                teleportable_obj.append(self._lands[pos.x][pos.y].occupied_obj)
            else:
                self._lands[pos.x][pos.y].occupied_obj = Potion(pos.x, pos.y, i-m-e-w, self)
                teleportable_obj.append(self._lands[pos.x][pos.y].occupied_obj)

    def teleport_all(self):
        global teleportable_obj

        for i in range(len(teleportable_obj)):
            if(teleportable_obj[i] != None):
                teleportable_obj[i].teleport()

    def coming(self, posx, posy, warrior):
        return self._lands[posx][posy].coming(warrior)

    def set_land(self, pos, occupied_obj):
        self._lands[pos.x][pos.y].occupied_obj = occupied_obj

    def delete_teleportable_obj(self, obj):
        global teleportable_obj

        index = teleportable_obj.index(obj)
        teleportable_obj[index] = None

    def get_unoccupied_position(self):
        randx = random.randint(0, D - 1)
        randy = random.randint(0, D - 1)
        while(self._lands[randx][randy].occupied_obj != None):
            randx = random.randint(0, D - 1)
            randy = random.randint(0, D - 1)
        return Pos(randx, randy)

    def print_board(self):
        printObject = [[None for i in range(D)] for j in range(D)]

        for i in range(D):
            for j in range(D):
                occupantName = self._lands[i][j].get_occupant_name()
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

    def decrease_num_of_alive_monsters(self):
        self._num_of_alive_monsters = self._num_of_alive_monsters - 1

    def decrease_num_of_warriors(self):
        self._num_of_alive_warriors = self._num_of_alive_warriors - 1

    @property
    def num_of_alive_monsters(self):
        return self._num_of_alive_monsters

    @num_of_alive_monsters.setter
    def num_of_alive_monsters(self, num_of_alive_monsters):
        self._num_of_alive_monsters = num_of_alive_monsters

    @property
    def num_of_alive_warriors(self):
        return self._num_of_alive_warriors

    @num_of_alive_warriors.setter
    def num_of_alive_warriors(self, num_of_alive_warriors):
        self._num_of_alive_warriors = num_of_alive_warriors
