#Homework 2, CS-491, Christopher Eichstedt

import unittest
import card as user_card
import hand as user_hand
import deck as user_deck

class IntegrationTest(unittest.TestCase):
    def test_player_busts(self):
        deck = user_deck.Deck()
        deck.shuffle()

        player_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Ace")
        player_hand.add_card(test_card)
        test_card = user_card.Card("Hearts","King")
        player_hand.add_card(test_card)
        test_card = user_card.Card("Hearts","Queen")
        player_hand.add_card(test_card)

        dealer_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Nine")
        dealer_hand.add_card(test_card)
        test_card = user_card.Card("Clubs","Nine")
        dealer_hand.add_card(test_card)

        self.assertGreater(player_hand.value,21)
        pass

    def test_player_wins(self):
        deck = user_deck.Deck()
        deck.shuffle()

        player_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Ace")
        player_hand.add_card(test_card)
        test_card = user_card.Card("Hearts","King")
        player_hand.add_card(test_card)

        dealer_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Nine")
        dealer_hand.add_card(test_card)
        test_card = user_card.Card("Clubs","Nine")
        dealer_hand.add_card(test_card)

        self.assertGreater(player_hand.value,dealer_hand.value)
        self.assertLessEqual(player_hand.value,21)

    def test_dealer_wins(self):
        deck = user_deck.Deck()
        deck.shuffle()

        player_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Nine")
        player_hand.add_card(test_card)
        test_card = user_card.Card("Clubs","Nine")
        player_hand.add_card(test_card)

        dealer_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Ace")
        dealer_hand.add_card(test_card)
        test_card = user_card.Card("Hearts","King")
        dealer_hand.add_card(test_card)

        self.assertLess(player_hand.value,dealer_hand.value)
        self.assertLessEqual(dealer_hand.value,21)

    def test_push(self):
        deck = user_deck.Deck()
        deck.shuffle()

        player_hand = user_hand.Hand()
        test_card = user_card.Card("Hearts","Ace")
        player_hand.add_card(test_card)
        test_card = user_card.Card("Hearts","King")
        player_hand.add_card(test_card)

        dealer_hand = user_hand.Hand()
        test_card = user_card.Card("Clubs","Ace")
        dealer_hand.add_card(test_card)
        test_card = user_card.Card("Clubs","King")
        dealer_hand.add_card(test_card)

        self.assertEqual(player_hand.value,dealer_hand.value)
        self.assertLessEqual(player_hand.value,21)
        self.assertLessEqual(dealer_hand.value,21)

if __name__ == '__main__':
    unittest.main() 