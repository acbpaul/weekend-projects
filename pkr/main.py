# -*- coding: utf-8 -*-
"""
Main script to run a simulation of a Poker Match
Nothing much to say here... just run the script
"""


import functions as f

gameMode    = 'match'          # tournament or match
gameSpeed   = 'hyper'             # zero, regular, turbo or hyper
strategyP0  = 'random'              # random, human, trained
strategyP1  = 'random'              # random, human trained


if __name__ == "__main__":            
    f.PokerMatch(gameMode, gameSpeed, strategyP0, strategyP1)
