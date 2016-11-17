""" Malcolm Grossman and Dylan Murphy
    CS 111 final
    Euchre game
"""

import random 
#import graphics 
class Cards:
    # this class creates cards. Each card has a number associated to its number and suit.
    def __init__(self, suit, number):
        # suits are defined by numbers 0-4. Spades = 0, Clubs = 1, Hearts = 2, Diamonds = 3, Jokers = 4 and 5
        self.suit = suit
        self.number = number
        
    def get_suit(self):
        return self.suit
    
    def get_number(self):
        return self.number 
    
    def show_card(self):
        print(self.suit, self.number)
    
  
       
        
    
    
class Deck:
    # this class creates a deck containing cards.
    def __init__(self, game_type):
        self.game_type = game_type
        deck = []
        for i in range(4):
            for j in range(13):
                card = Cards(i, j+2)
                deck.append(card)
                
        for joker in range(2):
            card = Cards(joker+4, 14)
            deck.append(card)
        self.deck = deck
        
        
    
    
    def get_deck(self):
        return self.deck
    
    def choose_cards(self):
        # this method determines how many cards will be played with in this game.
        # redefines self.deck so that it reflects the deck that will be used in the game.
        self.game_deck = []
        if self.game_type == 34:
            for k in self.deck:
                if k.get_number() >= 7:
                    self.game_deck.append(k)
            self.deck = self.game_deck
        
        elif self.game_type == 30:
            for k in self.deck:
                if k.get_number() >= 8:
                    self.game_deck.append(k)
            self.deck = self.game_deck
        
        elif self.game_type == 26:
            for k in self.deck:
                if k.get_number() >= 9:
                    self.game_deck.append(k)
            self.deck = self.game_deck
        return self.deck
        
    def shuffle(self):
        # this method shuffles the deck.
        self.shuffled_deck= []
        for card in self.game_deck:
            n = random.randrange(len(self.game_deck))
            self.shuffled_deck.insert(n, card)
        self.deck = self.shuffled_deck
        return self.deck

    def deal(self):
        pass
    def show_hand(self):
        pass

        
class Trick:
    # this class will be used to play each round of Eucher, called tricks.
    def __init__(self, game_type, num_players, player0, player1, player2 = None, player3 = None):
        self.game_type = game_type
        self.num_players = num_players
        self.deck = Deck(self.game_type)
        self.player0 = player0
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.deck.choose_cards()
        self.deck.shuffle()
        # use self.deck.deck to access the list of cards
        
    def getGameType(self):
        return self.game_type
    
    def getNumPlayers(self):
        return self.num_players
    
    def getDeck(self):
        return self.deck
    
    def deal(self, player):
        for i in range(5):
            player.hand.append(self.deck.deck.pop())
        return player.hand
        
class Player:
    # creates a player that can either be controlled by the player or the AI.
    def __init__(self, control, score):
        self.control = control
        self.score = score
        self.hand = []
        
    def getControl(self):
        return self.control
    
    def getHand(self):
        return self.hand
    
    def getScore(self):
        return self.score
    
def play_game():
    # plays the game
    cardChoice= input("How many cards do you want to play with? 34, 30, 26 ")
    cardChoice= int(cardChoice)
    num_players= input("How many players do you want to play with? 2, 3, 4 ")
    num_players= int(num_players)
    if num_players == 4:
        player0 = Player(None)
        player1 = Player(None)
        player2 = Player(None)
        player3 = Player(None)
    elif num_players == 3:
        player0 = Player(None)
        player1 = Player(None)
        player2 = Player(None)
    elif num_players == 2:
        player0 = Player(None)
        player1 = Player(None)
    while player0.score < 10 or player1.score < 10 or player2.score < 10 or player3.score < 10:
        t = Trick(cardChoice, num_players, player0, player1, None, None)
    
"""       
for j in range(4):
    for i in range(14):
        Cards(j, i+2)
"""
def main():
    play_game()
    
    
if __name__ == "__main__":
    main()
