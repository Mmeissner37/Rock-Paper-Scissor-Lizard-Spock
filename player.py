import random 
from time import sleep 


class Player: 
    def __init__(self, name) -> None:
        self.name = name
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.win = 0
        self.chosen_gesture = ""
        pass

    def choose_gesture(self):
        pass

    def gestures(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


