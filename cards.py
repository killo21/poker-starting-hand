# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:30:27 2020

@author: dshlyapnikov
"""
import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def getSuit(self):
        return self.suit
    
    def getVal(self):
        return self.val
    
class Deck:
    def __init__(self):
        self.cardCount = 52
        suits = ["clubs", "diamonds", "hearts", "spades"]
        self.cards = []
        for suit in suits:
            for val in range(1, 14):
                c = Card(suit, val)
                self.cards.append(c)
        random.shuffle(self.cards)
    
    def getCount(self):
        return self.cardCount
    
    def draw(self):
        card = self.cards[0]
        self.cards = self.cards[1:]
        self.cardCount -= 1
        return card
        
