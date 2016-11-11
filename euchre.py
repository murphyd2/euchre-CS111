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
        
        for i in range(len(self.game_deck)):
            self.shuffled_deck.append(0)
        for card in self.game_deck:
            n = random.randrange(len(self.game_deck))
            while self.shuffled_deck[n] != 0:
                n= random.randrange(len(self.game_deck))
            self.shuffled_deck.insert(n, card)
            p=0
            while self.shuffled_deck[p] == 0:
                self.shuffled_deck[p] = []
                p += 1
            for j in self.shuffled_deck:
                print(j)
        return self.shuffled_deck
                
                
        # function that finds a randint btwn 0- (34) 52 and inserts the current card 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
            
        
        
        
    def deal(self):
        pass
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
    t = Deck(cardChoice)
    t.choose_cards()
    t.shuffle()
    
    
if __name__ == "__main__":
    main()