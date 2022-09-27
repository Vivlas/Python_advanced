from src.homework_day_2.card import Card, VALUES, SUITS


def test_add_all_cards():

    cards = [Card(value, suit) for value in VALUES for suit in SUITS]

    assert len(cards) == 52


def test_print_all_cards():

    cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    print(f'cards[{len(cards)}]: ' + ', '.join(map(lambda card: card.to_str(), cards)))
