import random


deck = StandardDeck()
player = Player()
player.addCard(deck.deal())
player.addCard(deck.deal())
player.cards
player.hand()




class Card(object):
    def __init__(self, name, value, suit, symbol,short):
        self.value = value
        self.suit = suit
        self.name = name
        self.symbol = symbol
        self.short = short
        self.showing = True

    def __repr__(self):
        if self.showing:
            return self.symbol
        else:
            return "Card"




class Deck(object):
    def shuffle(self, times=1 ):
        for i in range(times):
            random.shuffle(self.cards)
        print("Deck Shuffled {} times.".format(times))
        
    def deal(self):
        return self.cards.pop(0)
    
    def __repr__(self):
        return self.cards




class StandardDeck(Deck):
    def __init__(self):
        self.cards = []
        suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
        values = {"Two":2,
                  "Three":3,
                  "Four":4,
                  "Five":5,
                  "Six":6,
                  "Seven":7,
                  "Eight":8,
                  "Nine":9,
                  "Ten":10,
                  "Jack":11,
                  "Queen":12,
                  "King":13,
                  "Ace":14 }
    
        for name in values:
          for suit in suits:
            symbolIcon = suits[suit]
            if values[name] < 10:
                short = str(values[name])
                symbol = str(values[name])+symbolIcon
            else:
                short = str(name[0])
                symbol = name[0]+symbolIcon
            self.cards.append( Card(name, values[name], suit, symbol, short) )
         
            
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
                    
        
        
        short = {'22':,
                 '32o',
                 '32s',
                 '33',
                 '42o',
                 '42s',
                 '43o',
                 '43s',
                 '44',
                 '52o',
                 '52s',
                 '53o',
                 '53s',
                 '54o',
                 '54s',
                 '55',
                 '62o',
                 '62s',
                 '63o',
                 '63s',
                 '64o',
                 '64s',
                 '65o',
                 '65s',
                 '66',
                 '72o',
                 '72s',
                 '73o',
                 '73s',
                 '74o',
                 '74s',
                 '75o',
                 '75s',
                 '76o',
                 '76s',
                 '77',
                 '82o',
                 '82s',
                 '83o',
                 '83s',
                 '84o',
                 '84s',
                 '85o',
                 '85s',
                 '86o',
                 '86s',
                 '87o',
                 '87s',
                 '88',
                 '92o',
                 '92s',
                 '93o',
                 '93s',
                 '94o',
                 '94s',
                 '95o',
                 '95s',
                 '96o',
                 '96s',
                 '97o',
                 '97s',
                 '98o',
                 '98s',
                 '99',
                 'A2o',
                 'A2s',
                 'A3o',
                 'A3s',
                 'A4o',
                 'A4s',
                 'A5o',
                 'A5s',
                 'A6o',
                 'A6s',
                 'A7o',
                 'A7s',
                 'A8o',
                 'A8s',
                 'A9o',
                 'A9s',
                 'AA',
                 'AJo',
                 'AJs',
                 'AKo',
                 'AKs',
                 'AQo',
                 'AQs',
                 'ATo',
                 'ATs',
                 'J2o',
                 'J2s',
                 'J3o',
                 'J3s',
                 'J4o',
                 'J4s',
                 'J5o',
                 'J5s',
                 'J6o',
                 'J6s',
                 'J7o',
                 'J7s',
                 'J8o',
                 'J8s',
                 'J9o',
                 'J9s',
                 'JJ',
                 'JTo',
                 'JTs',
                 'K2o',
                 'K2s',
                 'K3o',
                 'K3s',
                 'K4o',
                 'K4s',
                 'K5o',
                 'K5s',
                 'K6o',
                 'K6s',
                 'K7o',
                 'K7s',
                 'K8o',
                 'K8s',
                 'K9o',
                 'K9s',
                 'KJo',
                 'KJs',
                 'KK',
                 'KQo',
                 'KQs',
                 'KTo',
                 'KTs',
                 'Q2o',
                 'Q2s',
                 'Q3o',
                 'Q3s',
                 'Q4o',
                 'Q4s',
                 'Q5o',
                 'Q5s',
                 'Q6o',
                 'Q6s',
                 'Q7o',
                 'Q7s',
                 'Q8o',
                 'Q8s',
                 'Q9o',
                 'Q9s',
                 'QJo',
                 'QJs',
                 'QQ',
                 'QTo',
                 'QTs',
                 'T2o',
                 'T2s',
                 'T3o',
                 'T3s',
                 'T4o',
                 'T4s',
                 'T5o',
                 'T5s',
                 'T6o',
                 'T6s',
                 'T7o',
                 'T7s',
                 'T8o',
                 'T8s',
                 'T9o',
                 'T9s',
                 'TT'
            }

    def __repr__(self):
        return "Standard deck of cards with {0} cards remaining".format(len(self.cards))


    
    
class Player(object, name = "villain"):
    def __init__(self):
        self.cards = []
        self.stack = 1500
        self.active = True

        
    def __repr__(self):
        if self.cards == []:
            return "Player without any cards dealt"
        else:
            return "{},{}".format(self.cards[0],self.cards[1])

    def cardCount(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.append(card)
        
    def hand(self):
        try:
            self.hand = Hand(self.cards)
            return self.hand
        except:
            print("Player without any cards dealt")



        
def hand(object):
    cards = object
    
    if cards[0].value < cards[1].value:
        aux = cards[0]
        cards[0] = cards[1]
        cards[1] = aux
    
    if cards[0].value == cards[1].value and cards[1].value >= 10:
        hand = str(cards[0].short) + str(cards[1].short)
        
    elif cards[0].value == cards[1].value and cards[0].value >= 10 and cards[1].value < 10:
        hand = str(cards[0].short) + str(cards[1].value)
        
    elif cards[0].value == cards[1].value and cards[0].value < 10 and cards[1].value < 10:
        hand = str(cards[0].value) + str(cards[1].value)
        
    elif cards[0].suit == cards[1].suit and cards[1].value >= 10:
        hand = str(cards[0].short) + str(cards[1].short) + "s"
        
    elif cards[0].suit == cards[1].suit and cards[0].value >= 10 and cards[1].value < 10:
        hand = str(cards[0].short) + str(cards[1].value) + "s"
        
    elif cards[0].suit == cards[1].suit and cards[0].value < 10 and cards[1].value < 10:
        hand = str(cards[0].value) + str(cards[1].value) + "s"
        
    elif cards[0].suit != cards[1].suit and cards[1].value >= 10:
        hand = str(cards[0].short) + str(cards[1].short) + "o"
        
    elif cards[0].suit != cards[1].suit and cards[0].value >= 10 and cards[1].value < 10:
        hand = str(cards[0].short) + str(cards[1].value) + "o"
        
    else:
        hand = str(cards[0].value) + str(cards[1].value) + "o"

    return hand




class PokerScorer(object):
    def __init__(self, cards):
        # Number of cards
        if not len(cards) == 5:
            return "Error: Wrong number of cards"

        self.cards = cards

    def flush(self):
        suits = [card.suit for card in self.cards]
        if len( set(suits) ) == 1:
            return True
        return False

    def straight(self):
        values = [card.value for card in self.cards]
        values.sort()

        if not len( set(values)) == 5:
            return False 

        if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
            return 5

        else:
            if not values[0] + 1 == values[1]: return False 
            if not values[1] + 1 == values[2]: return False
            if not values[2] + 1 == values[3]: return False
            if not values[3] + 1 == values[4]: return False

        return values[4]

    def highCard(self):
        values = [card.value for card in self.cards]
        highCard = None
        for card in self.cards:
            if highCard is None:
                highCard = card
            elif highCard.value < card.value: 
                highCard=card

        return highCard

    def highestCount(self):
        count = 0
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) > count:
                count = values.count(value)

        return count

    def pairs(self):
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)

        return pairs
        
    def fourKind(self):
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True

    def fullHouse(self):
        two = False
        three = False
    
        values = [card.value for card in self.cards]
        if values.count(values) == 2:
            two = True
        elif values.count(values) == 3:
            three = True

        if two and three:
            return True

        return False



class handsCompare(object):
    pass

class PokerSettings():
    def __init__(self):
        self.gameType = {"Normal": 720,
                "Turbo": 300,
                "Hyper": 180 }
    
        self.blinds = [[20,10,0],
                  [30,15,0],
                  [50,25,0],
                  [100,50,0],
                  [150,75,0],
                  [200,100,0],
                  [250,125,25],
                  [300,150,25],
                  [400,200,50],
                  [600,300,50],
                  [800,400,75],
                  [1000,500,100],
                  [1200,600,125],
                  [1600,800,150],
                  [2000,1000,200],
                  [3000,1500,300],
                  [4000,2000,400],
                  [5000,2500,500],
                  [6000,3000,600],
                  [7000,3500,700]]
        
        self.maxPlayers = 9
    

        

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
