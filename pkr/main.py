# -*- coding: utf-8 -*-
"""
Main script to run a simulation of a Poker Match
Nothing much to say here... just run the script
after setting the following parameters:
    
gameMode: single match or tournament
gameSpeed: applicable to tournaments only
playerType0: if 'random': number between 0-1 (Pass proportion to total actions)
             if 'trained': script with P/B weighted strategy (/strats/)
             if 'human': 0 (instructions will be prompted when needed)
i = number or matches or tournaments

Strategies available:
    strategy{trainedHands}-{regret}
        trainedHands = [2^n*10000 where n from 0-8]
        regret = any in [2,4,6,8,10]
"""

train = [80000, 160000, 320000, 640000]
action = [100000, 500000, 2000000]
reg0 = [2,4,6,8]
reg1= [2,4,7,10]
it = 1000
rand = [0, 0.25, 0.5]

import pandas as pd

df = pd.DataFrame(columns = ['gameMode', 'gameSpeed', 'playerType0', 'strategyP0', 'actionP0',
                             'playerType1', 'strategyP1', 'actionP1', 'log', 'resultP1'])

print('\n')
print('---------------------------------------------------------')
for ra in rand:
    for r0 in reg0:
        for r1 in reg1:
            for t in train:
                for act in action: 
                    strat = 'strategy'+str(t)+'-'+str(r0)
                    ac   = 'actions'+str(act)+'-'+str(r1)
                
            
                    import functions as f
                    
                    gameMode    = 'tournament'          # 'tournament' or 'match'
                    gameSpeed   = 'regular'             # 'zero', 'regular', 'turbo' or 'hyper'
                    playerType0 = 'random'              # 'random', 'trained' or 'human'
                    strategyP0  =  ra                   # follow guidelines above
                    actionP0    =  ra
                    playerType1 = 'trained'
                    strategyP1  =  strat
                    actionP1    =  ac
                    
                           
                    log = []
                    
                    if __name__ == "__main__":
                        for i in range(it):            
                            f.PokerMatch(gameMode, gameSpeed, playerType0, strategyP0, actionP0, 
                                         playerType1, strategyP1, actionP1, log)
                        
                        print('Player 1 won '+str(round(sum(log)/it,4))+' tournaments ('
                              +strat+') against '+str(ra) +' randomness while using '+ac)
                        df.loc[df.shape[0]] = [gameMode, gameSpeed, playerType0, strategyP0, actionP0,
                                  playerType1, strategyP1, actionP1, log, round(sum(log)/it,4)]
        print('---------------------------------------------------------')
    print('\n')