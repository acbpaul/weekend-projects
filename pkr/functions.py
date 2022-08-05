# -*- coding: utf-8 -*-
"""
All methods used in the Poker Match Simulator

The way they are now, it is not possible to have more than 2
simultaneous players in a match (so far, there is no need to expand on it too)
"""

from itertools import combinations
import classes as c
import random
import pandas as pd


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
    if speed != 'zero':
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
        if player.button == False:  
            # Pays the Big Blind
            pot += player.payBlind(settings.blindLvl[settings.tier][0])

        else:
            # Pays the Small Blind and gets to Call First
            pot += player.payBlind(settings.blindLvl[settings.tier][1])
    return players, pot

def chargeBlindDiff(player, pot, settings):
    if player.action in ['P','B']:  
        pot += player.payBet(settings.blindLvl[settings.tier][0]
                               -settings.blindLvl[settings.tier][1])
    return player, pot    


def dealHand(players,deck):
    for j in range(2):
        for i in range(len(players)):
            if players[i].button == True:
                players[i].addCard(deck.deal())
                players[i-1].addCard(deck.deal())
    return players, deck


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
    return discard, table, deck
    


   
def dealTurn(players, discard, table, deck):
    discard.append(deck.deal())
    table.append(deck.deal())
    table[3].face_up = True
    printTable(players, table)
    return discard, table, deck

   
def dealRiver(players, discard, table, deck):
    discard.append(deck.deal())
    table.append(deck.deal())
    table[4].face_up = True
    printTable(players, table)
    return discard, table, deck
    
    
def checkWinner(table, players):
    # Selects the best hand from each player -------------------------------
    scoreP0 = checkHand(table, players[0].cards)
    scoreP1 = checkHand(table, players[1].cards)
    
    # Compares both hands to define the round's winner (or a tie) ----------
    player, hand = compareHand(scoreP0,scoreP1)
    return scoreP0, scoreP1, player, hand  


def printResults(pot, players, winner, scoreP0, scoreP1):
    if winner != 'split':       
        i = int(winner)
        if players[i].bet < pot/2:      pot = players[i].bet*2
    
    print("--------------------------------------------------------------------------------")
    print("Pot: {}, Bets: {}x{}, P0 stack: {}, P1 stack: {}".format(pot, players[0].bet, players[1].bet,
                                                                    players[0].stack, players[1].stack))
    if winner != 'split':
        print("Winner: Player {} - {} x {} wins {}".format(winner, scoreP0[0],scoreP1[0], pot))
    else: 
        print("Split Pot! - {} x {} each wins {}".format(scoreP0[0],scoreP1[0], int(pot/2)))
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
    pot = 0
    return players, pot


def restart(settings, players, pot):
    if settings.gameMode == 'tournament':
        # Moving the button around to define the next blind charges
        for player in players:      
            player.button = not player.button
            player.allIn = False
        
        # Restarting players round's bets and checking for losers
        for player in players:
            player.bet = 0
            if player.stack == 0:       player.active = False
            
    else:                               players[0].active = False
    return players, pot
    



def endMatch(players,pot, i, settings):
    print("--------------------------------------------------------------------------------")
    print("Pot: {}, Bets: {}x{}, P0 stack: {}, P1 stack: {}".format(pot, players[0].bet, players[1].bet,
                                                                    players[0].stack, players[1].stack))
    print("Winner: Player {} - {} x {} wins {}".format(abs(i), players[0].cards,
                                                     players[1].cards, pot))
    print("--------------------------------------------------------------------------------")
   
    # Pays the pot accordingly
    players, pot = payout(players, i, pot)        
        
    # If in Tournament Mode, passes the button for the next match
    players, pot = restart(settings, players, pot)
    return players, pot


def checkBet(player,pot, settings):
    if player.action == 'B':
        pot += player.payBet(settings.blindLvl[settings.tier][0]*3)
    return player, pot
    
        
        
    
def play(settings, players):
    """
    The heart and soul of the game model!
    """
#-------------------------------------------------------------------------
    # Initiate table
    deck, table, discard, pot = initiateTable()     
#-------------------------------------------------------------------------
    # Charges blinds according to the button
    players, pot = chargeBlind(players, pot, settings)      
#-------------------------------------------------------------------------
    # Deals 2 cards to each player      
    players, deck = dealHand(players, deck)                  
#-------------------------------------------------------------------------
         
    # TO-DO Player input (pass, fold, bet)
    actions = []
    strategy = pd.read_csv('strategy500k-7.csv', index_col = 'Unnamed: 0')
    for i in range(len(players)):
        # First Small Blind Player round of Action
        if players[i].button == True:
            players[i].defineAction(actions, strategy)
            actions.append(players[i].action) 
            players[i], pot = chargeBlindDiff(players[i], pot, settings)
            players[i], pot = checkBet(players[i],pot,settings)
            
            # Big Blind Player round of Action
            players[i-1].defineAction(actions, strategy)
            actions[0] = actions[0] + players[i-1].action
            
            # Ends match if button bets and BB doesn't
            if players[i].action == 'B' and players[i-1].action != 'B':
                players, pot = endMatch(players, pot, i, settings)
                return players
            
            # BB pays bet when button bets
            elif players[i].action == 'B' and players[i-1].action == 'B':
                players[i-1], pot = checkBet(players[i-1],pot,settings)
                
            # Defines another action for button if first P then BB bets    
            if players[i-1].action == 'B' and players[i].action == 'P':
                players[i].defineAction(actions, strategy)
                actions[0] = actions[0] + players[i].action
                players[i], pot = checkBet(players[i],pot,settings)
                
                # Ends match if button doesn't pay BB bet
                if players[i].action == 'P':   
                    players, pot = endMatch(players, pot, i-1, settings)
                    return players
            
    

#--------------------------------------------------------------------------
    # Deal Cards for the Flop 
    discard, table, deck = dealFlop(players, discard, table, deck)            
#--------------------------------------------------------------------------
    # TO-DO Player input ((pass, bet))
    # if players[0].allIn == False and players[1].allIn == False:
    #     pass
    

#--------------------------------------------------------------------------
    # Deal Card for the Turn
    discard, table, deck = dealTurn(players, discard, table, deck)          
#--------------------------------------------------------------------------
    # Deal Card for the River
    discard, table, deck = dealRiver(players, discard, table, deck)                
#--------------------------------------------------------------------------
    
    # Defines match winner and winner hand    
    scoreP0, scoreP1, winner, winnerHand = checkWinner(table, players)
    
    # Small print for debugging purposes
    printResults(pot, players, winner, scoreP0, scoreP1)
   
    # Pays the pot accordingly
    players, pot = payout(players, winner, pot)        
        
    # If in Tournament Mode, passes the button for the next match
    players, pot = restart(settings, players, pot)

    return players



def PokerMatch(gameMode, gameSpeed, strategyP0, strategyP1, log):
    # Initializing settings w/ strategy for each player
    settings = c.PokerSettings(gameMode, strategyP0, strategyP1)  
    
    # Creates players according to settings.maxPlayers
    players = createPlayers(settings)
    
    # Initial Time
    time = 0   
           
    
    # Starts match
    while (players[0].active == True) and (players[1].active == True):
        players = play(settings, players)
        time = updateTime(time, settings, gameSpeed)
        
    
    for i, player in enumerate(players):
        if players[i].active == True:
            # winLog.append(str(i))
            print('Winner is Player {}'.format(i))
            log.append(i)
        
        
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
    
def quad(cards):
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