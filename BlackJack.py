# System for ARGV
import sys

# Importing time for the sleep() funtion. 
import time

# Importing the Shuffle Funtion
from random import shuffle

# Sorce: https://msdn.microsoft.com/en-us/library/ff649643.aspx

# Model–view–controller (MVC) 

# Model - The model manages the behavior and data of the application domain,
# responds to requests for information about its state (usually from the view),
# and responds to instructions to change state (usually from the controller).

# View - The view manages the display of information.


# Controller - The controller interprets the mouse and keyboard inputs
# from the user, informing the model and/or the view to change as appropriate.



# Model Classes Player, Dealer, Card, and Deck are part of the model of this
# program, they literally "manages the behavior and data of the application." 

class Player:
        def __init__(self, name):
            self.name = name
            self.hand = []
        
        def showHand(self):
            for i in range(0, len(self.hand) ): 
                print(  self.hand[i].face + " of " + self.hand[i].suit )
            print( "\n")    

class Dealer:
        def __init__(self, name):
            self.name = name
            self.hand = []
        
        def showHand(self):
            for i in range(0, len(self.hand) ): 
                print( self.hand[i].face )
            print( "\n")

    
class Card:
        def __init__(self, face, suit):
            self.face = face
            self.suit = suit

class Deck:
    def __init__(self, size):
        self.size = size
        self.container = []

    def __str__(self):
        for i in range(0, 52):
            x = ""
            y = self.container[i].face + " " + "of" + " " + self.container[i].suit + "\n" 
            x = x + y 
            return x 

    # This Funtion assumes that the deck is 52 Cards
    # but could easily be edited to work with more
    # the deck side isn't limited to 52. 
    def makeDeck(self, size):

        # Controls making the 2-10, Jack, Queen, King, and Ace
        # for the Spades suit.
        for i in range(2, 11):
            newCard = Card( str(i), "Spades" )
            self.container.append(newCard)
        newCard = Card( "Jack", "Spades" )
        self.container.append(newCard)
        newCard = Card( "Queen", "Spades" )
        self.container.append(newCard)
        newCard = Card( "King", "Spades" )
        self.container.append(newCard)
        newCard = Card( "Ace", "Spades" )
        self.container.append(newCard)

        # Controls making the 2-10, Jack, Queen, King, and Ace
        # for the Hearts suit. 
        for i in range(2, 11):
            newCard = Card( str(i), "Hearts" )
            self.container.append(newCard)
        newCard = Card( "Jack", "Hearts" )
        self.container.append(newCard)
        newCard = Card( "Queen", "Hearts" )
        self.container.append(newCard)
        newCard = Card( "King", "Hearts" )
        self.container.append(newCard)
        newCard = Card( "Ace", "Hearts" )
        self.container.append(newCard)

        # Controls making the 2-10, Jack, Queen, King, and Ace
        # for the Diamonds suit
        for i in range(2, 11):
            newCard = Card( str(i), "Diamonds" )
            self.container.append(newCard)
        newCard = Card( "Jack", "Diamonds" )
        self.container.append(newCard)
        newCard = Card( "Queen", "Diamonds" )
        self.container.append(newCard)
        newCard = Card( "King", "Diamonds" )
        self.container.append(newCard)
        newCard = Card( "Ace", "Diamonds" )
        self.container.append(newCard)

        # Controls making the 2-10, Jack, Queen, King, and Ace
        # for the Clubs suit
        for i in range(2, 11):
            newCard = Card( str(i), "Clubs" )
            self.container.append(newCard)
        newCard = Card( "Jack", "Clubs" )
        self.container.append(newCard)
        newCard = Card( "Queen", "Clubs" )
        self.container.append(newCard)
        newCard = Card( "King", "Clubs" )
        self.container.append(newCard)
        newCard = Card( "Ace", "Clubs" )
        self.container.append(newCard)

# The funtions Deal, Hit, D_Hit(Dealer Hit), and the Hold section of the
# while loop are Model like because they manage data, but I think they
# are more controller because they change the view and change aspects
# of what I already 100% identified to be the model.
 
def Deal(Deck, Dealer, Player):
    # Deal 1 Card to the Dealer 
    Dealer.hand.append( Deck.container.pop() )
    Dealer.hand.append( Deck.container.pop() )
    #Deal 2 cards to the Player
    Player.hand.append( Deck.container.pop() )
    Player.hand.append( Deck.container.pop() )

def Hit(Deck, Dealer, Player):
    Player.hand.append( Deck.container.pop() )
    
def D_Hit(Deck, Dealer, Player):
    Dealer.hand.append( Deck.container.pop() )    

def faceToNumber(Card):
    if Card.face == '2':
        return int(Card.face)
    if Card.face == '3':
        return int(Card.face)
    if Card.face == '4':
        return int(Card.face)
    if Card.face == '5':
        return int(Card.face)
    if Card.face == '6':
        return int(Card.face)
    if Card.face == '7':
        return int(Card.face)
    if Card.face == '8':
        return int(Card.face)
    if Card.face == '9':
        return int(Card.face)
    if Card.face == '10':
        return int(Card.face)

    if Card.face == "Jack": 
        return 10
    if Card.face == "Queen": 
        return 10
    if Card.face == "King":
        return 10
    
    # Aces high
    if Card.face == "Ace": 
        return 11
    else:
        return 999

def main(argv):
    
    # This in the init of the program and is a funtion of the controller. 
    Player_1 = Player("Gregory")
    Dealer_1 = Dealer("Dealer")
    Main_Deck = Deck(52)
    Main_Deck.makeDeck(52)

    # Shuffles the Deck
    shuffle( Main_Deck.container )

    Cont = 9
    while Cont != 10:    
	# This is part of the view 
	# This is the basic UI that interacts with the user. 
        print( "Welcome to BlackJack (Text Based Version)" )
        print( "1 - Deal" )
        print( "2 - Show My Hand" )
        print( "3 - Show Dealers Hand" )
        print( "4 - Hit" )
        print( "5 - Hold")
        print( "\n\n")

        # This input and the "switch" is part of the controller
        # because it litterally interprets a keyboard input and
        # does different task depending on the input. 
        X = input('Choose a number: ')
	
	# 1 - Deal the cars to the players and dealer. 
        if X == 1:
	    # Deal a new hand to all players
            Deal( Main_Deck, Dealer_1, Player_1 )
	
	    # View
            print( "The cards in your hand are: " )
            Player_1.showHand()
	
            print( "The totals of this hand is: " )
            x = 0
            for i in range(0, len(Player_1.hand) ):
                x = x + faceToNumber( Player_1.hand[i] )

            print( x )
            print( "\n")
	
            if x == 21:
                print( "You have Won the Game!" )
                print( "THE PROGRAM WILL ATTEMPT TO EXIT IN 5 SECONDS" )
                time.sleep(5)
                exit()
	    # Quite Unlucky 2 Aces? 
            if x > 21:
                print( "You have Busted!, and lost the game" )
                print( "THE PROGRAM WILL ATTEMPT TO EXIT IN 5 SECONDS" )
                time.sleep(5)
                exit()
	
	# 2 - Show My Hand    
        if X == 2:
	    # View
	    # This could honestly be encased in a function but,
	    # Passing around all the variables seemed like a lot
	    # more work then coping 5 lines each time. 
            Player_1.showHand()
            print( "The totals of this hand is:" )
            x = 0 
            for i in range(0, len(Player_1.hand) ):
                x = x + faceToNumber( Player_1.hand[i] )

            print( x )
            print( "\n")
            
	# 3 - Show Dealers Hand    
        if X == 3:
	    # View 
	    # Only showing one of the 2 cards in the dealers hand
            print( "The dealers visable card is: " )
            print(  "The " + Dealer_1.hand[0].face + " of " + Dealer_1.hand[0].suit + "\n" )
	
	# 4 - Hit    
        if X == 4:
            # Controller Then View 
            Hit( Main_Deck, Dealer_1, Player_1 )
            print( "The totals of this hand is:" )
            x = 0 
            for i in range(0, len(Player_1.hand) ):
                x = x + faceToNumber( Player_1.hand[i] )
            print (x)
            
            if x == 21: # Controller but the prints are View
                print( "You have Won the Game!" )
                print( "THE PROGRAM WILL ATTEMPT TO EXIT IN 5 SECONDS" )
                time.sleep(5)
                exit()
            if x > 21: # Controller but the prints are View
                print( "You have Busted!, and lost the game" )
                print( "THE PROGRAM WILL ATTEMPT TO EXIT IN 5 SECONDS" )
                time.sleep(5)
                exit()

            Player_1.showHand()
            print( "The totals of this hand is:" )
            x = 0 
            for i in range(0, len(Player_1.hand) ):
                x = x + faceToNumber( Player_1.hand[i] )

            print( x )
            print( "\n")
	
	# 5 - Hold
        if X == 5:
	    # View then Controller
            print( "You have chosen to hold." )
            x = 0 
            for i in range(0, len(Player_1.hand) ):
                x = x + faceToNumber( Player_1.hand[i] )
            print( "The totals your hand was: " + str(x) )

            print( "Now lets see how the dealer is doing.\n")

            time.sleep(3)
	
	    # Sum up the Dealers Hand add see if the dealer should hit
            y = 0 
            for i in range(0, len(Dealer_1.hand) ):
                y = y + faceToNumber( Dealer_1.hand[i] )
	
            if y < 17:
                print( "The Dealer was less than 17 and has to hit.\n" )
                D_Hit( Main_Deck, Dealer_1, Player_1 )

            
            print( "The total of the your hand was: " + str(x) + "\n" )
            print( "The total of the dealers hand was: " + str(y) + "\n" ) 
                
            z_1 = 21 - x # Players Total
            z_2 = 21 - y # Dealers Total 
            if z_1 < z_2:
                print( "You were closer to BlackJack!!!\n" )
                print( "You have Won the Game!!\n" )
                print( "THE PROGRAM WILL ATTEMPT TO EXIT IN 5 SECONDS!\n" )
                time.sleep(5)
                exit()
            if z_1 > z_2:
                print( "The dealer was closer to BlackJack!!!\n" )
                print( "The Dealer has Won the Game!!\n" )
                print( "THE PROGRAM WILL ATTEMPT TO EXIT IN 5 SECONDS!\n" )
                time.sleep(5)
                exit()

        # Hidden to show the dealers whole hand. 
        if X == 99:
            # View 
            Dealer_1.showHand()
            print( "The totals of this hand is:" )
            x = 0 
            for i in range(0, len(Dealer_1.hand) ):
                x = x + faceToNumber( Dealer_1.hand[i] )

            print( x )
            print( "\n")

# Catch all for multiply main.
# THIS CAN NOT BE INDENTED!!!
# THIS CAN NOT BE INDENTED!!!
# THIS CAN NOT BE INDENTED!!!
if __name__ == '__main__':
    main(sys.argv)       
