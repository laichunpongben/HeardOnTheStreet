# 3 men dueling
# 10% -> 30% -> 60%
# or 10% -> 60% -> 30%

import random

class Shooter:
    def __init__ (self, pKill):
        self.pKill = pKill
        self.life = True

    def Shoot(self, x):
        u = random.uniform(0 ,1)
        if (u < self.pKill): x.life = False

mr10Win = 0
mr30Win = 0
mr60Win = 0

def PlayGame():
    global mr10Win
    global mr30Win
    global mr60Win

    mr10 = Shooter(0.1)
    mr30 = Shooter(0.3)
    mr60 = Shooter(0.6)

    remainingLives = mr10.life + mr30.life + mr60.life
    while (remainingLives > 1):
        remainingLives = mr10.life + mr30.life + mr60.life
        if (mr10.life): 
            if (remainingLives < 3): 
                if (mr60.life): mr10.Shoot(mr60)
                elif (mr30.life): mr10.Shoot(mr30)
        if (mr60.life):
            if (remainingLives < 4): 
                if (mr30.life): mr60.Shoot(mr30)
                elif (mr10.life): mr60.Shoot(mr10)
        if (mr30.life): 
            if (remainingLives < 4): 
                if (mr60.life): mr30.Shoot(mr60)
                elif (mr10.life): mr30.Shoot(mr10)
        

    if (mr10.life): mr10Win += 1
    if (mr30.life): mr30Win += 1
    if (mr60.life): mr60Win += 1

def PlayManyGames(gameCount):
    for x in range(gameCount):
        PlayGame()
    print(mr10Win / gameCount)
    print(mr30Win / gameCount)
    print(mr60Win / gameCount)

PlayManyGames(100000)
