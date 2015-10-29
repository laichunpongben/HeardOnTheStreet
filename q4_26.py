# Heard on the Street
# Q4.26

# You will roll a fair diece until the game stops.
# The game stops when you get a 4, 5, or 6.
# For every number 1, 2, or 3 you have thrown your score increases by +1. 
# If the game stops with a 4 or 5, you get paid the accumulated score. 
# If the game stops with a 6 you get nothing. 
# What is the expected payoff of this game?

import random

payoff = 0
is_next = True

def update_payoff(x):
    global payoff 
    global is_next
    if x <= 3:
        payoff += 1
    elif x == 6:
        payoff = 0
        is_next = False
    else:
        is_next = False

def play_game():
    while is_next:
        sample_dice = random.randint(1, 6)
        update_payoff(sample_dice)

def play_many_games(game_count):
    global payoff
    global is_next
    payoff_total = 0
    for x in range(game_count):
        play_game()
        payoff_total += payoff
        payoff = 0
        is_next = True
    print(payoff_total / game_count)

play_many_games(100000)
