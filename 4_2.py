# payoff = final dice result
# player chooses when to stop

import random

def PlayGame(turn):
    isNext = True
    remainingTurn = turn
    while isNext:
        payoff = random.randint(1,6)
        remainingTurn += -1
        isNext = (remainingTurn > 0) and not(Terminate(payoff, remainingTurn))
    return payoff

def Terminate(payoff, remainingTurn):
    if (payoff >= 5): return True
    elif (payoff >= 4 and remainingTurn <= 1): return True
    else: return False

def PlayManyGames(gameCount):
    payoffTotal = 0.0
    for x in range(gameCount):
        payoffTotal += PlayGame(3)
    print(payoffTotal / gameCount)

PlayManyGames(100000)
