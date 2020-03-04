import random
import copy

Suit = {
    1: "Spades",
    2: "Hearts",
    3: "Diamonds",
    4: "Clubs"
}


class Card():
    def __init__(self, value, suit):
        super().__init__()
        self.value = value
        self.suit = suit

    def __eq__(self, other_card):
        if self.value == other_card.value and self.suit == other_card.suit:
            return True
        return False


class Deck():
    cards = []

    @classmethod
    def build(cls):
        for y in range(1, 4):
            for x in range(1, 13):
                cls.cards.append(
                    Card(value=x, suit=y)
                )
        return cls.cards

    def __eq__(self, other_deck):
        cards = sorted(self.cards)
        other_cards = sorted(other_deck.cards)
        for c, oc in zip(cards, other_cards):
            if c != oc:
                return False
        return True

    @classmethod
    def shuffle(cls, deck):
        new_deck = []
        old_deck = copy.copy(deck)
        while len(old_deck) - 1 > 0:
            key = random.randint(0, len(old_deck) -1)
            new_deck.append(old_deck.pop(key))
        return new_deck