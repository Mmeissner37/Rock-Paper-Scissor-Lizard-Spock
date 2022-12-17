from player import Player
import random 


class AI(Player): 
    def __init__(self, name) -> None:
        super().__init__(name) 

    
    def chosen_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(self.name, "has picked", self.chosen_gesture)



print(AI.chosen_gesture)
