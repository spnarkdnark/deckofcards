# Design the card object


class Card:
    """
    a card object
    """

    def __init__(self,number,suit):
        self._suit = suit
        self._number = number
        self.value = self.getValue()

    def __repr__(self):
        return self._number.title() + " of " + self._suit.title()

    @property
    def shorthand(self):
        return str(self._number[0] + self._suit[0])

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self,suit):
        suits = ['hearts','clubs','diamonds','spades']
        if suit.lower() in suits:
            self._suit = suit.title()
        else:
            print('%s is not an acceptable suit!' % suit)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self,number):
        numbers = ['1','2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
        if number.lower() in numbers:
            self._number = number.title()
        else:
            print('%s is not an acceptable number!' % number)

    def getValue(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        if self._number in numbers:
            return int(self._number)

        else:
            return 11



card1 = Card('3','hearts')

