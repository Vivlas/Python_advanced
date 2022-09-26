from __future__ import annotations

# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def __str__(self) -> str:

        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __eq__(self, other_card: Card) -> bool:

        return True if self.suit == other_card.suit else False

    def __gt__(self, other_card: Card) -> bool:

        result = False

        if VALUES.index(self.value) > VALUES.index(other_card.value):

            result = True

        elif VALUES.index(self.value) == VALUES.index(other_card.value):

            if SUITS.index(self.suit) > SUITS.index(other_card.suit):

                result = True

        return result

    def __lt__(self, other_card: Card) -> bool:

        result = False

        if VALUES.index(self.value) < VALUES.index(other_card.value):

            result = True

        elif VALUES.index(self.value) == VALUES.index(other_card.value):

            if SUITS.index(self.suit) < SUITS.index(other_card.suit):

                result = True

        return result
