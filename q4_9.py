# Heard on the Street
# Q4.9

# 3 men dueling
# 10% -> 30% -> 60%
# or 10% -> 60% -> 30%

import random

class Shooter:
    def __init__ (self, p_kill):
        self.p_kill = p_kill
        self.life = True

    def shoot(self, x):
        u = random.uniform(0 ,1)
        if (u < self.p_kill): x.life = False

mr10_win = 0
mr30_win = 0
mr60_win = 0

def play_game():
    global mr10_win
    global mr30_win
    global mr60_win

    mr10 = Shooter(0.1)
    mr30 = Shooter(0.3)
    mr60 = Shooter(0.6)

    remaining_lives = mr10.life + mr30.life + mr60.life
    while (remaining_lives > 1):
        remaining_lives = mr10.life + mr30.life + mr60.life
        if (mr10.life): 
            if (remaining_lives < 3): 
                if (mr60.life): mr10.shoot(mr60)
                elif (mr30.life): mr10.shoot(mr30)
        if (mr60.life):
            if (remaining_lives < 4): 
                if (mr30.life): mr60.shoot(mr30)
                elif (mr10.life): mr60.shoot(mr10)
        if (mr30.life): 
            if (remaining_lives < 4): 
                if (mr60.life): mr30.shoot(mr60)
                elif (mr10.life): mr30.shoot(mr10)

    if (mr10.life): mr10_win += 1
    if (mr30.life): mr30_win += 1
    if (mr60.life): mr60_win += 1

def play_many_games(game_count):
    for x in range(game_count):
        play_game()
    print(mr10_win / game_count)
    print(mr30_win / game_count)
    print(mr60_win / game_count)

play_many_games(100000)
