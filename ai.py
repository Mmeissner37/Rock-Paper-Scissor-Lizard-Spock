from player import Player
import random 
from time import sleep 


class AI(Player): 
    def __init__(self, name) -> None:
        super().__init__(name) 
        self.win = 0

    
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        sleep(1)
        print(f'{self.name} has picked {self.chosen_gesture}')


