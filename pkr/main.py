# -*- coding: utf-8 -*-
"""
Main script to run a simulation of a Poker Match
Nothing much to say here... just run the script
"""


import functions as f

gameMode    = 'tournament'        # tournament or match
gameSpeed   = 'hyper'             # zero, regular, turbo or hyper
strategyP0  = 'trained'           # random, human, trained
strategyP1  = 'random'            # random, human trained
log = []

if __name__ == "__main__":
    for i in range(1000):            
        f.PokerMatch(gameMode, gameSpeed, strategyP0, strategyP1, log)
