from Deck import Deck
import random

class Game(Deck):
    def __init__(self, deck, player_hand = [], computer_hand = []):
        self.deck = deck
        self.player_hand = player_hand
        self.computer_hand = computer_hand

    def reset(self,  deck, player_hand = [], computer_hand = []):
        self.deck = deck
        self.player_hand = player_hand
        self.computer_hand = computer_hand

    def get_deck(self):
        return self.deck

    def get_player_hand(self):
        return self.player_hand

    def get_computer_hand(self):
        return self.computer_hand

    def set_deck(self, deck):
        self.deck = deck

    def set_player_hand(self, hand):
        self.player_hand = hand

    def set_computer_hand(self, hand):
        self.computer_hand = hand

    def select_go_first(self):
        players = ['player', 'computer']

        return random.choice(players)

    def deal_card(self):
        return super(Game, self).deal_card()

    def create_hands(self):
        for card_count in range(0, 5):
            self.player_hand.append(self.deal_card())
            self.computer_hand.append(self.deal_card())

    def check_for_pairs(self, card_to_check, player):
        if player == 'computer':
            for card in self.player_hand:
                if card[1] == card_to_check[1]:
                    self.player_hand.remove(card)
                    self.computer_hand.remove(card_to_check)
                    return True
            return False
        else:
            for card in self.computer_hand:
                if card[1] == card_to_check[1]:
                    self.computer_hand.remove(card)
                    self.player_hand.remove(card_to_check)
                    return True
            return False

    def refill_hand(self, player):
        if player == 'computer':
            for card_count in range (0, len(self.player_hand)):
                self.computer_hand.append(self.deal_card())

            return self.computer_hand
        else:
            for card_count in range (0, len(self.computer_hand)):
                self.player_hand.append(self.deal_card())

            return self.player_hand

    def go_fish(self, player):
        if player == 'computer':
            dealt_card = self.deal_card()
            pair_check = self.check_for_pairs(dealt_card, player)

            if pair_check:
                if len(self.computer_hand) == 0:
                    self.refill_hand(player)
                self.go_fish(player)
        else:
            dealt_card = self.deal_card()
            pair_check = self.check_for_pairs(dealt_card, player)

            if pair_check:
                if len(self.player_hand) == 0:
                    self.refill_hand(player)
                self.go_fish(player)
