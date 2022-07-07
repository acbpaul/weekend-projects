# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:29:04 2022

@author: Adriano
"""

from itertools import combinations
import classes as c
import random


def checkHand(table,hand):
     cards = []
     
     
     for card in table:  cards.append(card)
     for card in hand:   cards.append(hand)
     
     cards = sorted(cards, key= lambda x: x.value, reverse=True)
     hands = list(combinations(cards,5))
     
     checks = [c.checkHand(hand) for hand in hands]
     
     best = [check.power for check in checks]
     best = best.index(max(best))
     
     return hands[best], checks[best].power



def compareHand(object):
    pass       
        
    

        

def createPlayers(settings):
    nrPlayers = settings.maxPlayers
    players = [c.PokerPlayer(settings.stack) for player in range(nrPlayers)]

    players[random.randint(0,nrPlayers-1)].button = True
    
    return players


        
    
    
def play(settings, players):
    deck = c.PokerDeck()
    deck.shuffle()
    
    table = []
    discard = []
    pot = 0
    
    for i in range(len(players)):
        if players[i].button == True:  
            pot += players[i].payBigBlind()
            button = 1
        else:
            pot += players[i].paySmallBlind()
            
    players[0].addCard(deck.deal())
    players[1].addCard(deck.deal())
    players[0].addCard(deck.deal())
    players[1].addCard(deck.deal())
            
    # Player input
    # Bet All in?
    
    

    # Deal Cards for the Flop
    discard.append(deck.deal())
    table.append(deck.deal())
    table.append(deck.deal())
    table.append(deck.deal())
    table[0].face_up = True
    table[1].face_up = True
    table[2].face_up = True
    
    # Deal Card for the Turn
    discard.append(deck.deal())
    table.append(deck.deal())
    table[3].face_up = True
    
    # Deal Card for the River
    discard.append(deck.deal())
    table.append(deck.deal())
    table[4].face_up = True
    

    # scoreP1 = f.checkHand(table, players[0].cards)
    # scoreP2 = f.checkHand(table, players[1].cards)
    
    winner = compareHand()
    
    for i in range(len(players)):
        if players[i].button == True:   players[i].button = False
        if players[i].button == False:  players[i].button = True
        if players[i].stack == 0:       players[1].active = False
    


##############################################################################
######################### POKER HAND CHECK ###################################
##############################################################################


def flush(cards):
    suits = [card.suit for card in cards]
    if len(set(suits)) == 1:
        return True
    return False

def straight(cards):
    values = [card.value for card in cards]
    values.sort()

    if not len( set(values)) == 5:
        return False 

    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
        return True

    else:
        if not values[0] + 1 == values[1]: return False 
        if not values[1] + 1 == values[2]: return False
        if not values[2] + 1 == values[3]: return False
        if not values[3] + 1 == values[4]: return False

    return True

# def highCard(cards):
#     highCard = None
#     for card in cards:
#         if highCard is None:
#             highCard = card
#         elif highCard.value < card.value: 
#             highCard=card

#     return highCard.value

# def higherCards(cards):
#     new = []
#     highCard = None
#     while len(cards)>1:
#         for i in range(len(cards)):
#             if highCard is None:
#                 highCard = (cards[i],i)
#                 new.append(highCard[0])
#             elif highCard.value < cards[i].value:
#                 highCard=(cards[i],i)
#                 new[-1]
#                 cards.pop(i)
            

def highestCount(cards):
    count = 0
    values = [card.value for card in cards]
    for value in values:
        if values.count(value) > count:
            count = values.count(value)

    return count

def pairs(cards):
    pairs = []
    values = [card.value for card in cards]
    for value in values:
        if values.count(value) == 2 and value not in pairs:
            pairs.append(value)
    if len(pairs) >= 1: aux = True
    else: aux = False
    return len(pairs), aux, sorted(pairs, reverse=True)

def threes(cards):
    values = [card.value for card in cards]
    for value in values:
        if values.count(value) == 3:
            return True, value
        return False, value
    
def fours(cards):
    values = [card.value for card in cards]
    for value in values:
        if values.count(value) == 4:
            return True, value
        return False, 0

def fullHouse(cards):
    two = False
    three = False

    values = [card.value for card in cards]
    if values.count(values) == 2:
        two = True
    elif values.count(values) == 3:
        three = True

    if two and three:
        return True

    return False 