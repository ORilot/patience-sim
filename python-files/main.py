# The main file. Currently the only file.
# push to GitHub by doing the following commands in order:
# git status
# git add .
# git commit -m "YOUR MESSAGE"
# git push origin main
# Import statements
import random as rand

# A class for cards, with each having a number and a suit
class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        # Face 0 means the card is face down and face 1 means the card is face up
        self.face = 0

    def Name(self):
        return(self.number, self.suit)

# Tuples of numbers and suits for making a deck
# Note that Jacks, Queens and Kings are 11, 12 and 13 respectively
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
suits = ('s','h','c','d')
# List called sorted_deck to add all the cards to
sorted_deck = []

# Iteratively adding a card to the deck for each 
# number and suit combination
for suit in suits:
    for number in numbers:
        sorted_deck.append(Card(number, suit))

class Game:
    def __init__(self, deck):
        # The seven stacks of cards 
        self.stack_1 = []
        self.stack_2 = []
        self.stack_3 = []
        self.stack_4 = []
        self.stack_5 = []
        self.stack_6 = []
        self.stack_7 = []
        # The four stacks starting with the aces
        self.ace_s = []
        self.ace_h = []
        self.ace_c = []
        self.ace_d = []
        # The cards that are shuffled through 3 at a time
        self.hand = []
        # A full deck of cards
        self.deck = deck
    
    # A function to start the game, setting it up with the stacks and hand etc.
    def start(self):
        
        # Randomly shuffle the deck of cards
        rand.shuffle(self.deck)

        # For each stack of cards, append the correct number of cards to each
        self.stack_1.append(self.deck.pop())

        for _ in range(2):
            self.stack_2.append(self.deck.pop())
        
        for _ in range(3):
            self.stack_3.append(self.deck.pop())
        
        for _ in range(4):
            self.stack_4.append(self.deck.pop())
        
        for _ in range(5):
            self.stack_5.append(self.deck.pop())
        
        for _ in range(6):
            self.stack_6.append(self.deck.pop())
        
        for _ in range(7):
            self.stack_7.append(self.deck.pop())

        # Within each of these stacks of cards, flip the topmost one to be face up
        self.stack_1[-1].face = 1
        self.stack_2[-1].face = 1
        self.stack_3[-1].face = 1
        self.stack_4[-1].face = 1
        self.stack_5[-1].face = 1
        self.stack_6[-1].face = 1
        self.stack_7[-1].face = 1

        for _ in range(24):
            self.hand.append(self.deck.pop())

new_game = Game(sorted_deck)
new_game.start()
for card in new_game.hand:
    print(card.Name())