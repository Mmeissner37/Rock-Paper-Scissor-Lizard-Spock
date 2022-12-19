#Use sleep method to slow down game play---? 

import time 
from human import Human 
from ai import AI


class Game:
    def __init__(self) -> None:
        self.player_one = None    
        self.player_two = None          #None is a placeholder that I override in choose_game_mode
        pass

    def run_game(self):
        self.display_rules()
        self.choose_game_mode()
        self.play_hands()
        self.determine_winner()
        self.show_win()
        self.play_again()

    def display_rules(self):
        print("Here are the Rules of the Game:")
        print(" ")
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
        print(" ")


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
        print("")
        print('Type 0 for Rock')
        print('Type 1 for Paper')
        print('Type 2 for Scissors')
        print('Type 3 for Lizard')
        print('Type 4 for Spock')
        print("")
        self.player_one.choose_gesture()
        # if self.player_one.choose_gesture == "0":
        #         print(f'{self.player_one.name} chose Rock')
        # if self.player_one.choose_gesture == "1":
        #     print(f'{self.player_one.name} chose Paper')
        # if self.player_one.choose_gesture == "2":
        #     print(f'{self.player_one.name} chose Scissors')
        # if self.player_one.choose_gesture == "3":
        #     print(f'{self.player_one.name} chose Lizard')
        # if self.player_one.choose_gesture == "4":
        #     print(f'{self.player_one.name} chose Spock')
        self.player_two.choose_gesture()
        # if self.player_two.choose_gesture == "0":
        #     print(f'{self.player_two.name} chose Rock')
        # if self.player_two.choose_gesture == "1":
        #     print(f'{self.player_two.name} chose Paper')
        # if self.player_two.choose_gesture == "2":
        #     print(f'{self.player_two.name} chose Scissors')
        # if self.player_two.choose_gesture == "3":
        #     print(f'{self.player_two.name} chose Lizard')
        # if self.player_two.choose_gesture == "4":
        #     print(f'{self.player_two.name} chose Spock')


    def determine_winner(self):
        if self.player_one.chosen_gesture == "0" and (self.player_two.chosen_gesture == "2" or self.player_two.chosen_gesture == "3"): 
            self.player_one.win = self.player_one.win + 1 
        elif self.player_one.chosen_gesture == "1" and (self.player_two.chosen_gesture == "0" or self.player_two.chosen_gesture == "3"):
            self.player_one.win = self.player_one.win + 1
        elif self.player_one.chosen_gesture == "2" and (self.player_two.chosen_gesture == "1" or self.player_two.chosen_gesture == "3"):
            self.player_one.win = self.player_one.win + 1
        elif self.player_one.chosen_gesture == "3" and (self.player_two.chosen_gesture == "4" or self.player_two.chosen_gesture == "1"):
            self.player_one.win = self.player_one.win + 1 
        elif self.player_one.chosen_gesture == "4" and (self.player_two.chosen_gesture == "0" or self.player_two.chosen_gesture == "2"):
            self.player_one.win = self.player_one.win + 1
        if self.player_two.chosen_gesture == "0" and (self.player_one.chosen_gesture == "2" or self.player_one.chosen_gesture == "3"): 
            self.player_two.win = self.player_two.win + 1 
        elif self.player_two.chosen_gesture == "1" and (self.player_one.chosen_gesture == "0" or self.player_one.chosen_gesture == "3"):
            self.player_one.win = self.player_two.win + 1
        elif self.player_two.chosen_gesture == "2" and (self.player_one.chosen_gesture == "1" or self.player_one.chosen_gesture == "3"):
            self.player_two.win = self.player_two.win + 1
        elif self.player_two.chosen_gesture == "3" and (self.player_one.chosen_gesture == "4" or self.player_one.chosen_gesture == "1"):
            self.player_two.win = self.player_two.win + 1 
        elif self.player_two.chosen_gesture == "4" and (self.player_one.chosen_gesture == "0" or self.player_one.chosen_gesture == "2"):
            self.player_two.win = self.player_two.win + 1
        pass
 

    def show_win(self):
        if self.player_one.win == 2:
            print("Looks like", self.player_one.name, "is the winner!")
        elif self.player_two.win == 2: 
            print("Looks like", self.player_two.name, "is the winner!")
        elif self.player_one.win or self.player_two.win < 2: 
            self.play_hands()
        elif self.player_one.win and self.player_two.win == 2:
            print("It's a tie!")
            self.play_again()
        print("")


    def play_again(self):
        print('Would you like to play again? Yes or No')
        user_input = input("")
        if user_input == "Yes":
            self.choose_game_mode()
        if user_input == "No":
            print('Thanks for playing!')


