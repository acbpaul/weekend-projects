# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:17:13 2022

@author: adrpaul
"""


import random

# Card class with attributes that a card might hold to a multitude of games
class Card(object):
    
    # Innate attributes to a single card
    def __init__(self, rank, value, suit, symbol, suit_rank, short):
        self.rank = rank             # Card rank: "Two" or "King", for example
        self.value = value           # Card value from rank, 2-14 (Ace = 14)
        self.suit = suit             # Card suit: "Hearts" or "Spades", for example
        self.symbol = symbol         # Card suit symbol: "♡","♠","♢","♣"
        self.suit_rank = suit_rank   # Relative strength between suits in a game
        self.short = short           # Card short name: "2♣" or "K♡", for example
        self.face_up = True          # If set to False, the card is not visible to the player
        self.joker = False           # Used in games where a card can earn (or override) original values

    # Only shows card values if face_up = True
    def __str__(self):
        if self.face_up:
            return "{} {} of {}".format(self.short, self.rank, self.suit)
        else:
            return "Card face down!"

    # Show values regardless of face up value (debugging purposes only)  
    def __repr__(self):
        return """
Rank:       {},
Value:      {},
Suit:       {}, 
Symbol:     {}, 
Suit Rank:  {},
Short:      {},
Faceup:     {}
""".format(self.rank, self.value, self.suit, self.symbol,
           self.suit_rank, self.short, self.face_up)

##############################################################################

# Instantiated object from a particular game deck. 
# Has methods that can be applied to most card games
class Dealer(object):
    
    # Shuffles the deck a random ammount of times for good measure
    def shuffle(self, shuffles=random.randint(2,8)):
        for i in range(shuffles):
            random.shuffle(self.cards)
        print("Deck Shuffled!")
    
    # Deals a card from the top (last card in the list)
    def deal(self):
        return self.cards.pop()
    
    #Simple descriptors for deck object  
    def __str__(self):
        return "Deck of cards with {} cards remaining".format(len(self.cards))
    
    def __repr__(self):
        for card in self.cards: print(card)

##############################################################################



# Standard deck for a game of Poker
class PokerDeck(Dealer):
    def __init__(self):
        
        values = {"Two":    ("2", 2),
                  "Three":  ("3", 3),
                  "Four":   ("4", 4),
                  "Five":   ("5", 5),
                  "Six":    ("6", 6),
                  "Seven":  ("7", 7),
                  "Eight":  ("8", 8),
                  "Nine":   ("9", 9),
                  "Ten":    ("T",10),
                  "Jack":   ("J",11),
                  "Queen":  ("Q",12),
                  "King":   ("K",13),
                  "Ace":    ("A",14)}
        
        suits = {"Clubs":("♣",1),"Diamonds":("♢",2),"Hearts":("♡",3),"Spades":("♠",4)}
        
        self.cards = []

        for suit in suits:
            symbol = suits[suit][0]
            suit_rank = suits[suit][1]
            for rank in values:
                value = values[rank][1]
                short = values[rank][0]+suits[suit][0]
                self.cards.append(Card(rank, value, suit, symbol, suit_rank, short))

##############################################################################    

class PokerTable(Dealer)
    pass











        
            
# Standard deck for a game of Truco
class TrucoDeck(Deck):
    def __init__(self):
        
        values = {"Four":1,
                  "Five":2,
                  "Six":3,
                  "Seven":4,
                  "Queen":5,
                  "Jack":6,
                  "King":7,
                  "Ace":8,
                  "Two":9,
                  "Three":10}
        
        suits = {"Diamonds":("♢",1), "Spades":("♠",2), "Hearts":("♡",3), "Clubs":("♣",4)}
        
        self.cards = []

        for suit in suits:
          for rank in values:
            symbol = str(suits[suit])
            if values[rank] < 10:   short = str(values[rank])+suits[suit]
            else:                   short = str(rank[0]+suits[suit])
                
            self.cards.append(Card(rank, values[rank], suit, suits[suit], short))
         
            
            
            
            
            
# Contains the cards dealt from the deck to a player in a given game          
class Hand(object):
    # Computes all possible initial hands combinations
    self.pairs = []
    for i in range(len(self.cards)-1):
        for j in range(i+1,len(self.cards)):
            self.pairs.append([self.cards[i],self.cards[j]])
            
    self.hands = []
    for item in self.pairs:
        self.hands.append(hand(item))
        
    self.hands = list(set(self.hands))
    self.hands.sort()
    
    def pairingHands(self.pairs,self.hands):
        self.short = dict
        for pair in self.pairs:
            for hand in self.hands:
                if pair[0].value == pair[1].value and str(pair[0].value)*2 == hand:
                    self.short 
