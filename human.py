from player import Player 
from time import sleep 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 
        self.win = 0

    def choose_gesture(self):
        #sleep(1)
        print("Please enter your hand: ")
        self.chosen_gesture = input()
        if self.chosen_gesture == "0":
            print(f'{self.name} chose Rock')
            self.chosen_gesture = "Rock"
        if self.chosen_gesture == "1":
            print(f'{self.name} chose Paper')
            self.chosen_gesture = "Paper"
        if self.chosen_gesture == "2":
            print(f'{self.name} chose Scissors')
            self.chosen_gesture = "Scissors"
        if self.chosen_gesture == "3":
            print(f'{self.name} chose Lizard')
            self.chosen_gesture = "Lizard"
        if self.chosen_gesture == "4":
            print(f'{self.name} chose Spock')
            self.chosen_gesture = "Spock"
        elif self.chosen_gesture == ('0', '4'): 
            print('Please chose between 0 and 4')
            self.choose_gesture()

            



