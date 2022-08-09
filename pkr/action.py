# -*- coding: utf-8 -*-
"""
Code to train the CFR Algorithmn
"""
REG = [2,4,7,10]
ITE = [100000, 500000, 2000000]
for reg in REG:
    for it in ITE:

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
                return m*2
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
        pokerHands = []
        
        
                    
        ACTIONS = ["P", "B"]
        
        sets = ['QD0FL0ST4TR0PR0','QD0FL0ST0TR1PR1','QD0FL0ST0TR0PR0',
 'QD0FL5ST4TR0PR0','QD0FL0ST5TR0PR0','QD0FL5ST5TR0PR0','QD0FL0ST0TR0PR1',
 'QD1FL0ST0TR0PR0','QD0FL0ST0TR1PR0','QD0FL0ST0TR0PR2','QD0FL5ST0TR0PR0',
 'QD0FL4ST0TR0PR1','QD0FL4ST5TR0PR0','QD0FL4ST0TR0PR0','QD0FL4ST4TR0PR0']
        ISETS = []
        for a in sets: ISETS.append(a)
        for a in ACTIONS: 
            for b in sets: ISETS.append(b+a)
        for a in sets: ISETS.append(a+"PB")
        
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
        
        settings = c.PokerSettings('match', 'random', 0.5, 0.5, 'random', 0.5, 0.5) 
        
        for t in range(1, it):
            sigma[t+1] = copy.deepcopy(sigma[t])
            players = f.createPlayers(settings)
            deck, table, discard, pot = f.initiateTable() 
            players, deck = f.dealHand(players, deck)
            discard, table, deck = f.dealFlop(players, discard, table, deck)
            hand0 =[]          
            for card in players[0].cards: hand0.append(card)
            for card in table: hand0.append(card)
            app0 = f.appraise(hand0)
            hand1 =[]          
            for card in players[1].cards: hand1.append(card)
            for card in table: hand1.append(card)
            app1 = f.appraise(hand1)
            app = (app0,app1)
            discard, table, deck = f.dealTurn(players, discard, table, deck)
            discard, table, deck = f.dealRiver(players, discard, table, deck)
            scoreP0, scoreP1, winner, winnerHand = f.checkWinner(table, players)
        
            for i in [1,2]:
                cfr(app, "", i, t, 1, 1, scoreP0, scoreP1) # hands pair, history, player, game, pi1, pi2
            del sigma[t], table, deck, players, app, app0, app1, hand0, hand1, discard
        
        
        # print "average" strategy
        # for k,v in strategy.items():
        #     norm = sum(list(v.values()))
        #     print("%3s:P:%.2f B:%.2f" % (k, v['P']/norm, v['B']/norm))
            
        
        import pandas as pd
        df = pd.DataFrame(strategy).T
        df = df.div(df.sum(axis=1), axis=0)
        df.fillna(0.5, inplace=True)
        df.to_csv('actions/actions{}-{}.csv'.format(it,reg), index=True)



##############################################################################
##############################################################################
##############################################################################
##############################################################################

import classes as c
import functions as f



isets = []

for i in range(500000):
    settings = c.PokerSettings('match', 'random', 0.5, 0.5, 'random', 0.5, 0.5)
    players = f.createPlayers(settings)
    deck, table, discard, pot = f.initiateTable() 
    players, deck = f.dealHand(players, deck)
    discard, table, deck = f.dealFlop(players, discard, table, deck)
    hand =[]          
    for card in players[0].cards: hand.append(card)
    for card in table: hand.append(card)
    app = f.appraise(hand)
    isets.append(app)
    hand = []
    for card in players[1].cards: hand.append(card)
    for card in table: hand.append(card)
    app = f.appraise(hand)
    isets.append(app)
    
    isets = list(set(isets))
   


isets.append('QD0FL5ST5TR0PR0')
isets = list(set(isets))

