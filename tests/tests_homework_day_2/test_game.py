from src.homework_day_2.player import Player
from src.homework_day_2.deck_dunder import Deck
from src.homework_day_2.game import Game


def test_game_main():

    deck = Deck()
    deck.shuffle()

    player_1 = Player('Bob')
    player_2 = Player('Mark')

    game_1 = Game(deck, player_1, player_2)

    game_1.main()

    assert len(game_1.attacker.cards) == 0
    assert len(game_1.deck.cards) == 0
    assert (len(game_1.cards_after_cover) + len(game_1.defender.cards)) == 52

    # Запустим игру еще раз с теми же входящими данными. Ожидаем, что исход будет такой же.
    game_2 = Game(deck, player_1, player_2)

    game_2.main()

    assert len(game_2.attacker.cards) == 0
    assert len(game_2.deck.cards) == 0
    assert (len(game_2.cards_after_cover) + len(game_2.defender.cards)) == 52

    # Проверим совпадение результатов
    assert game_1.cards_after_cover == game_2.cards_after_cover
    assert game_1.defender.cards == game_2.defender.cards
