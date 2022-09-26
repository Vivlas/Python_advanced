from src.homework_day_2.player import Player
from src.homework_day_2.deck_dunder import Deck
from src.homework_day_2.card_dunder import Card


def test_player():

    player = Player()

    assert len(player.cards) == 0
    assert player.name == 'Bob'

    player = Player('Mark')
    player.cards = [Card('4', 'Clubs')]

    assert player.name == 'Mark'
    assert player.cards[0].suit == 'Clubs'
    assert player.cards[0].value == '4'


def test_take_cards():

    player = Player()

    deck = Deck()

    player.take_cards(deck.draw(10))

    assert len(player.cards) == 10
    assert player.cards[0].value == '2'
    assert player.cards[0].suit == 'Spades'
    assert player.cards[9].value == 'J'
    assert player.cards[9].suit == 'Spades'

    assert len(deck.cards) == 42


def test_put_min_card():

    player_1 = Player()

    deck = Deck()

    player_1.take_cards(deck.draw(10))

    assert len(player_1.cards) == 10

    min_card = player_1.put_min_card()

    assert min_card.value == '2'
    assert min_card.suit == 'Spades'
    assert len(player_1.cards) == 9

    player_2 = Player()

    # Проверим, что самая маленькая карта выбирается корректно, если карты одинаковые по значению.
    cards = [Card('4', 'Clubs'), Card('4', 'Spades'), Card('4', 'Hearts'), Card('4', 'Diamonds')]

    player_2.take_cards(cards)

    assert len(player_2.cards) == 4

    min_card = player_2.put_min_card()

    assert min_card.value == '4'
    assert min_card.suit == 'Spades'
    assert len(player_2.cards) == 3

    player_3 = Player()

    # Проверим, что самая маленькая карта выбирается корректно, если карты одинаковые по значению.
    cards = [Card('10', 'Clubs'), Card('A', 'Spades'), Card('2', 'Clubs'), Card('4', 'Diamonds')]

    player_3.take_cards(cards)

    assert len(player_3.cards) == 4

    min_card = player_3.put_min_card()

    assert min_card.value == '2'
    assert min_card.suit == 'Clubs'
    assert len(player_3.cards) == 3


def test_cover_card():

    card = Card('4', 'Clubs')

    player = Player()

    # Добавим игроку карты, среди которых нет такой, которая побьет карту другого игрока
    player.take_cards([Card('J', 'Hearts'), Card('3', 'Clubs'), Card('6', 'Spades')])

    # Ожидаем, что игрок заберет карту со стола
    cover_card = player.get_cover_card(card)

    assert cover_card is None

    # Теперь походим такой картой, которую игрок сможет отбить

    card = Card('5', 'Hearts')

    # Ожидаем, что игрок побьет карту
    cover_card = player.get_cover_card(card)

    assert cover_card.value == 'J'
    assert cover_card.suit == 'Hearts'


def test_add_card():

    player = Player()

    player.take_cards([Card('J', 'Hearts'), Card('3', 'Clubs'), Card('6', 'Spades'), Card('7', 'Spades')])

    cars_on_table = [Card('10', 'Clubs'), Card('3', 'Spades')]

    card = player.add_card(cars_on_table)

    assert card.value == '3'
    assert card.suit == 'Clubs'

    card = player.add_card(cars_on_table)

    assert card is None


