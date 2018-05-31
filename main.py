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
print('computer hand', computer_hand)
player_hand = Game.get_player_hand()
print('player hand', player_hand)

Game.check_for_pairs('computer')
Game.check_for_pairs('player')
print('computer hand', computer_hand)
print('player hand', player_hand)


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
            computer_guess = random.choice(computer_hand)

            print('Do you have a {}'.format(computer_guess[1]))

            pair_check = Game.check_for_pairs(turn, computer_guess[1])

            if pair_check == True:
                computer_hand = Game.get_computer_hand()
            elif pair_check == False:
                Game.go_fish(turn)
                Game.check_for_pairs('computer')
                computer_hand = Game.get_computer_hand()
                continue_turn = False

            print('computer hand', computer_hand)
            print('player hand', player_hand)

    if turn == 'player':
        continue_turn = True

        while continue_turn == True:
            player_guess = input('Do you have a ')

            pair_check = Game.check_for_pairs(turn, player_guess)

            if pair_check == True:
                player_hand = Game.get_player_hand()
            elif pair_check == False:
                Game.go_fish(turn)
                Game.check_for_pairs('player')
                player_hand = Game.get_player_hand()
                continue_turn = False
            print('computer hand', computer_hand)
            print('player hand', player_hand)

    if turn == 'computer':
        turn = 'player'
    else:
        turn = 'computer'
