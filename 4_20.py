# Expected number of tosses need to get 2 heads in a row

import random

def SampleCoin(p):
    u = random.uniform(0, 1)
    if (u < p): return 1
    else: return 0

def PlayGame():
    headCount = 0
    tryCount = 0
    while (headCount < 2):
        tryCount += 1
        sample = SampleCoin(0.5)
        if (sample > 0): headCount += 1
        else: headCount = 0
    return tryCount

def PlayManyGames(gameCount):
    totalTry = 0
    for x in range(gameCount):
        totalTry += PlayGame()
    print(totalTry / gameCount)

PlayManyGames(100000)
