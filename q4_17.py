# Heard on the Street
# Q4.17

# payout: 
# 0,0 => A+1
# 1,1 => A+3
# 0,1 or 1,0 => B+2

import random

p_a0 = 0.5
p_b0 = 0.5
payout_a = 0
payout_b = 0
payout_total_a = 0
payout_total_b = 0
count = 0
goal_a = 1.5
goal_b = 1.5

def sample_a():
    global p_a0
    uA = random.uniform(0, 1)
    if (uA < p_a0): return 0
    else: return 1

def sample_b():
    global p_b0
    uB = random.uniform(0, 1)
    if (uB < p_b0): return 0
    else: return 1

def do_payout(a, b):
    global payout_a
    global payout_b
    x = a + b
    if (x == 0): payout_a += 3
    elif (x == 1): payout_b += 2
    elif (x == 2): payout_a += 1

def play_game():
    global count
    count += 1
    do_payout(sample_a(), sample_b())

def play_many_games(game_count):
    global payout_total_a
    global payout_total_b
    global payout_a
    global payout_b

    for x in range(game_count):
        play_game()

    payout_total_a += payout_a
    payout_total_b += payout_b

def play_and_learn(set_count):
    global payout_total_a
    global payout_total_b
    global payout_a
    global payout_b
    global p_a0
    global p_b0
    global count
    
    for x in range(set_count):
        overall_average_a = 0
        overall_average_b = 0
        if (count > 0):
            overall_average_a = payout_total_a / count
            overall_average_b = payout_total_b / count

        play_many_games(100)
        average_a = payout_a / 100
        average_b = payout_b / 100
        payout_a = 0
        payout_b = 0

        if (average_a > overall_average_a): 
            if (p_a0 < 1): p_a0 += 0.005
        elif (average_a < overall_average_a): 
            if (p_a0 < p_b0): p_a0 += 0.01
            else: p_a0 += -0.01

        if (average_b > overall_average_b): 
            if (p_b0 > 0): p_b0 += -0.005
        elif (average_b < overall_average_b): 
            if (p_b0 < 0.5): p_b0 += 0.01
            else: p_b0 += -0.01

def report():
    print(p_a0)
    print(p_b0)
    print(payout_total_a / count)
    print(payout_total_b / count)
    print((payout_total_a + payout_total_b) / count)

play_and_learn(1000)
report()
