# You will roll a fair diece until the game stops.
# The game stops when you get a 4, 5, or 6.
# For every number 1, 2, or 3 you have thrown your score increases by +1. 
# If the game stops with a 4 or 5, you get paid the accumulated score. 
# If the game stops with a 6 you get nothing. 
# What is the expected payoff of this game?

import random

payoff = 0
isNext = True

def UpdatePayoff(x):
    global payoff 
    global isNext
    if x <= 3:
        payoff += 1
    elif x == 6:
        payoff = 0
        isNext = False
    else:
        isNext = False

def PlayGame():
    while isNext:
        sampleDice = random.randint(1, 6)
        UpdatePayoff(sampleDice)

def PlayManyGames(gameCount):
    global payoff
    global isNext
    payoffTotal = 0
    for x in range(gameCount):
        PlayGame()
        payoffTotal += payoff
        payoff = 0
        isNext = True
    print(payoffTotal / gameCount)

PlayManyGames(100000)
