""" Malcolm Grossman and Dylan Murphy
    CS 111 final
    Euchre game
"""

import random 
#import graphics 
class Cards:
    # This class creates a card with a suit and a number, represented by numbers.
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
    #This class initializes a deck class with 52 cards.
    def __init__(self, game_type, playerNumber):
        self.game_type = game_type
        self.playerNumber = playerNumber
        deck = []
        # creates 13 cards of each suit using the Card class and appends them to the card list.
        for i in range(4):
            for j in range(13):
                card = Cards(i, j+2)
                deck.append(card)
        # creates 2 jokers each with the same number but with suit numbers 4 and 5.
        for joker in range(2):
            card = Cards(joker+4, 14)
            deck.append(card)
        self.deck = deck
        
       
    def get_deck(self):
        return self.deck
    
    def get_game_type(self):
        return self.game_type
    
    def get_player_number(self):
        return self.playerNumber
    
    def choose_cards(self):
        #chooses the number of cards the game will be played with based on a user input.
        self.game_deck = []
        if self.game_type == 34:
            for k in self.deck:
                if k.get_number() >= 7:
                    self.game_deck.append(k)
            return self.game_deck
        
        elif self.game_type == 30:
            for k in self.deck:
                if k.get_number() >= 8:
                    self.game_deck.append(k)
            return self.game_deck
        
        elif self.game_type == 26:
            for k in self.deck:
                if k.get_number() >= 9:
                    self.game_deck.append(k)
            return self.game_deck
        
    def shuffle(self):
        #shuffles the deck 
        self.shuffled_deck= []
        for card in self.game_deck:
            n = random.randrange(len(self.game_deck))
            self.shuffled_deck.insert(n, card)
        return self.shuffled_deck

    def deal(self):
        #deals the cards in the shuffled deck to the selected number of players.
        if self.playerNumber == 2:
            
    def show_hand(self):
        pass

        
class HumanPlayer:
    
    def __init__(self):
        
        
"""       
for j in range(4):
    for i in range(14):
        Cards(j, i+2)
"""
def main():
    cardChoice= input("How many cards do you want to play with? 34, 30, 26 ")
    cardChoice= int(cardChoice)
    playerNumber= input("How many people do you want to play with? 2, 3, 4 ")
    playerNumber=int(playerNumber)
    t = Deck(cardChoice, playerNumber)
    t.choose_cards()
    t.shuffle()
    
    
if __name__ == "__main__":
    main()
