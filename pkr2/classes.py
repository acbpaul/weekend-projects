import random

class Card:
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
        
class Deck(Card):
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
        return str(self.cards)


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

class Player:
# Player Class with general methods applied to most card games

    def __init__(self, i = 1):
        self.name = 'Player {}'.format(i)
        self.cards = []
        self.active = True
        
    def __repr__(self):
        return str([self.name, self.hand(), self.active])
    
    def __str__(self):
        return 'Name: {}, Cards: {}, Is active?: {}'.format(
            self.name, str(self.cards), self.active)
    
    # Number of cards dealt to the player
    def cardCount(self):
        return len(self.cards)

    # Used with deck.deal() to receive a card from the deck
    def addCard(self, card):
        self.cards.append(card)
        
    # Change Player name:
    def changeName(self, name):
        self.name = name
        
    # Define current action based (or not) in past actions
    # def defineAction(self, pastActions):
    # #TODO

    # Defines a notation on the current hand       
    def hand(self):
        hand = '' 
        if self.cards == []: 
            return "Player without any cards dealt"
        
        else: 
            for card in self.cards:
                hand = hand + ' ' + str(card.short)
                return hand
            

        
# class Strategy():
    #TODO
    


class PokerPlayer(Player):
# Player object with defined actions a player might take in a Poker Match

    def __init__(self, stack=1000):
        # Poker Player attributes
        Player.__init__(self)
        self.stack      = stack
        self.bet        = 0
        self.bigBlind   = False
        self.smallBlind = False
        self.allIn      = False
        
        
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
            return self.betAllIn()
        else:
            self.stack -= bet
            self.bet += bet
            return bet
    
    # Pay the initial fee at the start of the round
    def payBlind(self,blind):
        return self.payBet(blind)   
    
    # Adds pot chips to own stack at the end of a round
    def winPot(self,pot):
        self.stack += pot
        self.cards = []
        self.bet = 0
        return True
    
    # Just loses the cards at hand =(
    def losePot(self):
        self.cards = []
        self.bet = 0
        return True
        
        
    # Defines a short notation on the hand received ('AKs','TJo',e.g.)        
    def hand(self):
        if len(self.cards) == 2:
            # Organizing cards in hand by card value
            sorted(self.cards, key=lambda x: x.value)
            
            if self.cards[0].value == self.cards[1].value:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0])
                return hand
                
            elif self.cards[0].symbol == self.cards[1].symbol:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 's'
                return hand
            else:
                hand = str(self.cards[0].short[0]) + str(self.cards[1].short[0]) + 'o'
                return hand
        else:
            return Player.hand(self)
            
        
    def appraiseHand(self, table):
        self.fullHand = self.cards+table
        self.appraise = f.appraise(self.fullHand)



class Table(players):
# Class used with the attributes and actions a table (or a dealer) usually has in a card game
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.actions = []
        for i in range(len(players)):
            self.players.append(players.pop(random.randrange(len(players))))

    def __repr__(self):
        return 'This table contains {} active players.'.format(len(players))
    
    def addPlayer(Player):
        self.players.append(Player)

    def removePlayer(Player):
        self.players.pop(self.position.index(Player))

    def askAction(Player):
        self.actions.append((Player.name,Player.action))

    def dealCard(self, object):
        if isinstance(object, Player):
            Player.addCard(self.deck.deal())
        if isinstance(object, list):
            list.append(self.deck.deal())
        return object
    
    def discardCard(self):
        self.deck[-1].face_up = False
        self.deck.pop()



    # TODO (should it even be here? Maybe in Settings -> PokerSettings)
    # def updateTime(Settings, askAction):
    #     def wrapper():
    #         Settings.clock = Settings.clock + self.actionTime
    #         askAction()
    #     return wrapper



class PokerTable(Table):
# Class used with the attributes and actions a table (or a dealer) usually has in a poker game
    def __init__(self):
        self.players    = Table.__init__(self)
        self.deck       = PokerDeck(self.deck)
        self.button     = random.randrange(len(self.players))
        self.commcards  = []
        self.pot        = 0
        self.players[self.button].bigBlind      = True
        self.players[self.button-1].smallBlind  = True
        self.positions = []
        self.bet = 0
        for player in self.players:
            self.positions.append(self.players.index(player))

    def __repr__(self):
        return 'This poker table contains {} active players.'.format(len(position))
    
    def assignNewBBs(self):
        self.button = self.players.index(self.players[self.button+1])
        for i in range(len(self.players)):
            if i == self.button: self.players[i].bigBlind = True
            elif i == (self.button - 1): self.players[i].smallBlind = True
            else: 
                self.players[i].bigBlind = False
                self.players[i].smallBlind = False
                
    def chargeBlinds(self, Settings):
        for player in self.players:
            if player.bigBlind   == True: self.pot += player.payBlind(Settings.BB)
            if player.smallBlind == True: self.pot += player.payBlind(Settings.SB)
        self.bet = Settings.BB

    def chargeBet(player, Settings):
        if player.action






 class PokerEvaluator(object):   
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