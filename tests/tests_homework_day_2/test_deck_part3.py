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


def test_deck_dunder_draw():
    deck = Deck()

    assert len(deck.cards) == 52

    # Берем первые 5 карт из отсортированной колоды
    hand = deck.draw(5)

    assert len(hand) == 5

    assert hand[0].value == '2'
    assert hand[0].suit == 'Spades'

    assert hand[1].value == '3'
    assert hand[1].suit == 'Spades'

    assert hand[2].value == '4'
    assert hand[2].suit == 'Spades'

    assert hand[3].value == '5'
    assert hand[3].suit == 'Spades'

    assert hand[4].value == '6'
    assert hand[4].suit == 'Spades'

    # Проверим оставшиеся карты в коллоде
    assert len(deck.cards) == 47

    assert deck.cards[0].value == '7'
    assert deck.cards[0].suit == 'Spades'

    assert deck.cards[46].value == 'A'
    assert deck.cards[46].suit == 'Hearts'

    # Попробуем взять из колоды больше карт, чем там есть. По реализованной логике получим только оставшиеся карты.
    hand = deck.draw(52)

    assert len(hand) == 47
    assert len(deck.cards) == 0


def test_iteration():
    deck = Deck()

    for card in deck:
        print(card)

    print('='*100)
    deck.draw(10)

    for card in deck:
        print(card)


def test_get_item():
    deck = Deck()

    card = deck[6]

    assert card.value == '8'
    assert card.suit == 'Spades'

    print(deck[6])

