# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:17:13 2022
@author: adrpaul
"""


import random
from itertools import combinations
import functions as f


class PokerSettings():
    def __init__(self):
        # Defines blinds structure (BB/SB)
        self.blindLvl = [(20,10),(30,15),(40,20),(50,25),(60,30),(80,40),(100,50),
                    (120,60),(150,75),(180,90),(210,105),(300,150),(400,200)]
        
        
        self.blinds = [[20,10,0],[30,15,0],[50,25,0],[100,50,0],[150,75,0],
                  [200,100,0],[250,125,25],[300,150,25],[400,200,50],
                  [600,300,50],[800,400,75],[1000,500,100],[1200,600,125],
                  [1600,800,150],[2000,1000,200],[3000,1500,300],
                  [4000,2000,400],[5000,2500,500],[6000,3000,600],
                  [7000,3500,700]]
        
        # Defines blind tier (0-12)
        self.tier = 0
        
        # Defines the time needed for a tier change
        self.speed = {"Regular": 360,
                      "Turbo":   180,
                      "Hyper":   120}
        
        
        # Defines player's initial stack
        self.stack = 500
        
        # Defines max number of players
        self.maxPlayers = 2
        
        self.dealTime = 5
        
        self.decisionTime = random.randint(5,15)
        
##############################################################################

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
    def __repr__(self):
        if self.face_up:
            return self.short
        else:
            return "Card face down!"

    # Show values regardless of face up value (debugging purposes only)  
#     def __str__(self):
#         return """
# Rank:       {},
# Value:      {},
# Suit:       {}, 
# Symbol:     {}, 
# Suit Rank:  {},
# Short:      {},
# Faceup:     {}
# """.format(self.rank, self.value, self.suit, self.symbol,
#            self.suit_rank, self.short, self.face_up)

##############################################################################

# Instantiated object from a particular game deck. 
# Has methods that can be applied to most card games
class Deck(object):
    
    
    # Shuffles the deck a random ammount of times for good measure
    def shuffle(self, shuffles=random.randint(5,10)):
        for i in range(shuffles):
            random.shuffle(self.cards)
        print("Deck Shuffled!")
    
    # Deals a card from the top (last card in the list)
    def deal(self):
        return self.cards.pop()
    
    
    # Simple descriptors for Deck object  
    def __str__(self):
        return "Deck of cards with {} cards remaining".format(len(self.cards))
    
    def __repr__(self):
        for card in self.cards: print(card)

##############################################################################

class PokerPlayer():


    def __init__(self, stack):

        self.stack = stack
        self.cards = []
        self.active = True
        self.button = False
        self.bet = 0

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
            self.bet = self.stack
            self.stack -= self.stack
            return bb
        else:
            self.stack -= bb
            self.bet = bb
            return bb
        
    def betAllIn(self):
        bet = self.stack
        self.bet += bet
        self.stack -= bet
        return self.stack
    
    def payBet(self,bet):
        if bet > self.stack: 
            bet = self.stack
            self.bet += bet
            self.stack -= self.stack
            return bet
        else:
            self.stack -= bet
            self.bet += bet
            return bet
        
    def winPot(self,pot):
        self.stack += pot
        self.bet = 0
        
    def losePot(self):
        self.bet = 0
    

            
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
                return hand
            else:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 'o'
                return hand


    
    def __str__(self):
        if self.cards == []:
            return "Player without any cards dealt!"
        else:
            return "{} {}".format(self.cards[0],self.cards[1])
        
##############################################################################

# Standard deck for a game of Poker
class PokerDeck(Deck):
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

class checkHand(object):
    
    def __init__(self, cards):
        self.cards = cards
        
        self.fours, self.foursVal = f.fours(self.cards)
        self.flush = f.flush(self.cards)
        self.straight = f.straight(self.cards)
        self.highCard = self.cards[0].value
        if self.flush == True and self.straight == True:
            self.straightFlush = True
        else: self.straightFlush = False
        self.threes, self.threesVal = f.threes(self.cards)
        self.nPairs, self.pairs, self.pairsVal = f.pairs(self.cards)
        if self.threes == True and self.nPairs == 1:
            self.fullHouse = True
        else: self.fullHouse = False
        self.vals = [card.value for card in cards]
        
        
        self.power = 0        
        self.power += sum([card.value for card in self.cards])
        self.power += sum([val*20 for val in self.pairsVal])
        self.power += self.threesVal*300
        self.power += self.straight*5000
        self.power += self.flush*6000
        self.power += self.fullHouse*6000
        self.power += self.foursVal*10000
        self.power += self.straightFlush*150000
        
        
 












         
# Contains the cards dealt from the deck to a player in a given game          
# class Hand(object):
#     # Computes all possible initial hands combinations
#     self.pairs = []
#     for i in range(len(self.cards)-1):
#         for j in range(i+1,len(self.cards)):
#             self.pairs.append([self.cards[i],self.cards[j]])
            
#     self.hands = []
#     for item in self.pairs:
#         self.hands.append(hand(item))
        
#     self.hands = list(set(self.hands))
#     self.hands.sort()
    
#     def pairingHands(self.pairs,self.hands):
#         self.short = dict
#         for pair in self.pairs:
#             for hand in self.hands:
#                 if pair[0].value == pair[1].value and str(pair[0].value)*2 == hand:
#                     self.short 
                    
                    
                    
                    
                    
                    
                    
                    
                    
############################################################################                  
                    
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
