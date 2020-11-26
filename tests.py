# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:01:46 2020

@author: dshlyapnikov
"""
import unittest
import cards

class TestCards(unittest.TestCase):
    def test_draw_and_card_nums(self):
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
    
    
    