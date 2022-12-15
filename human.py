from player import Player 


class Human(Player):
    def __init__(self, gesture) -> None:
        super().__init__(gesture) 

player_one = Human(Player)
player_one.gesture = user_input("")



