import random

from src.homework_day_2.card import Card, SUITS, VALUES


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def __str__(self):

        return f'deck[{len(self.cards)}]: ' + ', '.join(map(lambda card: card.to_str(), self.cards))

    def draw(self, x):

        # Берем x карт из колоды. Если карт в колоде меньше, чем x, то берем все, что есть.
        card_range = range(x) if (x <= (n := len(self.cards))) else range(n)

        return [self.cards.pop() for _ in card_range]

    def shuffle(self):

        random.shuffle(self.cards)
