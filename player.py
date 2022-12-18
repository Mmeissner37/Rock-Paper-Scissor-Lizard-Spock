import random 


class Player: 
    def __init__(self, name) -> None:
        self.name = name
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.win = 0
        self.chosen_gesture = "You have chosen: "
        pass

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
        print("You have chosen: ")


