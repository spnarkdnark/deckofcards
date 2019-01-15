from Deck import Deck


class Player:
    """
    A player object
    """
    def __init__(self, name):
        """
        create a new player as input name, with empty score, hand and isActive set to true
        :param name: name passed from Game.get_players
        """
        self.name = name
        self.score = 0
        self.hand = []
        self.isActive = True

    def __repr__(self):
        """
        return the players name when passed into (print)
        """
        return f'\n Player: {self.name} \n Score: {self.score} \n Hand: {self.hand} \n'


class Game:
    """
    A Game Object
    """
    def __init__(self):
        """
        initiate the game object with an unshuffled deck, empty list of players and state of True
        """
        self.deck = Deck()
        self.players = []
        self.gameOn = True

    def get_players(self):
        """
        fill the self.players with n number of new Players
        :return: no return value; mutates object property
        """
        while True:
            try:
                player_count = int(input('How many players?'))
                break
            except ValueError:
                print('Please enter a valid number!')

        for i in range(player_count):
            name = input(f'Player {i+1} Name?')
            self.players.append(Player(name))

    def deal_cards(self, hand_size):
        """
        Deal a hand to each player in self.players
        :param hand_size: how many cards should be in player.hand at end of loop
        :return: no return value, mutates property of Player object
        """
        for i in range(0, len(self.players)*hand_size):
            card = self.deck.deck.pop(-1)
            self.players[i % len(self.players)].hand.append(card)


class BlackJack(Game):
    """
    A Game of BlackJack
    """

    def __init__(self):
        super().__init__()
        self.deck.shuffle_deck()

    def __repr__(self):
        """
        return a simple statement when BlackJack is called as property
        """
        return 'A Game of BlackJack!'

    def score_hand(self,player):
        """
        Calculate the score of the given player's hand
        :param player: player hand to be scored
        :return: score of the given player's hand
        """
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        score = 0

        for i in range(len(player.hand)):
            if player.hand[i].number in values:
                score += int(player.hand[i].number)
            else:
                score += 11

        return score

    def player_loop(self, player_index):
        """
        Main Player Loop for BlackJack - On each turn, display player info, get hit or stay, and check lose condition
        :param player_index: index of the player from self.players
        :return: no return, operates on self.players
        """
        player = self.players[player_index]

        while player.isActive:

            player.score = self.score_hand(player)

            if player.score > 21:
                print(f'{player.score} Bust!')
                player.isActive = False
                break

            print(player)

            choice = input('Hit or Stay!').lower()

            if choice == 'hit':
                player.hand.append(self.deck.deck[-1])

            elif choice == 'stay':
                break

    def game_loop(self):
        """
        Main Game Loop, gets players, deals cards, goes through player loop for each player until game end
        :return: a fun way to pass the time on your computer terminal
        """
        while True:

            self.get_players()
            self.deal_cards(2)

            for i in range(0, len(self.players)):
                self.player_loop(i)

            for i in range(0, len(self.players)):
                print(self.players[i].name, self.players[i].hand, self.players[i].score)

            restart_game = input('Would you like to play again? Yes / No').lower()

            if restart_game == 'no':
                break


def main():
    """
    I think this will help me execute the program more easily from the terminal
    :return: its gametime baby
    """

    new_game = BlackJack()
    new_game.game_loop()


main()