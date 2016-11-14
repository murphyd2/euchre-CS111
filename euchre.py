""" Malcolm Grossman and Dylan Murphy
    CS 111 final
    Euchre game
"""

import random 
#import graphics 
class Cards:

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
    
    def __init__(self, game_type, players):
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
        self.players = players
        
        
    
    
    def get_deck(self):
        return self.deck
    def choose_cards(self):
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
        self.shuffled_deck= []
        for card in self.game_deck:
            n = random.randrange(len(self.game_deck))
            self.shuffled_deck.insert(n, card)
        self.game_deck = self.shuffled_deck 
        return self.game_deck

    def deal(self):
        #deals the four players five cards each first by dealing a round of three at a time then a round of two at a time
        players_hands = []
        for i in self.players: 
            players_hands.append([])
        for i in players_hands:
            for j in i: 
                players_hands.append(self.game_deck[:2]) 
        for i in players_hands: 
            for j in i: 
                players_hands.append(self.game_deck[:1]) 
        discard_pile = self.game_deck
        return (discard_pile, players_hands)
    
    def show_hand(self):
        pass

        

        
"""       
for j in range(4):
    for i in range(14):
        Cards(j, i+2)
"""
def main():
    cardChoice= input("How many cards do you want to play with? 34, 30, 26 ")
    cardChoice= int(cardChoice)
    playerChoice = input("how many people do you want to play with (2-4)? ")
    playerChoice = int(playerChoice) 
    t = Deck(cardChoice, playerChoice)
    t.choose_cards()
    t.shuffle()
    
    
if __name__ == "__main__":
    main()
