'''

BlackJack Game

User Stories:

1) User can play the blackjack game in terminal against the dealer
2) Dealer automatically plays his hand with a fixed algorithm (If it's 16 or below they hit, if it's above 16, they stay)
3) User can play the blackjack game repeatedly
4) User can choose to hit or stay
5) User can see what cards they have been dealt
6) User can only see one dealer card, not the bottom card

Tips:
1) Aces can count as an eleven or a one - but it only counts as a one if your score is over 21
2) Research random.shuffle()
3) You are not allowed to code until you design your program!
4) Research __radd__ - it is a built-in method in Python

Extension:
1) Multiple users can play blackjack game in terminal in a turn-based game
2) Consider using the stack data structure
3) User can bet dollar amounts in the blackjack game


'''

import random

suits = {'c': "Clubs", 's': "Spades", 'h': "Hearts", 'd': "Diamonds"}
ranks = ('2','3','4','5','6','7','8','9','10','j','q','k','a')
facecards = {'j': "Jack", 'q': "Queen", 'k': "King", 'a': "Ace"}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s of %s" %(facecards[self.rank] if self.rank in facecards.keys() else self.rank, suits[self.suit])

    def __repr__(self):
        return  self.__str__()

    def __radd__(self,other):
        pass
        
    def value(self):
        if self.rank == 'a':
            self.val = 11
        elif self.rank in ['j','q', 'k']:
            self.val = 10
        else:
            self.val = int(self.rank)
        return self.val


class Deck:
    def __init__(self):
        self.deck = [Card(s,r) for s in suits.keys() for r in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def one(self):
        return self.deck.pop()
        

class Player:
    def __init__(self,name):
        self.name = name
        self.playerhand = []

    def __str__(self):
        return self.name

    def __lt__(self,other):
        #overrides the less than operator
        pass
    
    def get(self,card):
        self.playerhand.append(card)

    def choose(self):
        #"ui, ask user to hit or stand"
        self.decision = raw_input("What's Next? Enter 'h' to hit or 's' to stay  ")
        if self.decision.lower() == "h":
            return True
        elif self.decision.lower() == "s":
            return False
        else:
            print "Please enter 'h' or 's'"
            return self.choose()

    def hand(self):
        self.total = sum([card.value() for card in self.playerhand])
        if self.total > 21:
            for card in self.playerhand:
                if card.rank == 'a':
                    self.total -= 10
        return self.total 

    def bust(self):
        "did the user bust"
        if self.hand() > 21:
            return True
            
    def won(self):
        "do they have 21"
        if self.hand() == 21:
            return True

class Dealer(Player):
    def __init__(self,name):
       Player.__init__(self,name)

    def __str__(self):
        "optional"
        return self.name

    def choose(self):
        if self.hand() < 17:
            return True
        else:
            return False

class Game:
    def __init__(self):
        "Game setup, adds players and a dealer"
        name = raw_input("please enter your playername:  ")
        self.player1 = Player(name)
        self.thedealer = Dealer("Dealer")
        self.gamedeck = Deck()
        self.gamedeck.shuffle()

    def print_table(self,player):
        print "\n=======THE TABLE======== "
        print self.player1
        print "Player Hand:  " + str(self.player1.playerhand)
        print "Total:" + str(self.player1.hand())
        print "========================"
        print self.thedealer
        print "Dealer Hand:  " + str(self.thedealer.playerhand[0])
        #print "Total:" + str(self.thedealer.hand())
        print "\n"

          
    def deal(self):
        while len(self.thedealer.playerhand) < 2:
            self.player1.get(self.gamedeck.one())
            self.thedealer.get(self.gamedeck.one())


    def play(self):
        self.deal()
        self.print_table(self.player1)
        if self.player1.won() == True:
            print "BlackJack! You're the WINNER"
            return
        elif self.thedealer.won() == True:
            print "BlackJack! Dealer Wins!"
            return
       
       #Player Turn
        while self.player1.choose():
            self.player1.get(self.gamedeck.one())
            self.print_table(self.player1)

            if self.player1.won() == True:
                print "BlackJack! You're the WINNER"
                return
            elif self.player1.bust() == True:
                print "It's a Bust!"
                return
         
        #Dealer Turn
        while self.thedealer.choose():
            self.thedealer.get(self.gamedeck.one())
            self.print_table(self.player1)
            if self.thedealer.won() == True:
                print "Dealer score:  " + str(self.thedealer.hand())
                print "BlackJack! Dealer Wins"
                return 
            elif self.thedealer.bust() == True:
                print "Dealer Bust! You Win!"
                return

        if self.thedealer.hand() > self.player1.hand():
            print "Dealer score:  " + str(self.thedealer.hand())
            print "The dealer Wins"
        if self.thedealer.hand() < self.player1.hand():
            print "You Beat the Dealer!"
        if self.thedealer.hand() == self.player1.hand():
            print "It's a Draw...you win?"

g = Game()
g.play()

    
