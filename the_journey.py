from Map import Map

class TheJourney:
    def __init__(self):
        self._map = Map()

    def gameStart(self):
        self._map.initializeAll()

        numOfAliveMonsters = self._map.numOfAliveMonsters
        numOfAliveWarriors = self._map.numOfAliveWarriors

        while(numOfAliveMonsters > 0 and numOfAliveWarriors > 0):
            self._map.printBoard()
            self._map.teleportAll()

            numOfAliveMonsters = self._map.numOfAliveMonsters
            numOfAliveWarriors = self._map.numOfAliveWarriors

        if numOfAliveMonsters == 0:
            print("Congratulations, all the monsters have been killed.")
        else:
            print("Unfortunately, the mission failed and all the warriors died.")

if __name__ == "__main__":
    game = TheJourney()
    game.gameStart()
