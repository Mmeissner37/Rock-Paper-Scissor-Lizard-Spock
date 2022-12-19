from player import Player 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 
        self.win = 0

    def choose_gesture(self):
        self.chosen_gesture = input("Please enter your hand: ")
        if input == "0":
            print("You chose Rock")
            self.chosen_gesture = Player.gestures(0)
        if input == "1":
            print("You chose Paper")
            self.chosen_gesture = Player.gestures(1)
        if input == "2":
            print("You chose Scissors")
            self.chosen_gesture = Player.gestures(2)
        if input == "3":
            print("You chose Lizard")
            self.chosen_gesture = Player.gestures(3)
        if input == "4":
            print("You chose Spock")
            self.chosen_gesture = Player.gestures(4)
            






    # def choose_gesture(self):
    #     self.chosen_gesture = random.choice(self.gestures)
    #     print(f'{self.name} has picked {self.chosen_gesture}')



