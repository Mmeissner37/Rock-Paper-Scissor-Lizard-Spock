from player import Player 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 

    def choose_gesture(self):
        self.chosen_gesture = input("Please enter your hand: ")
        if input == "0":
            self.chosen_gesture = Player.gestures(0)
        if input == "1":
            self.chosen_gesture = Player.gestures(1)
        if input == "2":
            self.chosen_gesture = Player.gestures(2)
        if input == "3":
            self.chosen_gesture = Player.gestures(3)
        if input == "4":
            self.chosen_gesture = Player.gestures(4)







    # def choose_gesture(self):
    #     self.chosen_gesture = random.choice(self.gestures)
    #     print(f'{self.name} has picked {self.chosen_gesture}')



