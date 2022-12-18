from player import Player 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 

    def chosen_gesture(self):
        self.chosen_gesture = input("Please chose your hand: ")
        if user_choice == "0":
            user_choice = "Rock"
        if user_choice == "1":
            user_choice = "Paper"
        if user_choice == "2":
            user_choice = "Scissors"
        if user_choice == "3":
            user_choice = "Lizard"
        if user_choice == "4":
            user_choice = "Spock"



