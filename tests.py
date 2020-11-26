# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:01:46 2020

@author: dshlyapnikov
"""
import unittest
import cards

class TestCards(unittest.TestCase):
    def test_card(self):
        card = cards.Card("spades", 11)
        cardK = cards.Card("hearts", 13)
        cardQ = cards.Card("diamonds", 12)
        cardA = cards.Card("clubs", 1)
        cardNum = cards.Card("hearts", 5)
        self.assertEqual(card.getSuit(), "spades") #suit should have be set to spades
        self.assertEqual(card.getVal(), 11) #value should have been set to 11
        self.assertEqual(card.getShortHand(), "JS") #shorthand should convert 11 value to J for Jack
        self.assertEqual(cardK.getShortHand(), "KH") #shorthand should convert 13 value to K for King
        self.assertEqual(cardQ.getShortHand(), "QD") #shorthand should convert 12 value to Q for Queen
        self.assertEqual(cardA.getShortHand(), "AC") #shorthand should convert 1 value to A for Ace
        self.assertEqual(cardNum.getShortHand(), "5H") #shorthand should leave the 5 value
    def test_deck(self):
        d1 = cards.Deck()
        self.assertEqual(d1.getCount(), 52) #Deck should have 52 cards
        cardValsDrawn = {}
        cardSuitsDrawn = {}
        while d1.getCount() > 0:
            card = d1.draw()
            if card.getSuit() not in cardSuitsDrawn:
                cardSuitsDrawn[card.getSuit()] = 1
            else:
                cardSuitsDrawn[card.getSuit()] += 1
            
            if card.getVal() not in cardValsDrawn:
                cardValsDrawn[card.getVal()] = 1
            else:
                cardValsDrawn[card.getVal()] += 1
        
        for i in cardValsDrawn:
            self.assertEqual(cardValsDrawn[i], 4) #There should be 4 of each card value in a deck
        for i in cardSuitsDrawn:
            self.assertEqual(cardSuitsDrawn[i], 13) #There should be 13 cards of each suit


if __name__ == '__main__':
    unittest.main()
    
    
    