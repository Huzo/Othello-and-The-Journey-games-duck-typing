from Map import Map

class TheJourney:
    def __init__(self):
        self.mapp = Map()

    def gameStart(self):
        self.mapp.initializeAll()

        numOfAliveMonsters = self.mapp.numOfAliveMonsters
        numOfAliveWarriors = self.mapp.numOfAliveWarriors

        while(numOfAliveMonsters > 0 and numOfAliveWarriors > 0):
            self.mapp.printBoard()
            self.mapp.teleportAll()

            numOfAliveMonsters = self.mapp.numOfAliveMonsters
            numOfAliveWarriors = self.mapp.numOfAliveWarriors

        if numOfAliveMonsters == 0:
            print("Congratulations, all the monsters have been killed.")
        else:
            print("Unfortunately, the mission failed and all the warriors died.")

if __name__ == "__main__":
    game = TheJourney()
    game.gameStart()
