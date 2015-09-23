# Payout: 
# 0,0 => A+1
# 1,1 => A+3
# 0,1 or 1,0 => B+2
# Find the mixed strategy Nash equilibrium. 
# Unsupervised learning. Stepwise optimization

import random
from math import exp

strategyA = 0.5
strategyB = 0.5
gamesPayoutA = 0
gamesPayoutB = 0
gamesCardsA = [0, 0]
gamesCardsB = [0, 0]
totalGameCount = 0
totalGamePayoutA = 0
totalGamePayoutB = 0

goalAvgPayoutA = 1.5
goalAvgPayoutB = 1.5

def SampleUniform(p):
    u = random.uniform(0, 1)
    if (u < p): return 0 # card 0
    else: return 1 # card 1

def Payout(a, b):
    x = a + b
    return {
        0: [1, 0],
        1: [0, 2],
        2: [3, 0],
    }[x]

def PlayGame(pA, pB):
    global gamesPayoutA
    global gamesPayoutB
    global gamesCardsA
    global gamesCardsB
    
    a = SampleUniform(pA)
    b = SampleUniform(pB)
    
    if (a == 0): gamesCardsA[0] += 1
    else: gamesCardsA[1] += 1
    
    if (b == 0): gamesCardsB[0] += 1
    else: gamesCardsB[1] += 1
    
    payout = Payout(a, b)
    gamesPayoutA += payout[0]
    gamesPayoutB += payout[1]
    
def PlayGameSet(gameCountInSet):
    for x in range(gameCountInSet):
        PlayGame(strategyA, strategyB)
    pA = EstimateStrategy(gamesCardsA, gameCountInSet)
    pB = EstimateStrategy(gamesCardsB, gameCountInSet)
    avgPayoutA = gamesPayoutA / gameCountInSet
    avgPayoutB = gamesPayoutB / gameCountInSet
    UpdateStrategyA(avgPayoutA, pB)
    UpdateStrategyB(avgPayoutB, pA)
    UpdateTotalGameCount(gameCountInSet)
    UpdateTotalGamePayoutA(gamesPayoutA)
    UpdateTotalGamePayoutB(gamesPayoutB)
    ResetGameSet()
    
def EstimateStrategy(gamesCards, gameCount):
    return gamesCards[0] / gameCount
        
def UpdateStrategyA(avgPayoutA, pB):
    global strategyA
    d = exp(- 0.00001 * totalGameCount)
    newStrategyA = 0
    payoutHistoryA = 0
    if (totalGameCount > 0): totalGamePayoutA / totalGameCount
    
    if (avgPayoutA > payoutHistoryA and pB < 0.5): newStrategyA = strategyA * 0.1
    elif (avgPayoutA > payoutHistoryA and pB > 0.5): newStrategyA = strategyA * 0.1 + 0.9
    elif (avgPayoutA < payoutHistoryA and pB < 0.5): newStrategyA = strategyA * 0.8 + 0.1
    elif (avgPayoutA < payoutHistoryA and pB > 0.5): newStrategyA = strategyA * 0.8 + 0.1
    
    strategyA = (1 - d) * strategyA + d * newStrategyA
    if (strategyA < 0): strategyA = 0
    if (strategyA > 1): strategyA = 1
    
def UpdateStrategyB(avgPayoutB, pA):
    global strategyB
    d = exp(- 0.00001 * totalGameCount)
    newStrategyB = 0
    payoutHistoryB = 0
    if (totalGameCount > 0): payoutHistoryB = totalGamePayoutB / totalGameCount
    
    if (avgPayoutB > payoutHistoryB and pA < 0.5): newStrategyB = strategyB * 0.1 + 0.9
    elif (avgPayoutB > payoutHistoryB and pA > 0.5): newStrategyB = strategyB * 0.1
    elif (avgPayoutB < payoutHistoryB and pA < 0.5): newStrategyB = strategyB * 0.8 + 0.1
    elif (avgPayoutB < payoutHistoryB and pA > 0.5): newStrategyB = strategyB * 0.8 + 0.1
    
    strategyB = (1 - d) * strategyB + d * newStrategyB
    if (strategyB < 0): strategyB = 0
    if (strategyB > 1): strategyB = 1
    
def UpdateTotalGameCount(count):
    global totalGameCount
    totalGameCount += count
    
def UpdateTotalGamePayoutA(payout):
    global totalGamePayoutA
    totalGamePayoutA += payout
    
def UpdateTotalGamePayoutB(payout):
    global totalGamePayoutB
    totalGamePayoutB += payout
    
def ResetGameSet():
    global gamesPayoutA
    global gamesPayoutB
    global gamesCardsA
    global gamesCardsB
    
    gamesPayoutA = 0
    gamesPayoutB = 0
    gamesCardsA = [0, 0]
    gamesCardsB = [0, 0]
            
def Learn():
    global strategyA
    global strategyB
    strategyA = random.uniform(0, 1)
    strategyB = random.uniform(0, 1)
    
    for x in range(5000):
        PlayGameSet(1000)    

def Report():
    print('% 1.0f' % totalGameCount)
    print('% 1.6f' % strategyA)
    print('% 1.6f' % strategyB)
    print('% 1.0f' % totalGamePayoutA)
    print('% 1.0f' % totalGamePayoutB)
    avgPayoutA = totalGamePayoutA / totalGameCount
    avgPayoutB = totalGamePayoutB / totalGameCount
    avgPayout = (totalGamePayoutA + totalGamePayoutB) / totalGameCount
    print('% 1.6f' % avgPayoutA)
    print('% 1.6f' % avgPayoutB)
    print('% 1.6f' % avgPayout)

Learn()
Report()
