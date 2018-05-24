import random

class Deck:
    'represents a deck of 52 cards'

    def __init__(self):
        self.deck = []

    def shuffle_deck(self):
        'returns a shuffled deck'

        suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
        ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

        for suit in suits:
            for rank in ranks:
                card = []
                card.append(suit)
                card.append(rank)
                self.deck.append(card)

        random.shuffle(self.deck)

        return self.deck

    def deal_card(self):
        'returns the dealt card'

        dealt_card = self.deck.pop()

        return dealt_card
