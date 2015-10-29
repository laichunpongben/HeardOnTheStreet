# Heard on the Street
# Q4.2a

# payoff max of 3 dice sample dots

import random

def play_game(): 
    u1 = random.randint(1, 6)
    u2 = random.randint(1, 6)
    u3 = random.randint(1, 6)
    return max(u1, u2, u3)

def play_many_games(game_count):
    payoff_total = 0
    for x in range(game_count):
        payoff_total += play_game()
    print(payoff_total / game_count)

play_many_games(100000)
