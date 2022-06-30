# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:19:54 2022
@author: adrpaul
"""

from itertools import combinations



# All possible initial hand combinations (decide to play or not)
pokerHands = {'22','32o','32s','33','42o','42s','43o','43s','44','52o','52s',
'53o','53s','54o','54s','55','62o','62s','63o','63s','64o','64s','65o','65s',
'66','72o','72s','73o','73s','74o','74s','75o','75s','76o','76s','77','82o',
'82s','83o','83s','84o','84s','85o','85s','86o','86s','87o','87s','88','92o',
'92s','93o','93s','94o','94s','95o','95s','96o','96s','97o','97s','98o','98s',
'99','T2o','T2s','T3o','T3s','T4o','T4s','T5o','T5s','T6o','T6s','T7o','T7s',
'T8o','T8s','T9o','T9s','TT','J2o','J2s','J3o','J3s','J4o','J4s','J5o','J5s',
'J6o','J6s','J7o','J7s','J8o','J8s','J9o','J9s','JTo','JTs','JJ',
'Q2o','Q2s','Q3o','Q3s','Q4o','Q4s','Q5o','Q5s','Q6o','Q6s',
'Q7o','Q7s','Q8o','Q8s','Q9o','Q9s','QTo','QTs','QJo','QJs','QQ',
'K2o','K2s','K3o','K3s','K4o','K4s','K5o','K5s','K6o','K6s','K7o','K7s','K8o',
'K8s','K9o','K9s','KTo','KTs''KJo','KJs','KQo','KQs','KK',
'A2o','A2s','A3o','A3s','A4o','A4s','A5o','A5s','A6o','A6s','A7o','A7s',
'A8o','A8s','A9o','A9s','ATo','ATs','AJo','AJs','AQo','AQs','AKo','AKs', 'AA'}









class handsCompare(object):
    pass

class PokerSettings():
    def __init__(self):
        self.gameType = {"Normal": 720,
                "Turbo": 300,
                "Hyper": 180 }
    

        
        
    

        

def texasHoldem():

    settings = PokerSettings()
    blindTime = settings.gameType["Hyper"]
    decisionTime = 5
    nrPlayers = 2
    
    hero = Player()
    villain = Player()
    
    
    while (hero.active == True) and (villain.active == True):
        play()
    
        
    
    
def play():
    deck = StandardDeck()
    deck.shuffle()

    # Preflop
    
    # Postflop
    
    # Turn
    
    # River
    
    
    deck = StandardDeck()
    deck.shuffle()
    



def interpreterVideoPoker():
    player = Player()
      
    # Intial Amount
    points = 100
      
    # Cost per hand
    handCost = 5
      
    end = False
    while not end:
        print( "You have {0} points".format(points) )
        print()
    
        points-=5
    
        ## Hand Loop
        deck = StandardDeck()
        deck.shuffle()
    
        # Deal Out
        for i in range(5):
            player.addCard(deck.deal())

        # Make them visible
        for card in player.cards:
          card.showing = True
        print(player.cards)
    
        validInput = False
        while not validInput:
            print("Which cards do you want to discard? ( ie. 1, 2, 3 )")
            print("*Just hit return to hold all, type exit to quit")
            inputStr = input()
      
            if inputStr == "exit":
                end=True
        break

        try:
            inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

            for inp in inputList:
              if inp > 6:
                continue 
              if inp < 1:
                continue 

            for inp in inputList:
              player.cards[inp-1] = deck.deal()
              player.cards[inp-1].showing = True

            validInput = True
        except:
            print("Input Error: use commas to separated the cards you want to hold")

        print(player.cards)
        
        #Score
        score = PokerScorer(player.cards)
        straight = score.straight()
        flush = score.flush()
        highestCount = score.highestCount()
        pairs = score.pairs()
    
        # Royal flush
        if straight and flush and straight == 14:
            print("Royal Flush!!!")
            print("+2000")
            points += 2000

        # Straight flush
        elif straight and flush:
            print("Straight Flush!")
            print("+250")
            points += 250

        # 4 of a kind
        elif score.fourKind():
            print("Four of a kind!")
            print("+125")
            points += 125

        # Full House
        elif score.fullHouse():
            print("Full House!")
            print("+40")
            points += 40

        # Flush
        elif flush:
            print("Flush!")
            print("+25")
            points += 25

        # Straight
        elif straight:
            print("Straight!")
            print("+20")
            points += 20

        # 3 of a kind
        elif highestCount == 3:
            print("Three of a Kind!")
            print("+15")
            points += 15

        # 2 pair
        elif len(pairs) == 2:
            print("Two Pairs!")
            print("+10")
            points += 10

        # Jacks or better
        elif pairs and pairs[0] > 10:
          print ("Jacks or Better!")
          print("+5")
          points += 5
    
        player.cards=[]
    
        print()
