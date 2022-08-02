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
    
    sorted_cards = sorted(cards, key= lambda x: x.value, reverse=True)
    hands = list(combinations(sorted_cards,5))
    
    checks = [c.checkHand(hand) for hand in hands] 
    
    best = [check.power for check in checks]
    best = best.index(max(best))
    
    return hands[best], checks[best].power



def compareHand(scoreP0,scoreP1):
    """
    This method compares the power of each player's best hand obtained 
    in the checkHand() method to evaluate the winner of a round 
    (or a split pot, in case of common cards for both players)
    """
    if scoreP0[1] > scoreP1[1]: return 0, scoreP0[0]
    elif scoreP0[1] == scoreP1[1]: return 'split', scoreP0[0]
    return 1, scoreP1[0]
        
    
def updateTime(time, settings, speed):
    if speed != 'Zero':
        time = time + settings.dealTime + settings.decisionTime
        
        if time >= settings.speed[speed]:   
            settings.tier += 1
            time -= settings.speed[speed]
        
    return time
        

def createPlayers(settings):
    """
    Creates players according to the settings from PokerSettings class.
    So far, there is no need to create more than 2 players
    """
    
    # players = [c.PokerPlayer(settings.stack, 'random') for player in range(nrPlayers)]
    
    players = []
    players.append(c.PokerPlayer(settings.stack, settings.playerType0))
    players.append(c.PokerPlayer(settings.stack, settings.playerType1))

    players[random.randint(0,settings.maxPlayers-1)].button = True
    
    return players




def initiateTable():
    deck = c.PokerDeck()
    deck.shuffle()
    
    table = []
    discard = []
    pot = 0
    return deck, table, discard, pot



def chargeBlind(players, pot, settings):
    for player in players:
        if player.button == True:  
            pot += player.payBlind(settings.blindLvl[settings.tier][0])

        else:
            pot += player.payBlind(settings.blindLvl[settings.tier][1])
        


def dealHand(players,deck):
    for j in range(2):
        for i in range(len(players)):
            if players[i].button == True:
                players[i].addCard(deck.deal())
                players[i-1].addCard(deck.deal())


def printTable(players, table):
    if players[0].playerType == 'human' or players[1].playerType == 'human':
        print('---------------------------------------')
        print(table)
        print('---------------------------------------')
    
    
        
def dealFlop(players, discard, table, deck):
    discard.append(deck.deal())
    table.append(deck.deal())
    table.append(deck.deal())
    table.append(deck.deal())
    table[0].face_up = True
    table[1].face_up = True
    table[2].face_up = True
    printTable(players, table)
    


   
def dealTurn(players, discard, table, deck):
    discard.append(deck.deal())
    table.append(deck.deal())
    table[3].face_up = True
    printTable(players, table)

   
def dealRiver(players, discard, table, deck):
    discard.append(deck.deal())
    table.append(deck.deal())
    table[4].face_up = True
    printTable(players, table)
    
    
def checkWinner(table, players):
    # Selects the best hand from each player -------------------------------
    scoreP0 = checkHand(table, players[0].cards)
    scoreP1 = checkHand(table, players[1].cards)
    
    # Compares both hands to define the round's winner (or a tie) ----------
    player, hand = compareHand(scoreP0,scoreP1)
    return scoreP0, scoreP1, player, hand  


def printResults(pot, players, winner, scoreP0, scoreP1):
    print("Pot: {}, Bets: {}x{}".format(pot, players[0].bet, players[1].bet))
    print("Winner: Player {} - {}x{} wins {}".format(winner, scoreP0[0],scoreP1[0], pot))
    print("--------------------------------------------------------------------------------")   
    
    
def payout(players, winner, pot):
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


def restart(settings, players):
    if settings.gameMode == 'Tournament':
        # Moving the button around to define the next blind charges
        for player in players:      player.button = not player.button
        
        # Restarting players round's bets and checking for losers
        for i in range(len(players)):
            players[i].bet = 0
            if players[i].stack == 0:       players[1].active = False
            
    else: players[0].active, players[1].active == False
    

            
            
            
        
    
def play(settings, players):
    """
    The heart and soul of the game model!
    """
#-------------------------------------------------------------------------
    deck, table, discard, pot = initiateTable()     # Initiate table
#-------------------------------------------------------------------------
    chargeBlind(players, pot, settings)      # Charges blinds according to the button
#-------------------------------------------------------------------------      
    dealHand(players, deck)                  # Deals 2 cards to each player
#-------------------------------------------------------------------------         
    # TO-DO Player input
    

#--------------------------------------------------------------------------   
    dealFlop(players, discard, table, deck)          # Deal Cards for the Flop  
#--------------------------------------------------------------------------
    # TO-DO Player input
    

#--------------------------------------------------------------------------
    dealTurn(players, discard, table, deck)          # Deal Card for the Turn
#--------------------------------------------------------------------------
    dealRiver(players, discard, table, deck)         # Deal Card for the River       
#--------------------------------------------------------------------------
    
    # Defines match winner and winner hand    
    scoreP0, scoreP1, winner, winnerHand = checkWinner(table, players)
    
    # Small print for debugging purposes
    printResults(pot, players, winner, scoreP0, scoreP1)
   
    # Pays the pot accordingly
    payout(players, winner, pot)        
        
    # If in Tournament Mode, passes the button for the next match
    restart(settings, players)




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
    
def four(cards):
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