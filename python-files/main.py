# The main file. Currently the only file.

# A class for cards, with each having a number and a suit
class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.face = 0

# Tuples of numbers and suits for making a deck
# Note that Jacks, Queens and Kings are 11, 12 and 13 respectively
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
suits = ('s','h','c','d')
# List called deck to add all the cards to
deck = []

# Iteratively adding a card to the deck for each 
# number and suit combination
for suit in suits:
    for number in numbers:
        deck.append(Card(number, suit))

class Game:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.stack_3 = []
        self.stack_4 = []
        self.stack_5 = []
        self.stack_6 = []
        self.stack_7 = []
        self.hand = []

