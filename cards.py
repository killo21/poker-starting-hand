# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:30:27 2020

@author: dshlyapnikov
"""
import random

class Card:
    def __init__(self, suit, val):
        """Create card of suit suit [str] and value val [int] 1-13
            1 - Ace, 2 - 2, 3 - 3,..., 11 - Jack, 12 - Queen, 13 - King
            suit can be "clubs", "diamonds", "hearts", "spades"."""
        assert type(suit) is str
        assert suit == "clubs" or suit == "diamonds" or suit == "hearts" or suit == "spades"
        assert type(val) is int
        assert val > 0 and val < 14
        
        self.suit = suit
        self.val = val
        
    def getSuit(self):
        """A card's suit. Can be "clubs", "diamonds", "hearts", "spades"."""
        return self.suit
    
    def getVal(self):
        """A card's value. [int] 1-13. 
            1 - Ace, 2 - 2, 3 - 3,..., 11 - Jack, 12 - Queen, 13 - King"""
        return self.val
    
    def getShortHand(self):
        """Short hand [str] notation to represent a card. The first character 
            is the chard's value 1-13, J, Q, K, or A. The second char is the
            card's suit C - clubs, D - diamonds, H - hearts, S - spades."""
        result = ""
        if self.val == 1:
            result = "A"
        elif self.val == 11:
            result = "J"
        elif self.val == 12:
            result = "Q"
        elif self.val == 13:
            result = "K"
        else:
            result = str(self.val)
        result = result + self.suit[0].capitalize()
        return result
    
class Deck:
    def __init__(self):
        """Creates a shuffled deck of 52 [card] objects."""
        self.cardCount = 52
        suits = ["clubs", "diamonds", "hearts", "spades"]
        self.cards = []
        for suit in suits:
            for val in range(1, 14):
                c = Card(suit, val)
                self.cards.append(c)
        random.shuffle(self.cards)
    
    def getCount(self):
        """The [int] number of cards in the deck. Between 0-52 inclusive."""
        return self.cardCount
    
    def draw(self):
        """The first [card] in the deck. Removed from the deck without replacement."""
        card = self.cards[0]
        self.cards = self.cards[1:]
        self.cardCount -= 1
        return card
        
