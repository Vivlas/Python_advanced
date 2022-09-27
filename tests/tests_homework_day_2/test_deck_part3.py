from src.homework_day_2.deck_dunder import Deck
from src.homework_day_2.card_dunder import Card


def test_card_dunder():

    card1 = Card('10', 'Hearts')
    card2 = Card('A', 'Diamonds')

    # Проверка на равенство. Карты не равны
    assert not card1 == card2

    # Проверка на неравенство. card1 меньше card2
    assert card1 < card2
    assert not card2 < card1

    assert card2 > card1
    assert not card1 > card2

    card1 = Card('6', 'Clubs')
    card2 = Card('6', 'Clubs')

    # Проверка на равенство. Карты равны
    assert card1 == card2

    assert not card1 < card2
    assert not card2 < card1

    assert not card2 > card1
    assert not card1 > card2

    print(card1)


def test_deck_dunder():

    deck = Deck()

    print(deck)
