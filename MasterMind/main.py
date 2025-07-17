# main.py
from mastermind import MasterMind

"""
Entry point for MasterMind game
"""
game = MasterMind()

while game.is_active: # some property indicating that the game is active
    game.take_turn() # some method to process a turn