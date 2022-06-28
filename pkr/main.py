# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:18:34 2022

@author: adrpaul
"""


deck = StandardDeck()
player = Player()
player.addCard(deck.deal())
player.addCard(deck.deal())
player.cards
player.hand()
