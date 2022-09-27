from src.homework_day_2.deck import Deck


def test_more_and_less():

    deck = Deck()

    # Для начала протестируем сравнение карт на отсортированной колоде карт
    # Карты одной масти. card2 больше по значению, чем card1
    card1 = deck.cards[0]
    card2 = deck.cards[1]

    assert card2.more(card1)
    assert card1.less(card2)

    # Карты разных мастей. card2 больше по значению, чем card1
    card1 = deck.cards[0]
    card2 = deck.cards[13]

    assert card2.more(card1)
    assert card1.less(card2)

    # Карты одинаковых мастей. card2 и card1 равны по значению
    card1 = deck.cards[10]
    card2 = deck.cards[10]

    assert not card2.more(card1)
    assert not card2.less(card1)

    # card2 и card1 равны по значению. card2 больше по масти, чем card1
    card1 = deck.cards[13]
    card2 = deck.cards[26]

    assert card1.value == card2.value
    assert card2.more(card1)
    assert card1.less(card2)

    # Тусуем колоду. Возьмем карты и протестируем методы

    deck.shuffle()
    print(deck.show())
    # Берем две карты из колоды
    card1, card2 = deck.draw(2)

    # Тестируем методы .less() и .more()
    if card1.more(card2):
        print(f"{card1.to_str()} больше {card2.to_str()}")
    if card1.less(card2):
        print(f"{card1.to_str()} меньше {card2.to_str()}")
