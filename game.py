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
        need_valid_input = True
        while need_valid_input:
            player_input = input("Guess a number from 0 to 100: ")
            if player_input.lower() == "exit":
                player_input = None
                need_valid_input = True
            if player_input.isnumeric():
                player_input = int(player_input)
                if 0 <= player_input <= 100:
                    need_valid_input = False
            else:
                print("That is not a valid input.\n")
        return player_input