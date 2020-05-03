#Homework 2, CS-491, Christopher Eichstedt
#Code is implemented using a tutorial, listed as resource.
#Resource: https://medium.com/@samarakoon.gayan/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

import random
import card as user_card

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = user_card.Card(suit,rank)
                self.deck.append(new_card)

    def __str__(self):
        deck_comp = ''
        for user_card in self.deck:
            deck_comp += '\n' + user_card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card