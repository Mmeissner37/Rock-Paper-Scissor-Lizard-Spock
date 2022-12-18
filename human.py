from player import Player 


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name) 

    def choose_gesture(self):
        self.chosen_gesture = input("Please chose your hand: ")
        if self.chosen_gesture == "0":
            self.chosen_gesture = "Rock"
        if self.chosen_gesture == "1":
            self.chosen_gesture = "Paper"
        if self.chosen_gesture == "2":
            self.chosen_gesture = "Scissors"
        if self.chosen_gesture == "3":
            self.chosen_gesture = "Lizard"
        if self.chosen_gesture == "4":
            self.chosen_gesture = "Spock"


    # def choose_gesture(self):
    #     self.chosen_gesture = random.choice(self.gestures)
    #     print(f'{self.name} has picked {self.chosen_gesture}')



