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
        while self.player_one.win < 2 and self.player_two.win < 2:
            self.play_hands()
            self.determine_winner()
        self.show_win()
        self.play_again()

    def display_rules(self):
        print("")
        print("Welcome to the game! Here are the rules: \n")
        sleep(0.5)
        print("Rock crushes Scissors")
        sleep(0.5)
        print("Scissors cuts Paper")
        sleep(0.5)
        print("Paper covers Rock")
        sleep(0.5)
        print('Rock crushes Lizard')
        sleep(0.5)
        print('Lizard poisons Spock') 
        sleep(0.5)
        print('Spock smashes Scissors')
        sleep(0.5)
        print('Scissors decapitates Lizard')
        sleep(0.5)
        print('Lizard eats Paper')
        sleep(0.5)
        print('Paper disproves Spock') 
        sleep(0.5)
        print('Spock vaporizes Rock \n')


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
        sleep(0.5)
        print('')
        print('Type 0 for Rock')
        sleep(0.5)
        print('Type 1 for Paper')
        sleep(0.5)
        print('Type 2 for Scissors')
        sleep(0.5)
        print('Type 3 for Lizard')
        sleep(0.5)
        print('Type 4 for Spock ')
        sleep(0.5)
        print('')
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()


    def determine_winner(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture: 
            print("It was a tie!")
        elif self.player_one.chosen_gesture == "Rock": 
            if self.player_two.chosen_gesture == "Scissors" or self.player_two.chosen_gesture == "Lizard":
                self.player_one.win += 1
                print(f'{self.player_one.name} won this round!')
            elif self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Spock":
                self.player_two.win += 1
                print(f'{self.player_two.name} won this round!')
        elif self.player_one.chosen_gesture == "Paper": 
            if self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Spock":
                self.player_one.win += 1
                print(f'{self.player_one.name} won this round!')
            elif self.player_two.chosen_gesture == "Scissors" or self.player_two.chosen_gesture == "Lizard":
                self.player_two.win += 1
                print(f'{self.player_two.name} won this round!')
        elif self.player_one.chosen_gesture == "Scissors":
            if self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Lizard":
                self.player_one.win += 1
                print(f'{self.player_one.name} won this round!')
            elif self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Spock":
                self.player_two.win += 1
                print(f'{self.player_two.name} won this round!')
        elif self.player_one.chosen_gesture == "Lizard":
            if self.player_two.chosen_gesture == "Spock" or self.player_two.chosen_gesture == "Paper":
                self.player_one.win += 1
                print(f'{self.player_one.name} won this round!')
            elif self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Scissors":
                self.player_two.win += 1
                print(f'{self.player_two.name} won this round!')
        elif self.player_one.chosen_gesture == "Spock":
            if self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Scissors":
                self.player_one.win += 1
                print(f'{self.player_one.name} won this round!')
            elif self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Lizard":
                self.player_two.win += 1
                print(f'{self.player_two.name} won this round!')
        pass        
 

    def show_win(self):
        if self.player_one.win == 2:
            print(f'{self.player_one.name} wins best of 3!')
            pass
        if self.player_two.win == 2:
            print(f'{self.player_two.name} wins best of 3!')
            pass


    def play_again(self):
        print('Would you like to play again? Yes or No')
        user_input = input("")
        if user_input == "Yes":
            self.run_game()
        if user_input == "No":
            print('Thanks for playing!')
        elif user_input != 'Yes' or 'No':
            print("Please type yes or no")
            self.play_again()


