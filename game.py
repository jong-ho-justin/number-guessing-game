from random import random

class Game():
    def __init__(self):
        self.start_message()
        self.__answer = self.generate_random()
        self.__attempts = 0
        self.__game_won = False

    # RNG to generate the answer
    def generate_random(self) -> int:
        return int(random() * 100)
    
    # ------------- for troubleshooting, delete after
    def temp_print_answer(self):
        print(self.__answer)

    # just a method that welcomes the player when game is initialized
    def start_message(self):
        print("Welcome. Guess a game from 0-100. You have 5 chance. Goodluck!")

    # method for starting game, loops the game_round method until either self.__game_won turns true or until 5 attempts are made
    def game_start(self):
        while self.__game_won == False and self.__attempts < 5:
            self.game_round()

    # method for a round of game. calls the player_guess method then calls check_if_won method, passing player's guess
    def game_round(self):
        player_guess = self.get_players_guess()
        if self.check_if_won(player_guess):
            self.__game_won = True
            print(f"You win! The answer was {self.__answer}. Your attempt count was {self.__attempts}.")
        else:
            self.__attempts += 1
            print(f"Darn, it wasn't {player_guess}! You have {5-self.__attempts} attempts left. \n")

    # method for acquiring and validating player's input/player's guess
    def get_players_guess(self) -> int:
        need_valid_input = True

        # loops until a valid input has been found
        while need_valid_input:
            player_input = input("Guess a number from 0 to 100: ")

            # in case player just wants to exit
            if player_input.lower() == "exit":
                player_input = None
                need_valid_input = True

            # checking if palyer input were valid numbers
            if player_input.isnumeric():
                player_input = int(player_input)
                if 0 <= player_input <= 100:
                    need_valid_input = False
                else:
                    print("That is not a valid input.\n")
            else:
                print("That is not a valid input.\n")

        return player_input
    
    def check_if_won(self, player_guess) -> bool:
        return player_guess == self.__answer