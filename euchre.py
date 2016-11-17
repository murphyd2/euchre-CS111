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
        if self.suit == 0:
            self.suit_name = "Spades"
        elif self.suit == 1:
            self.suit_name = "Clubs"
        elif self.suit == 2:
            self.suit_name = "Hearts"
        elif self.suit == 3:
            self.suit_name = "Diamonds"
        elif self.suit == 4 or self.suit == 5:
            self.suit_name = "Joker"  
            
        if self.number == 11:
            self.number_name = "Jack"
        elif self.number == 12:
            self.number_name = "Queen"
        elif self.number == 13:
            self.number_name = "King"
        elif self.number == 14:
            self.number_name = "Ace"
        else:
            self.number_name = self.number
            
    def get_suit(self):
        return self.suit
   
    def get_number(self):
        return self.number 
    
    def show_card(self):
        print(self.suit, self.number_name)
    
  
       
        
    
    
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
            card = Cards(joker+4, 15)
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


        
class Round:
    # this class will be used to play each round of Eucher.
    def __init__(self, game_type, player0, player1, player2, player3):
        self.game_type = game_type
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
    
    def getDeck(self):
        return self.deck
    
    def deal(self):
        for i in range(5):
            self.player0.hand.append(self.deck.deck.pop())
            self.player1.hand.append(self.deck.deck.pop())
            self.player2.hand.append(self.deck.deck.pop())
            self.player3.hand.append(self.deck.deck.pop())
  
    def trick(self, cards_played):
        print("your cards are: ")
        for i in self.player0.hand:
            i.show_card()
        play_card = input("What card would you like to play? ")
        play_list = play_card.split()
        for j in self.player0.hand:
            try:
                if play_list[0] == j.suit_name and int(play_list[1]) == j.number_name:
                    place = self.player0.hand.index(j)
                    cards_played.append(self.player0.hand.pop(place))
            except:
                if play_list[0] == j.suit_name and play_list[1] == j.number_name:
                    place = self.player0.hand.index(j)
                    cards_played.append(self.player0.hand.pop(place))
        
        print("The cards now in play are: ")
        for card in cards_played:
            card.show_card()
        

            
            
        
        
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
    # I think we should figure the game out with four players and then allow the option to choose after we've figured that out.
    """
    num_players= input("How many players do you want to play with? 2, 3, 4 ")
    num_players= int(num_players)
    if num_players == 4:
        player3 = Player(None, 0)
    if num_players >= 3:
        player2 = Player(None, 0)
    elif num_players >= 2:
        player0 = Player(None, 0)
        player1 = Player(None, 0)
    """
    player0 = Player(None, 0)
    player1 = Player(None, 0)
    player2 = Player(None, 0)
    player3 = Player(None, 0)
    while player0.score < 10 or player1.score < 10 or player2.score < 10 or player3.score < 10:
        t = Round(cardChoice, player0, player1, player2, player3)
        t.deal()
        cards_played = []
        while player0.hand != []:
            t.trick(cards_played)
        
        
    
"""       
for j in range(4):
    for i in range(14):
        Cards(j, i+2)
"""
def main():
    play_game()
    
    
if __name__ == "__main__":
    main()
