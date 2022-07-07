# -*- coding: utf-8 -*-
"""
Main script to run a simulation of a Poker Match
Nothing much to say here... just run the script
"""

import classes as c
import functions as f


settings = c.PokerSettings()
players = f.createPlayers(settings)
time = 0
speed = 'Hyper'

while (players[0].active == True) and (players[1].active == True):
    f.play(settings, players)
    
    time = time + settings.dealTime + settings.decisionTime
    
    if time >= settings.speed[speed]:   
        settings.tier += 1
        time -= settings.speed[speed]