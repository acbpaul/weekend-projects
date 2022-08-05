# -*- coding: utf-8 -*-
"""
All classes used in the Poker Match simulator
"""

import random
import functions as f


class PokerSettings():
    # Defines most settings needed to initialize a Poker Match
    def __init__(self, gameMode, playerType0, playerType1):
        # Defines blinds structure (BB/SB)
        self.blindLvl = [(20,10),(30,15),(40,20),(50,25),(60,30),(80,40),(100,50),
                    (120,60),(150,75),(180,90),(210,105),(300,150),(400,200)]
        
        # Blind structure with antes (BB/SB/Ante) -- won't use for now
        # self.blinds = [[20,10,0],[30,15,0],[50,25,0],[100,50,0],[150,75,0],
        #           [200,100,0],[250,125,25],[300,150,25],[400,200,50],
        #           [600,300,50],[800,400,75],[1000,500,100],[1200,600,125],
        #           [1600,800,150],[2000,1000,200],[3000,1500,300],
        #           [4000,2000,400],[5000,2500,500],[6000,3000,600],
        #           [7000,3500,700]]
        
        # Defines blind tier to start a Poker Match (0-12)
        self.tier = 0
        
        # Defines the time needed for a tier change
        self.speed = {"zero":    0,
                      "regular": 360,
                      "turbo":   180,
                      "hyper":   120}
        
        
        # Defines player's initial stack
        self.stack = 500
        
        # Defines max number of players
        self.maxPlayers = 2
        
        # Defines time spent in a round to deal cards
        self.dealTime = 5
        
        # Defines time needed by the players to make a decision
        self.decisionTime = random.randint(5,15)
        
        # Defines if 'tournament' or single 'match'
        self.gameMode = gameMode
        
        # Defines the strategy for each player ('random', 'human', 'trained')
        self.playerType0 = playerType0
        self.playerType1 = playerType1
        
##############################################################################

class Card(object):
# Card class with attributes that a card might hold to a multitude of games
    
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

class Deck(object):
# Instantiated object from a particular game deck. 
# Has methods that can be applied to most card games   
    
    # Shuffles the deck a random ammount of times for good measure
    def shuffle(self, shuffles=random.randint(5,10)):
        for i in range(shuffles):
            random.shuffle(self.cards)
        # print("Deck Shuffled!")
    
    # Deals a card from the top (last card in the deck)
    def deal(self):
        return self.cards.pop()
    
    
    # Simple descriptors for Deck object  
    def __str__(self):
        return "Deck of cards with {} cards remaining".format(len(self.cards))
    
    def __repr__(self):
        for card in self.cards: print(card)

##############################################################################

class PokerPlayer():
# Player object with defined actions a player might take in a Poker Match

    def __init__(self, stack, playerType):

        self.stack = stack
        self.cards = []
        self.active = True
        self.button = False
        self.bet = 0
        self.playerType = playerType
        self.allIn = False

    # Number of cards dealt to the player
    def cardCount(self):
        return len(self.cards)

    # Used with deck.deal() to receive a card from the deck
    def addCard(self, card):
        self.cards.append(card)
        
    # Pay the initial fee at the start of the round
    def payBlind(self,blind):
        if blind > self.stack:
            blind = self.stack
            self.bet = blind
            self.stack -= blind
            self.allIn = True
            return blind
        else:
            self.stack -= blind
            self.bet += blind
            return blind   
    
    # Bets all remaining chips
    def betAllIn(self):
        bet = self.stack
        self.bet += bet
        self.stack -= bet
        self.allIn = True
        return bet
    
    # Calls a bet from another player
    def payBet(self,bet):
        if bet > self.stack: 
            bet = self.stack
            self.bet += bet
            self.stack -= bet
            self.allIn = True
            return bet
        else:
            self.stack -= bet
            self.bet += bet
            return bet
    
    # Adds pot chips to own stack at the end of a round
    def winPot(self,pot):
        self.stack += pot
        self.cards = []
    
    # Just loses the cards at hand =(
    def losePot(self):
        self.cards = []
        
        
    # Defines a short notation on the hand received ('AKs','TJo',e.g.)        
    def hand(self):
        
        if self.cards == []: print("Player without any cards dealt")
        if len(self.cards) == 2:
            # Organizing cards in hand by card value (could've used a lambda...)
            if self.cards[0].value < self.cards[1].value:
                aux = self.cards[0]
                self.cards[0] = self.cards[1]
                self.cards[1] = aux
            
            if self.cards[0].value == self.cards[1].value:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0])
                return hand
                
            elif self.cards[0].symbol == self.cards[1].symbol:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 's'
                return hand
            else:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 'o'
                return hand
            
    def defineAction(self, actions, strategy):
        if self.playerType == 'random':
            if random.uniform(0,1) <= 0.01:
                self.action = 'P'
            else: 
                self.action = 'B'
            
        elif self.playerType == 'human':
            print('Your hand: {} - (B)et or (P)ass?'.format(self.cards))
            self.action = input()
            
        elif self.playerType == 'trained':
            if len(actions)>0:
                if random.uniform(0,1) <= strategy.loc[self.hand()+actions[0]]['P']:
                    self.action = 'P'
                else: 
                    self.action = 'B'
            else:
                if random.uniform(0,1) <= strategy.loc[self.hand()]['P']:
                    self.action = 'P'
                else: 
                    self.action = 'B'
            # self.action = max(self.strategy[self.hand()+actions[0]], 
            #                   key = self.strategy[self.hand()+actions[0]].get)
            
        if self.allIn == True:
            self.action = 'B'


    # To be used with any 2 cards in hand... or none
    def __str__(self):
        if self.cards == []:
            return "Player without any cards dealt!"
        else:
            return "{} {}".format(self.cards[0],self.cards[1])
        
##############################################################################

class PokerDeck(Deck):
# Standard deck for a game of Poker

    def __init__(self):
        
        values = {
                  "Two":    ("2", 2),
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
# Point system to select the best hand (out of all 5 cards combinations out of 7)
# Also used to compare player's best hand to find the round's winner
    
    def __init__(self, cards):
        self.cards = cards
        
        self.quad, self.quadVal = f.quad(self.cards)
        self.flush = f.flush(self.cards)
        self.straight = f.straight(self.cards)
        if self.flush == True and self.straight == True:
            self.straightFlush = True
        else: self.straightFlush = False
        self.threes, self.threesVal = f.threes(self.cards)
        self.nPairs, self.pairs, self.pairsVal = f.pairs(self.cards)
        if self.threes == True and self.nPairs == 1:
            self.fullHouse = True
        else: self.fullHouse = False
        self.vals = [card.value^2 for card in cards]
        
        # Assigned points to a hand based on its rankings
        self.power = 0        
        self.power += sum(self.vals)
        self.power += sum([val*200 for val in self.pairsVal])
        self.power += self.threesVal*3000
        self.power += self.straight*50000
        self.power += self.flush*60000
        self.power += self.fullHouse*60000
        self.power += self.quadVal*100000
        self.power += self.straightFlush*1500000
        
        
    def __str__(self):
        "{}, {}".format(self.cards, self.power)
        
        
 
                    
                    
                    
                 
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
