import random

class Game():
    def __init__(self):
        self.start_message()
        self.__start, self.__end = self.get_player_range()
        self.__answer = self.generate_random(self.__start, self.__end)
        self.__attempts = 0
        self.__game_won = False

    # RNG to generate the answer
    def generate_random(self, start, end) -> int:
        return random.randrange(start, end+1)
    
    # ------------- for troubleshooting
    def temp_print_answer(self):
        print(self.__answer)

    # just a method that welcomes the player when game is initialized
    def start_message(self):
        print("Welcome. Guess a game from 0-100. You have 5 chance. Goodluck!\n")

    # method for starting game, loops the game_round method until either self.__game_won turns true or until 5 attempts are made
    def game_start(self):
        while self.__game_won == False and self.__attempts < 5:
            self.game_round()
        if self.__game_won == False and self.__attempts < 5:
            print(f"You lost. The answer was {self.__answer}.")
        else:
          print(f"You win! The answer was {self.__answer}. Your attempt count was {self.__attempts}.")

    # method for a round of game. calls the player_guess method then calls check_if_won method, passing player's guess
    def game_round(self):
        player_guess = self.get_players_guess()
        if self.check_if_won(player_guess):
            self.__game_won = True
        else:
            self.__attempts += 1
            print(f"Darn, it wasn't {player_guess}! You have {5-self.__attempts} attempts left. \n")
    
    def get_player_range(self) -> int:
        need_valid_input = True

        while need_valid_input:
            start_range = input("What range would you like to guess from? From: ")

            # checking if palyer input were valid numbers
            if start_range.isnumeric():
                start_range = int(start_range)
                need_valid_input = False
            else:
                print("That is not a valid input.\n")

        need_valid_input = True

        while need_valid_input:
            end_range = input("To: ")

            # checking if palyer input were valid numbers
            if end_range.isnumeric():
                end_range = int(end_range)
                if end_range > start_range:
                    need_valid_input = False
                else:
                    print(f"Needs to be bigger than the starting number of {start_range}.\n")
            else:
                print("That is not a valid input.\n")

        return start_range, end_range

    # method for acquiring and validating player's input/player's guess
    def get_players_guess(self) -> int:
        need_valid_input = True

        # loops until a valid input has been found
        while need_valid_input:
            player_input = input(f"Guess a number from {self.__start} to {self.__end}: ")

            # in case player just wants to exit
            if player_input.lower() == "exit":
                player_input = None
                need_valid_input = True

            # checking if palyer input were valid numbers
            if player_input.isnumeric():
                player_input = int(player_input)
                if self.__start <= player_input <= self.__end:
                    need_valid_input = False
                else:
                    print("That is not a valid input.\n")
            else:
                print("That is not a valid input.\n")

        return player_input
    
    def check_if_won(self, player_guess) -> bool:
        return player_guess == self.__answer