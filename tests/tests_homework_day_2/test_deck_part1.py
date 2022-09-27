from src.homework_day_2.deck import Deck


def test_deck():

    deck = Deck()

    assert len(deck.cards) == 52

    assert deck.cards[0].suit == 'Spades'
    assert deck.cards[0].value == '2'

    assert deck.cards[12].suit == 'Spades'
    assert deck.cards[12].value == 'A'

    assert deck.cards[50].suit == 'Hearts'
    assert deck.cards[50].value == 'K'


def test_show():

    deck = Deck()

    print(deck.show())


def test_draw():

    deck = Deck()

    assert len(deck.cards) == 52

    # Берем первые 5 карт из отсортированной колоды
    hand = deck.draw(5)

    assert len(hand) == 5

    assert hand[0].value == 'A'
    assert hand[0].suit == 'Hearts'

    assert hand[1].value == 'K'
    assert hand[1].suit == 'Hearts'

    assert hand[2].value == 'Q'
    assert hand[2].suit == 'Hearts'

    assert hand[3].value == 'J'
    assert hand[3].suit == 'Hearts'

    assert hand[4].value == '10'
    assert hand[4].suit == 'Hearts'

    # Проверим оставшиеся карты в коллоде
    assert len(deck.cards) == 47

    assert deck.cards[0].value == '2'
    assert deck.cards[0].suit == 'Spades'

    assert deck.cards[46].value == '9'
    assert deck.cards[46].suit == 'Hearts'

    # Попробуем взять из колоды больше карт, чем там есть. По реализованной логике получим только оставшиеся карты.
    hand = deck.draw(52)

    assert len(hand) == 47
    assert len(deck.cards) == 0


def test_shuffle():

    deck = Deck()

    assert len(deck.cards) == 52

    deck.shuffle()

    assert len(deck.cards) == 52

    # Посмотрим состав колоды
    print(deck.show())

