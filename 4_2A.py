# payoff max of 3 dice sample dots

import random

def PlayGame(): 
    u1 = random.randint(1, 6)
    u2 = random.randint(1, 6)
    u3 = random.randint(1, 6)
    return max(u1, u2, u3)

def PlayManyGames(gameCount):
    payoffTotal = 0
    for x in range(gameCount):
        payoffTotal += PlayGame()
    print(payoffTotal / gameCount)

PlayManyGames(100000)
