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
            self.choose_gesture = "Rock"
        if self.chosen_gesture == "1":
            print(f'{self.name} chose Paper')
            self.choose_gesture = "Paper"
        if self.chosen_gesture == "2":
            print(f'{self.name} chose Scissors')
            self.choose_gesture = "Scissors"
        if self.chosen_gesture == "3":
            print(f'{self.name} chose Lizard')
            self.choose_gesture = "Lizard"
        if self.chosen_gesture == "4":
            print(f'{self.name} chose Spock')
            self.choose_gesture = "Spock"
        elif self.chosen_gesture == "":
            print('Please chose between 0 and 4')
            self.choose_gesture = input()

            



    # def choose_gesture(self):
    #     self.chosen_gesture = random.choice(self.gestures)
    #     print(f'{self.name} has picked {self.chosen_gesture}')



