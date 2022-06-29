# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:17:26 2022

@author: Adriano
"""

class PokerPlayer():
    
    cards = []
    stack = 500
    active = True
    
    def __init__(self, name, stack):
        self.name = name

    def cardCount(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.append(card)
        
    def paySmallBlind(self,sb):
        if sb > self.stack: 
            sb = self.stack
            self.stack -= self.stack
            return sb
        else:
            self.stack -= sb
            return sb
        
    def payBigBlind(self, bb):
        if bb > self.stack: 
            bb = self.stack
            self.stack -= self.stack
            return bb
        else:
            self.stack -= bb
            return bb
        
    def betAllIn(self):
        bet = self.stack
        self.stack -= bet
        return self.stack
    
    def payBet(self,bet):
        if bet > self.stack: 
            bet = self.stack
            self.stack -= self.stack
            return bet
        else:
            self.stack -= bet
            return bet
    

            
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


    
    def __str__(self):
        if self.cards == []:
            return "Player without any cards dealt!"
        else:
            return "{}, {}".format(self.cards[0],self.cards[1])