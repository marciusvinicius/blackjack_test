import unittest
from main import Deck, Card


class BlackJacTest(unittest.TestCase):
    def test_my_deck(self):
        deck = Deck().build()
        right_deck = []
        for y in range(1, 4):
            for x in range(1, 13):
                right_deck.append(
                    Card(value=x, suit=y)
                )

        self.assertEqual(deck, right_deck)

    def test_shuffle_deck(self):
        deck = Deck().build()
        s_deck = Deck.shuffle(deck)
        self.assertFalse(deck == s_deck)
        s_deck_2 = Deck.shuffle(deck)
        self.assertFalse(s_deck_2 == s_deck)
        self.assertEqual(len(s_deck_2), len(s_deck))


if __name__ == "___main__":
    unittest.main()