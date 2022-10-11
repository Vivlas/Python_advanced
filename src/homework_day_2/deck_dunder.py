import random

from src.homework_day_2.card_dunder import Card, SUITS, VALUES


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]
        self.max = len(self.cards)

    def __str__(self):

        return f'deck[{len(self.cards)}]: ' + ', '.join(map(lambda card: card.__str__(), self.cards))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.cards[self.n]
            self.n += 1
            return result
        else:
            self.n = 0
            raise StopIteration

    def __getitem__(self, item):
        return self.cards[item]

    def draw(self, x):
        out_cards = self.cards[:x]
        self.cards = self.cards[x:]
        self.max = len(self.cards)
        return out_cards

    def shuffle(self):

        random.shuffle(self.cards)
