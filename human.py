from player import Player 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 

    def choose_gesture(self):
        self.chosen_gesture = input("Please chose your hand: ")
        if input == "0":
            self.chosen_gesture = "Rock"
        if input == "1":
            self.chosen_gesture = "Paper"
        if input == "2":
            self.chosen_gesture = "Scissors"
        if input == "3":
            self.chosen_gesture = "Lizard"
        if input == "4":
            self.chosen_gesture = "Spock"




