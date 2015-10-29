# Heard on the Street
# Q4.17

# payoff = final dice result
# player chooses when to stop

import random

def play_game(turn):
    is_next = True
    remaining_turn = turn
    while is_next:
        payoff = random.randint(1,6)
        remaining_turn += -1
        is_next = (remaining_turn > 0) and not(terminate(payoff, remaining_turn))
    return payoff

def terminate(payoff, remaining_turn):
    if (payoff >= 5): return True
    elif (payoff >= 4 and remaining_turn <= 1): return True
    else: return False

def play_many_games(game_count):
    payoff_total = 0.0
    for x in range(game_count):
        payoff_total += play_game(3)
    print(payoff_total / game_count)

play_many_games(100000)
