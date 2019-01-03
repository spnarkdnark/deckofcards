# Create script to populate the deck_permutations.txt file with possible shuffles

from Deck import Deck

target_file = 'deck_permutations.txt'

with open(target_file,'w') as f_obj:
    for i in range(10000):
        deck1 = Deck()
        deck1.shuffle_deck()
        f_obj.write('\n' + ''.join(deck1.shorthand()))