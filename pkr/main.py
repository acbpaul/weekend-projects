# -*- coding: utf-8 -*-
"""
Main script to run a simulation of a Poker Match
Nothing much to say here... just run the script
"""

import classes as c
import functions as f


def PokerMatch():
    # Initializing settings w/ strategy for each player
    settings = c.PokerSettings('match','random', 'random')  
    
    # Creates players according to settings.maxPlayers
    players = f.createPlayers(settings)
    
    # Initial Time
    time = 0

    # Zero, Regular, Turbo, Hyper                            
    speed = 'Zero'                        
    
    # Starts match
    while (players[0].active == True) and (players[1].active == True):
        f.play(settings, players)
        time = f.updateTime(time, settings, speed)
            
PokerMatch()
