# -*- coding: utf-8 -*-
"""
Code to train the CFR Algorithmn
"""

def payout(scoreP0, scoreP1, h):
    if h == "PBP":
        return -1
    elif h == "BP":
        return 1
    if (scoreP0[1] == scoreP1[1]):
        m = 0
    elif (scoreP0[1] > scoreP1[1]):           #change payout according to winning hand
        m = 1      
    else:
        m = -1
    if h == "PP":
        return m
    if h in ["BB", "PBB"]:
        return m*5
    assert False
    return 1

def get_information_set(rs, h):
    assert h not in TERMINAL
    if h == "":
        return str(rs[0])
    elif len(h) == 1:
        return str(rs[1]) + h
    else:
        return str(rs[0]) + "PB"
    assert False

def cfr(rs, h, i, t, pi1, pi2, sc0, sc1):
    # random.choice(HANDS), "", i, t, 1, 1
    
    # rs = realstate
    # h = history
    # i = player
    # t = timestep
    
    # rs = hand
    # h = ''
    # i = 1
    # t= 1
    # pi1 = 1
    # pi2 =1
    
    if h in TERMINAL:
        return payout(sc0, sc1, h) * (1 if i == 1 else -1)
    I = get_information_set(rs, h)
    ph = 2 if len(h) == 1 else 1
      
    # if we are here, we have both actions available
    vo = 0.0
    voa = {}
    for a in ACTIONS:
        if ph == 1:
            voa[a] = cfr(rs, h+a, i, t, sigma[t][I][a] * pi1, pi2, sc0, sc1)
        else:
            voa[a] = cfr(rs, h+a, i, t, pi1, sigma[t][I][a] * pi2, sc0, sc1)
        vo += sigma[t][I][a] * voa[a]
    if ph == i:
        if i == 1:
            pi = pi1
            pnegi = pi2
        else:
            pi = pi2
            pnegi = pi1
        for a in ACTIONS:
            regret[I][a] += pnegi * (voa[a] - vo)
            strategy[I][a] += pi * sigma[t][I][a]
        # update the strategy based on regret
        rsum = sum([max(x, 0) for x in regret[I].values()])
        for a in ACTIONS:
            if rsum > 0:
                sigma[t+1][I][a] = max(regret[I][a], 0) / rsum
            else:
                sigma[t+1][I][a] = 0.5
    return vo



# All possible initial hand combinations (not sure how I´ll use this one yet)
pokerHands = ['22',
              '32o','32s','33',
              '42o','42s','43o','43s','44',
              '52o','52s','53o','53s','54o','54s','55',
              '62o','62s','63o','63s','64o','64s','65o','65s','66',
'72o','72s','73o','73s','74o','74s','75o','75s','76o','76s','77',
'82o','82s','83o','83s','84o','84s','85o','85s','86o','86s','87o','87s','88',
'92o','92s','93o','93s','94o','94s','95o','95s','96o','96s','97o','97s',
'98o','98s','99',
'T2o','T2s','T3o','T3s','T4o','T4s','T5o','T5s','T6o','T6s','T7o','T7s',
'T8o','T8s','T9o','T9s','TT',
'J2o','J2s','J3o','J3s','J4o','J4s','J5o','J5s','J6o','J6s','J7o','J7s',
'J8o','J8s','J9o','J9s','JTo','JTs','JJ',
'Q2o','Q2s','Q3o','Q3s','Q4o','Q4s','Q5o','Q5s','Q6o','Q6s','Q7o','Q7s',
'Q8o','Q8s','Q9o','Q9s','QTo','QTs','QJo','QJs','QQ',
'K2o','K2s','K3o','K3s','K4o','K4s','K5o','K5s','K6o','K6s','K7o','K7s',
'K8o','K8s','K9o','K9s','KTo','KTs','KJo','KJs','KQo','KQs','KK',
'A2o','A2s','A3o','A3s','A4o','A4s','A5o','A5s','A6o','A6s','A7o','A7s',
'A8o','A8s','A9o','A9s','ATo','ATs','AJo','AJs','AQo','AQs','AKo','AKs', 'AA']

pokerHands.reverse()

HANDS = []
for idx, i in enumerate(pokerHands): 
    for j in range(idx,len(pokerHands)):
            HANDS.append((str(i), pokerHands[j]))
            
ACTIONS = ["P", "B"]

ISETS = []
for a in pokerHands: ISETS.append(a)
for a in ACTIONS: 
    for b in pokerHands: ISETS.append(b+a)
for a in pokerHands: ISETS.append(a+"PB")

# ISETS = ["1", "2", "3",   # round 1#          "P1", "P2", "P3", "B1", "B2", "B3",  # round 2
#          "PB1", "PB2", "PB3"]  # round 3

# terminal history states
TERMINAL = ["PP", "PBP", "PBB", "BP", "BB"]

# init tables
regret = {}
strategy = {}
for I in ISETS:
    regret[I] = {k:0 for k in ACTIONS}
    strategy[I] = {k:0 for k in ACTIONS}
  
sigma = {}
sigma[1] = {}
for I in ISETS:
    sigma[1][I] = {k:0.5 for k in ACTIONS}
 
    
# learn strategy
import copy
import classes as c
import functions as f

settings = c.PokerSettings('match', 'random', 'random') 

for t in range(1, 200000):
    sigma[t+1] = copy.deepcopy(sigma[t])
    players = f.createPlayers(settings)
    deck, table, discard, pot = f.initiateTable() 
    players, deck = f.dealHand(players, deck)
    discard, table, deck = f.dealFlop(players, discard, table, deck)
    discard, table, deck = f.dealTurn(players, discard, table, deck)
    discard, table, deck = f.dealRiver(players, discard, table, deck)
    scoreP0, scoreP1, winner, winnerHand = f.checkWinner(table, players)
    hand = (players[0].hand(),players[1].hand())

    for i in [1,2]:
        cfr(hand, "", i, t, 1, 1, scoreP0, scoreP1) # hands pair, history, player, game, pi1, pi2
    del sigma[t], table, deck, players, hand, discard


# print "average" strategy
# for k,v in strategy.items():
#     norm = sum(list(v.values()))
#     print("%3s:P:%.2f B:%.2f" % (k, v['P']/norm, v['B']/norm))
    

import pandas as pd
df = pd.DataFrame(strategy).T
df = df.div(df.sum(axis=1), axis=0)
df.to_csv('strategy200k.csv', index=True)



##############################################################################
##############################################################################
##############################################################################
##############################################################################






