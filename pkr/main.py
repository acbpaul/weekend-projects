# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:18:34 2022

@author: adrpaul
"""

import classes as c
import functions as f

settings = c.PokerSettings()

players = f.createPlayers(settings)


while (players[0].active == True) and (players[1].active == True):
    f.play(settings, players)
    # time = time +dealTime + decisionTime
    
    # if time >= blindTime:   
    #     tier += 1
    #     blind = settings.blindLvl[tier]