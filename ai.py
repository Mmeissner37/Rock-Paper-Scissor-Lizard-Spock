from player import Player
import random 


class AI(Player): 
    def __init__(self, name) -> None:
        super().__init__(name) 
        self.win = 0

    
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'{self.name} has picked {self.chosen_gesture}')


