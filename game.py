#Use sleep method to slow down game play---? 

import time 
from human import Human 
from ai import AI


class Game:
    def __init__(self) -> None:
        self.player_one = None   #None is a placeholder that I override in choose_game_mode 
        self.player_two = None 
        pass

    def run_game(self):
        self.display_rules()
        self.choose_game_mode()
        self.play_hands()
        self.determine_winner()
        self.show_win()

    def display_rules(self):
        print("Here are the Rules of the Game:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print('Rock crushes Lizard')
        print('Lizard poisons Spock') 
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock') 
        print('Spock vaporizes Rock')


    def choose_game_mode(self):
        user_choice = input('Welcome to the game! Please press 1 for single player and 2 for multi-player: ')
        if user_choice == "1":
            player_one_name = input("Please enter Player One name: ")
            self.player_one = Human(player_one_name)
            self.player_two = AI("Rumba")
        if user_choice == "2":
            player_one_name = input("Please enter Player One name: ")
            self.player_one = Human(player_one_name)
            player_two_name = input("Please enter Player Two name: ")
            self.player_two = Human(player_two_name)

    def play_hands(self): 
        self.player_one.chosen_gesture()
        self.player_two.chosen_gesture()

    #def determine_winner(self):
        


    # def show_win(self):
    #     self.player_one.win = 


