from card import Card
from Deck import Deck


class Player:

    def __init__(self,name):
        self.name = name
        self.score = 0
        self.hand = []
        self.isActive = True

    def __repr__(self):
        return self.name

    def get_hand_score(self):

        score = 0
        for i in range(0,len(self.hand)):
            score += self.hand[i].value

        if score > 21:
            self.isActive = False

        self.score = score


class Game:

    def __init__(self):

        self.deck = Deck()
        self.players = []
        self.gameOn = True

    def get_game_info(self):

        player_count = int(input('How many players?'))

        for i in range(player_count):
            name = input(f'Player {i+1} Name?')
            self.players.append(Player(name))

        self.deck.shuffle_deck()

    def deal_to_players(self):

        for i in range(0,len(self.players)*2):
            card = self.deck.deck.pop(-1)
            self.players[i%len(self.players)].hand.append(card)

    def player_loop(self,player):

        while self.players[player].isActive == True:

            self.players[player].get_hand_score()

            print(self.players[player].name)
            print(self.players[player].hand,self.players[player].score)

            choice = input('Hit or Stay!').lower()

            if choice == 'hit':
                self.players[player].hand.append(self.deck.deck[-1])

            elif choice == 'stay':
                break

    def game_loop(self):

        for i in range(0,len(self.players)):

            self.player_loop(i)

        for i in range(0,len(self.players)):

            print(self.players[i].name, self.players[i].hand,self.players[i].score)




game1 = Game()
game1.get_game_info()

game1.deal_to_players()

game1.game_loop()