import random
from typing import List, Dict, Any

i = random.randint(0, 9)

class MasterMind:

    # initialise game by turning game on, set number of guesses, set secret code, etc
    def __init__(self) -> None:
        print(f"Welcome to MasterMind - Code guessing game\n")
        print(f"I'm thinking of a 5 digit number, can you work it out it in 10 guesses?\n")
        self.is_active = True
        self.guesses = 10
        self.code = ""
        for _ in range(0, 5):
            self.code += str(random.randint(0,9))
        self.turn_count = 0
        
    def take_turn(self) -> None:
        if self.turn_count == self.guesses:
            self.__game_lost()
            return
        self.turn_count += 1
        guess = str(input(f"({self.turn_count}) Enter guess: "))
        self.__check_guess(guess)

    def __check_guess(self, guess: str) -> None:
        digits_correct = 0
        for index in range(len(guess)):
            if guess[index] == self.code[index]:
                digits_correct += 1

        if guess == self.code:
            print('Correct!')
            self.__game_won()
        print(f'Incorrect - {digits_correct} correct digit(s)', end='\n\n')
        

    """
    Function to define actions taken upon player losing the game
    """
    def __game_lost(self):
        print('game lost - exiting')
        self.is_active = False

    """
    Function to define actions taken upon player winning the game
    """
    def __game_won(self):
        print('game won - exiting')
        self.is_active = False
    