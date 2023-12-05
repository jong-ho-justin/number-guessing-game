from random import random

class Game():
    def __init__(self):
        self.start_message()
        self.__answer = self.generate_random()
        self.__attempts = 0

    def generate_random(self):
        return int(random() * 100)
    
    def temp_print_answer(self):
        print(self.__answer)

    def start_message(self):
        print("Welcome. Guess a game from 0-100. You have 5 chance. Goodluck!")