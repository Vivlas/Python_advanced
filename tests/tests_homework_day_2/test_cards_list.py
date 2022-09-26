from src.homework_day_2.card import Card, VALUES


def test_hearts_cards():

    hearts_cards = [Card(value, 'Hearts') for value in VALUES]

    for index, card in enumerate(hearts_cards):
        assert card.value == VALUES[index]
        assert card.suit == 'Hearts'


def test_diamonds_cards():

    diamonds_cards = [Card(value, 'Diamonds') for value in VALUES]

    for index, card in enumerate(diamonds_cards):
        assert card.value == VALUES[index]
        assert card.suit == 'Diamonds'


def test_print_hearts_cards():

    hearts_cards = [Card(value, 'Hearts') for value in VALUES]

    print(', '.join(map(lambda card: card.to_str(), hearts_cards)))
