# payout: 
# 0,0 => A+1
# 1,1 => A+3
# 0,1 or 1,0 => B+2

import random

pA0 = 0.5
pB0 = 0.5
payoutA = 0
payoutB = 0
payoutTotalA = 0
payoutTotalB = 0
cnt = 0
goalA = 1.5
goalB = 1.5

def SampleA():
    global pA0
    uA = random.uniform(0, 1)
    if (uA < pA0): return 0
    else: return 1

def SampleB():
    global pB0
    uB = random.uniform(0, 1)
    if (uB < pB0): return 0
    else: return 1

def Payout(a, b):
    global payoutA
    global payoutB
    x = a + b
    if (x == 0): payoutA += 3
    elif (x == 1): payoutB += 2
    elif (x == 2): payoutA += 1

def PlayGame():
    global cnt
    cnt += 1
    Payout(SampleA(), SampleB())

def PlayManyGames(gameCount):
    global payoutTotalA
    global payoutTotalB
    global payoutA
    global payoutB

    for x in range(gameCount):
        PlayGame()

    payoutTotalA += payoutA
    payoutTotalB += payoutB


def PlayAndLearn(setCount):
    global payoutTotalA
    global payoutTotalB
    global payoutA
    global payoutB
    global pA0
    global pB0
    global cnt
    
    for x in range(setCount):
        overallAverageA = 0
        overallAverageB = 0
        if (cnt > 0):
            overallAverageA = payoutTotalA / cnt
            overallAverageB = payoutTotalB / cnt

        PlayManyGames(100)
        averageA = payoutA / 100
        averageB = payoutB / 100
        payoutA = 0
        payoutB = 0

        if (averageA > overallAverageA): 
            if (pA0 < 1): pA0 += 0.005
        elif (averageA < overallAverageA): 
            if (pA0 < pB0): pA0 += 0.01
            else: pA0 += -0.01

        if (averageB > overallAverageB): 
            if (pB0 > 0): pB0 += -0.005
        elif (averageB < overallAverageB): 
            if (pB0 < 0.5): pB0 += 0.01
            else: pB0 += -0.01

def Report():
    print(pA0)
    print(pB0)
    print(payoutTotalA / cnt)
    print(payoutTotalB / cnt)
    print((payoutTotalA + payoutTotalB) / cnt)

PlayAndLearn(1000)
Report()
