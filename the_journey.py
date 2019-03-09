from Map import Map

class TheJourney:
    def __init__(self):
        self._map = Map()

    def game_start(self):
        self._map.initialize_all()

        num_of_alive_monsters = self._map.num_of_alive_monsters
        num_of_alive_warriors = self._map.num_of_alive_warriors

        while(num_of_alive_monsters > 0 and num_of_alive_warriors > 0):
            self._map.print_board()
            self._map.teleport_all()

            num_of_alive_monsters = self._map.num_of_alive_monsters
            num_of_alive_warriors = self._map.num_of_alive_warriors

        if num_of_alive_monsters == 0:
            print("Congratulations, all the monsters have been killed.")
        else:
            print("Unfortunately, the mission failed and all the warriors died.")

if __name__ == "__main__":
    game = TheJourney()
    game.game_start()
