# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:17:26 2022

@author: Adriano
"""

class PokerPlayer():
    
    cards = []
    stack = 1500
    active = True
    
    def __init__(self, name):
        self.name = name

        
    def __str__(self):
        if self.cards == []:
            return "Player without any cards dealt!"
        else:
            return "{}, {}".format(self.cards[0],self.cards[1])

    def cardCount(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.append(card)
        

            
    def hand(self):
        
        if self.cards == []: print("Player without any cards dealt")
        if len(self.cards) == 2:
            # Organizing cards in hand by card value
            if self.cards[0].value < self.cards[1].value:
                aux = self.cards[0]
                self.cards[0] = self.cards[1]
                self.cards[1] = aux
            
            if self.cards[0].value == self.cards[1].value:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0])
                
            if self.cards[0].symbol == self.cards[1].symbol:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 's'
            else:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 'o'

        return hand