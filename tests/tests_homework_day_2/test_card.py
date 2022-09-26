from src.homework_day_2.card import Card


def test_create_card():
    card1 = Card('10', 'Hearts')
    card2 = Card('A', 'Diamonds')

    assert card1.value == '10'
    assert card1.suit == 'Hearts'

    assert card2.value == 'A'
    assert card2.suit == 'Diamonds'

    # Выведем карты на экран в виде: 10♥ и A♦
    print(card1.to_str())
    print(card2.to_str())


def test_equal_suit():

    card1 = Card('10', 'Hearts')
    card2 = Card('A', 'Diamonds')

    assert card1.suit != card2.suit

    # Проверим, одинаковые ли масти у карт
    if card1.equal_suit(card2):
        print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
    else:
        print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

    card3 = Card('10', 'Clubs')
    card4 = Card('A', 'Clubs')

    assert card3.suit == card4.suit

    # Проверим, одинаковые ли масти у карт
    if card3.equal_suit(card4):
        print(f"У карт: {card3.to_str()} и {card4.to_str()} одинаковые масти")
    else:
        print(f"У карт: {card3.to_str()} и {card4.to_str()} разные масти")