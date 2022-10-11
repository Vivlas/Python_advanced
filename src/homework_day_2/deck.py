import random

from src.homework_day_2.card import Card, SUITS, VALUES


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def show(self):

        return f'deck[{len(self.cards)}]: ' + ', '.join(map(lambda card: card.to_str(), self.cards))

    def draw(self, x):
        out_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return out_cards

    def shuffle(self):

        random.shuffle(self.cards)
