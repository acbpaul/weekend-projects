# -*- coding: utf-8 -*-
"""
All methods used in the Poker Match Simulator

The way they are now, it is not possible to have more than 2
simultaneous players in a match (so far, there is no need to expand on it too)
"""

from itertools import combinations
import classes as c
import random


def checkHand(table,hand):
    """ 
    This method iterates all possible combinations between the cards dealt
    to a player and those at the table.
    
    From the iteration, it returns the best 5-card hand combination along
    with the points used to identify this hand as the best one available.
    """
     
    cards = []
     
    for card in table:  cards.append(card)
    for card in hand:   cards.append(card)
   
    # For some reason, the line below does not work when called, 
    # so I'll leave it off for now
    
    # cards = sorted(cards, key= lambda x: x.value, reverse=True)
    hands = list(combinations(cards,5))
    
    checks = [c.checkHand(hand) for hand in hands] 
    
    best = [check.power for check in checks]
    best = best.index(max(best))
    
    return hands[best], checks[best].power



def compareHand(scoreP0,scoreP1):
    """
    This method compares the returns from the previous checkHand() method
    to evaluate the winner of a round (or a split pot, in case of
                                       common cards for both players)
    """
    if scoreP0[1] > scoreP1[1]: return 0, scoreP0[0]
    elif scoreP0[1] == scoreP1[1]: return 'split', scoreP0[0]
    return 1, scoreP1[0]
        
    

        

def createPlayers(settings):
    """
    Creates players according to the settings from PokerSettings class.
    So far, there is no need to create more than 2 players
    """
    
    nrPlayers = settings.maxPlayers
    players = [c.PokerPlayer(settings.stack) for player in range(nrPlayers)]

    players[random.randint(0,nrPlayers-1)].button = True
    
    return players


def initiateTable():
    pass
        
    
    
def play(settings, players):
    """
    The heart and soul of the game model!
    """
    # Initiate table ----------------------------------------------------
    deck = c.PokerDeck()
    deck.shuffle()
    
    table = []
    discard = []
    pot = 0
    
    # Charges blinds according to the button ----------------------------
    for i in range(len(players)):
        if players[i].button == True:  
            pot += players[i].payBlind(settings.blindLvl[settings.tier][0])

        else:
            pot += players[i].payBlind(settings.blindLvl[settings.tier][1])

    # Deals 2 cards to each player accordingly ---------------------------        
    players[0].addCard(deck.deal())
    players[1].addCard(deck.deal())
    players[0].addCard(deck.deal())
    players[1].addCard(deck.deal())
            
    # TO-DO Player input (no bets for now) --------------------------------------
    # Bet All in?
    
    
    

    # Deal Cards for the Flop ----------------------------------------------
    discard.append(deck.deal())
    table.append(deck.deal())
    table.append(deck.deal())
    table.append(deck.deal())
    table[0].face_up = True
    table[1].face_up = True
    table[2].face_up = True
    
    # Deal Card for the Turn -----------------------------------------------
    discard.append(deck.deal())
    table.append(deck.deal())
    table[3].face_up = True
    
    # Deal Card for the River ----------------------------------------------
    discard.append(deck.deal())
    table.append(deck.deal())
    table[4].face_up = True
    
    # Selects the best hand from each player -------------------------------
    scoreP0 = checkHand(table, players[0].cards)
    scoreP1 = checkHand(table, players[1].cards)
    
    # Compares both hands to define the round's winner (or a tie) ----------
    winner, winnerHand = compareHand(scoreP0,scoreP1)
    
    # Small print for debugging purposes
    print("Pot: {}, Bets: {}x{}".format(pot,
                        players[0].bet,players[1].bet))
    
    # Paying (or splitting) the pot, according to the player's bet ammounts
    if winner != 'split':
        if players[winner].bet < players[winner-1].bet:
            players[winner].winPot(players[winner].bet*2)
            pot -= players[winner].bet*2
            players[winner-1].winPot(pot)
        else:
            players[winner].winPot(pot)
            players[winner-1].losePot()
    else:
        players[0].winPot(players[0].bet)
        pot -= players[0].bet
        players[1].winPot(players[1].bet)
    
    # Moving the button around to define the next blind charges
    players[0].button = not players[0].button
    players[1].button = not players[1].button
    
    # Restarting players round's bets and checking for losers
    for i in range(len(players)):
        players[i].bet = 0
        if players[i].stack == 0:       players[1].active = False
    
        # Another debug print
    print("Winner: Player {} - {}x{} and {}x{} chips!".format(winner,
scoreP0[0],scoreP1[0],
players[0].stack,players[1].stack))
    
    print("--------------------------------------------------------------------------------")
        

    


##############################################################################
######################### POKER HAND CHECK ###################################
##############################################################################

# All these methods below are used to identify a hand rank to provide points
# (or power) in the checkHand class

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
        return False, 0
    
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