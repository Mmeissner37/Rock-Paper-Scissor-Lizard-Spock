#Use sleep method to slow down game play---? 

import time 
from human import Human 
from ai import AI
from time import sleep 


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
        print("Welcome to the game! Here are the rules:")
        print(" ")
        #sleep(1)
        print("Rock crushes Scissors")
        #sleep(1)
        print("Scissors cuts Paper")
        #sleep(1)
        print("Paper covers Rock")
        #sleep(1)
        print('Rock crushes Lizard')
        #sleep(1)
        print('Lizard poisons Spock') 
        #sleep(1)
        print('Spock smashes Scissors')
        # sleep(1)
        print('Scissors decapitates Lizard')
        # sleep(1)
        print('Lizard eats Paper')
        # sleep(1)
        print('Paper disproves Spock') 
        # sleep(1)
        print('Spock vaporizes Rock')
        # sleep(1)
        print(" ")


    def choose_game_mode(self):
        user_choice = input('Please press 1 for single player and 2 for multi-player: ')
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
        #sleep(1)
        print('Type 0 for Rock')
        print('Type 1 for Paper')
        print('Type 2 for Scissors')
        print('Type 3 for Lizard')
        print('Type 4 for Spock')
        print("")
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()


    def determine_winner(self):
        if self.player_one.chosen_gesture == "0" and (self.player_two.chosen_gesture == "2" or "Scissors") or (self.player_two.chosen_gesture == "3" or "Lizard"): 
            self.player_one.win = (self.player_one.win + 1)
        elif self.player_one.chosen_gesture == "1" and (self.player_two.chosen_gesture == "0" or "Rock") or (self.player_two.chosen_gesture == "4" or "Spock"):
            self.player_one.win = (self.player_one.win + 1)
        elif self.player_one.chosen_gesture == "2" and (self.player_two.chosen_gesture == "1" or "Paper") or (self.player_two.chosen_gesture == "3" or "Lizard"):
            self.player_one.win = (self.player_one.win + 1)
        elif self.player_one.chosen_gesture == "3" and (self.player_two.chosen_gesture == "4" or "Spock") or (self.player_two.chosen_gesture == "1" or "Paper"):
            self.player_one.win = (self.player_one.win + 1) 
        elif self.player_one.chosen_gesture == "4" and (self.player_two.chosen_gesture == "0" or "Rock") or (self.player_two.chosen_gesture == "2" or "Scissors"):
            self.player_one.win = (self.player_one.win + 1)
        elif self.player_one.choose_gesture == "0" and (self.player_two.chosen_gesture == "0" or "Rock"):
            pass
        elif self.player_one.choose_gesture == "1" and (self.player_two.chosen_gesture == "1" or "Paper"):
            pass
        elif self.player_one.choose_gesture == "2" and (self.player_two.chosen_gesture == "2" or "Scissors"):
            pass
        elif self.player_one.choose_gesture == "3" and (self.player_two.chosen_gesture == "3" or "Lizard"):
            pass
        elif self.player_one.choose_gesture == "4" and (self.player_two.chosen_gesture == "4" or "Spock"):
            pass
        if self.player_two.chosen_gesture == "0" or "Rock" and (self.player_one.chosen_gesture == "2") or (self.player_one.chosen_gesture == "3"): 
            self.player_two.win = (self.player_two.win + 1) 
        elif self.player_two.chosen_gesture == "1" or "Paper" and (self.player_one.chosen_gesture == "0") or (self.player_one.chosen_gesture == "4"):
            self.player_two.win = (self.player_two.win + 1)
        elif self.player_two.chosen_gesture == "2" or "Scissors" and (self.player_one.chosen_gesture == "1") or (self.player_one.chosen_gesture == "3"):
            self.player_two.win = (self.player_two.win + 1)
        elif self.player_two.chosen_gesture == "3" or "Lizard" and (self.player_one.chosen_gesture == "4") or (self.player_one.chosen_gesture == "1"):
            self.player_two.win = (self.player_two.win + 1) 
        elif self.player_two.chosen_gesture == "4" or "Spock" and (self.player_one.chosen_gesture == "0") or (self.player_one.chosen_gesture == "2"):
            self.player_two.win = (self.player_two.win + 1)
        elif self.player_two.choose_gesture == "0" or "Rock" and (self.player_one.chosen_gesture == "0"):
            pass
        elif self.player_two.choose_gesture == "1" or "Paper" and (self.player_one.chosen_gesture == "1"):
            pass
        elif self.player_two.choose_gesture == "2" or "Scissors" and (self.player_one.chosen_gesture == "2"):
            pass
        elif self.player_two.choose_gesture == "3" or "Lizard" and (self.player_one.chosen_gesture == "3"):
            pass
        elif self.player_two.choose_gesture == "4" or "Spock" and (self.player_one.chosen_gesture == "4"):
            pass
        self.show_win()
 

    def show_win(self):
        if self.player_one.win == 1:
            print(f'{self.player_one.name} "won this round!')
            self.play_hands()
        elif self.player_two.win == 1: 
            print(f'{self.player_two.name} "won this round!')
            self.play_hands()
        elif self.player_one.win == 2:
            print(f'{self.player_one.name} wins best of 3!')
            self.play_again()
        elif self.player_two.win == 2:
            print(f'{self.player_two.name} wins best of 3!')
            self.play_again()
        print("")


    def play_again(self):
        print('Would you like to play again? Yes or No')
        user_input = input("")
        if user_input == "Yes":
            self.choose_game_mode()
        if user_input == "No":
            print('Thanks for playing!')


