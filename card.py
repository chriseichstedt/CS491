#Homework 2, CS-491, Christopher Eichstedt
#Code is implemented using a tutorial, listed as resource.
#Resource: https://medium.com/@samarakoon.gayan/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit