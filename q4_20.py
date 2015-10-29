# Heard on the Street
# Q4.20

# Expected number of tosses required to get 2 heads in a row

import random

def sample_coin(p):
    u = random.uniform(0, 1)
    if (u < p): return 1
    else: return 0

def play_game():
    head_count = 0
    try_count = 0
    while (head_count < 2):
        try_count += 1
        sample = sample_coin(0.5)
        if (sample > 0): head_count += 1
        else: head_count = 0
    return try_count

def play_many_games(game_count):
    total_try = 0
    for x in range(game_count):
        total_try += play_game()
    print(total_try / game_count)

play_many_games(100000)
