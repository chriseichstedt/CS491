#Homework 2, CS-491, Christopher Eichstedt
#Code is implemented using a tutorial, listed as resource.
#Resource: https://medium.com/@samarakoon.gayan/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83

import deck as user_deck
import hand as user_hand

playing = True

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input ("Enter 'h' to Hit or Enter 's' to Stand: \n")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            playing = False

        else:
            print("Incorrect input, please try again!")
            continue
        break

def show_some(player, dealer):
    print("Dealer's Hand:")
    print(" <card hidden> ")
    print ('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("---------------------------------------------")

def show_all(player, dealer):
    print("Dealer's Hand:", *dealer.cards, sep='\n')
    print("\nDealer's Total:", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("\nPlayer's Total:", player.value)
    print("---------------------------------------------")

def player_busts(player,dealer):
    print("Player busts!")

def player_wins(player,dealer):
    print("Player wins!")

def dealer_busts(player, dealer):
    print("Dealer busts!")

def dealer_wins(player,dealer):
    print("Dealer wins!")

def push(player,dealer):
    print("No winner, game is a push!")




if __name__== '__main__':
    while True:
        print("---------------------------------------------")
        print("Welcome to the CS-491 Casino! \nThe game is Blackjack. \n\n---Rules--- \nTry to score any value under or equal to 21. \nDealer will continue to hit until they reach a value above 16. \n\n***Lets play!***")

        deck = user_deck.Deck()
        deck.shuffle()

        player_hand = user_hand.Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = user_hand.Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        show_some(player_hand,dealer_hand)

        while playing:
            hit_or_stand(deck,player_hand)

            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand)

            else:
                push(player_hand,dealer_hand)

        new_game = input("\nPlayer another hand?\nEnter 'y' for Yes: \n")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Selection was not 'y', exiting game. Take care!")
            break