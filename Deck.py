# Design the deck object

from card import Card
import random


class Deck:
    """
    a deck object
    """

    def __init__(self):
        """
        initialize a clean, unshuffled deck
        """

        self.isShuffled = False
        self.deck = []
        self.populate()

    def __str__(self):
        """
        :return: strings to describe the deck as shuffled or unshuffled
        """
        if self.isShuffled:
            return 'A Sloppily Shuffled Deck of Cards'

        else:
            return 'A Clean Crisp Fresh Deck of Cards'

    def populate(self):
        """
        :return: populate the empty deck of cards at __init__
        """
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        suits = ['hearts', 'spades', 'diamonds', 'clubs']

        for suit in suits:
            for number in numbers:
                self.deck.append(Card(number,suit))

    def shorthand(self):
        """
        :return: print the shorthand of the full deck of cards
        """
        return [card.shorthand for card in self.deck]

    def shuffle_deck(self):
        """
        :return: use random integers to pop and append cards to deck
        """
        for n in range(2):
            for i in range(52):
                seed = random.randint(0,51)
                popped = self.deck.pop(seed)
                self.deck.append(popped)

        self.isShuffled = True

