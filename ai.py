from player import Player
import random 


class AI(Player): 
    def __init__(self, gesture) -> None:
        super().__init__(gesture) 


player_two = AI(Player)
player_two.gesture.random.choice[0, 4]

print(player_two.gesture) 