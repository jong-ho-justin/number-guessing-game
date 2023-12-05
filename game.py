from random import random

class Game():
    def __init__(self):
        self.start_message()
        self.__answer = self.generate_random()
        self.__attempts = 0
        self.__game_won = False

    def generate_random(self):
        return int(random() * 100)
    
    def temp_print_answer(self):
        print(self.__answer)

    def start_message(self):
        print("Welcome. Guess a game from 0-100. You have 5 chance. Goodluck!")

    def game_start(self):
        self.game_round()

    def game_round(self):
        player_guess = self.get_players_guess()

    def get_players_guess(self):
        player_guess = input("Guess a number from 0 to 100? ")
        if player_guess.isnumeric():
            player_guess = int(player_guess)
        if not 0 >= player_guess >= 100 or type(player_guess) is not int:
            player_guess = input("I don't think that is a number, please try again: ")