from player import Player 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 
        self.win = 0

    def choose_gesture(self):
        print("Please enter your hand: ")
        self.chosen_gesture = input()
        if self.chosen_gesture == "0":
            print(f'{self.name} chose Rock')
        if self.chosen_gesture == "1":
            print(f'{self.name} chose Paper')
        if self.chosen_gesture == "2":
            print(f'{self.name} chose Scissors')
        if self.chosen_gesture == "3":
            print(f'{self.name} chose Lizard')
        if self.chosen_gesture == "4":
            print(f'{self.name} chose Spock')
        elif self.chosen_gesture == "":
            print('Please chose between 0 and 4')

            



    # def choose_gesture(self):
    #     self.chosen_gesture = random.choice(self.gestures)
    #     print(f'{self.name} has picked {self.chosen_gesture}')



