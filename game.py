#Use sleep method to slow down game play---? 

import time 
from human import Human 
from ai import AI


class Game:
    def __init__(self) -> None:
        self.player_one = Human("Michaela")
        self.player_two = AI("Rumba")
        pass

    def run_game(self):
        print("game setup tested ok")


