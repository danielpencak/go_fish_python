from Deck import Deck
from Game import Game
import random

# create new Deck and Game instances and setup shuffled deck
Deck = Deck()
deck = Deck.shuffle_deck()
Game = Game(deck)

# select who will go first
turn = Game.select_go_first()

# deal hands
Game.create_hands()
computer_hand = Game.get_computer_hand()
print(computer_hand)
player_hand = Game.get_player_hand()
print(player_hand)

# set pair counts
computer_pairs = 0
player_pairs = 0

# main game loop
while len(deck) >= 0:
    print(len(deck))
    if len(deck) == 0:
        if computer_pairs > player_pairs:
            print('Sorry, you lost.')
            break
        else:
            print('Congratulations! You won!')
            break

    if turn == 'computer':
        continue_turn = True
        while continue_turn == True:
            print(computer_hand)
            computer_guess = random.choice(computer_hand)

            print('Do you have a {}'.format(computer_guess[1]))

            print(Game.check_for_pairs(computer_guess, turn))

            if Game.check_for_pairs(computer_guess, turn):
                computer_hand = Game.get_computer_hand()
            else:
                Game.go_fish(turn)
                computer_hand = Game.get_computer_hand()
                continue_turn = False

    if turn == 'player':
        continue_turn = True
        while continue_turn == True:

            player_guess = input('Do you have a ')

            if Game.check_for_pairs(computer_guess, turn):
                computer_hand = Game.get_computer_hand
            else:
                Game.go_fish(turn)
                computer_hand = Game.get_computer_hand
                continue_turn = False

    if turn == 'computer':
        turn = 'player'
    else:
        turn = 'computer'
