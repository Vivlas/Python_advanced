from copy import deepcopy

from src.homework_day_2.card_dunder import Card
from src.homework_day_2.deck_dunder import Deck
from src.homework_day_2.player import Player


def decorator_take_more_cards(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        if return_value:
            print(f'{args[1].name} добирает карты: {", ".join(map(lambda card: card.__str__(), return_value))}')
        else:
            print(f'{args[1].name} не добирает карты.')
        return return_value
    return wrapper


def decorator_main(function):
    def wrapper(*args, **kwargs):
        print(f'\n{"=" * 20} Начало игры {"=" * 20}')
        function(*args, **kwargs)
        print(f'\n{args[0].attacker.name} победил!\n{args[0].defender.name} проиграл.')
        print(f'\n{"=" * 20} Конец игры {"=" * 20}')
    return wrapper


def decorator_one_move(function):
    def wrapper(*args, **kwargs):
        print(f'\n{"="*15} Начало хода {args[0].move_cnt} {"="*15}')
        function(*args, **kwargs)
        print(f'{"=" * 15} Конец хода {args[0].move_cnt} {"=" * 15}')
    return wrapper


class Game:

    def __init__(self, deck: Deck, attacker: Player, defender: Player, draw_cards: int = 10):

        self.deck = deepcopy(deck)
        self.attacker = deepcopy(attacker)
        self.defender = deepcopy(defender)
        # Кол-во карт у игрока на начало игры и макс кол-во, до которого он может добирать из колоды, если требуется
        self.draw_cards = draw_cards

        # Набор карт, которые игроки выложили на стол
        self.cards_on_table = []
        # Как колода "бита" в игре
        self.cards_after_cover = []
        # Номер хода
        self.move_cnt = 1

    def defender_cover(self, card: Card):

        cover_card = self.defender.get_cover_card(card)

        # Если отбивающий отбил карту, то далее атакующий может подкинуть еще.
        if cover_card:
            self.cards_on_table.append(cover_card)
            # Атакующий пытается подбросить еще карту.
            new_card = self.attacker.add_card(self.cards_on_table)

            if new_card:
                self.cards_on_table.append(new_card)
                self.defender_cover(new_card)
            else:
                self.cards_after_cover.extend(self.cards_on_table)
                self.cards_on_table.clear()
        else:
            self.defender.take_cards(self.cards_on_table)
            print(f'{self.defender.name} взял со стола: '
                  f'{", ".join(map(lambda card: card.__str__(), self.cards_on_table))}')
            self.cards_on_table.clear()

    @decorator_take_more_cards
    def take_more_cards(self, player: Player):

        more_cards = []

        if self.deck.cards and ((player_cards_cnt := len(player.cards)) < self.draw_cards):
            more_cards.extend(self.deck.draw(self.draw_cards - player_cards_cnt))

        return more_cards

    @decorator_one_move
    def one_move(self):

        self.attacker.show_cards()
        self.defender.show_cards()

        # Ведем счетчик карт в бите
        cards_after_cover_cnt = len(self.cards_after_cover)

        card = self.attacker.put_min_card()

        self.cards_on_table.append(card)

        self.defender_cover(card)

        if len(self.cards_after_cover) > cards_after_cover_cnt:
            print(f'{self.defender.name} cмог отбиться!')
        else:
            print(f'{self.defender.name} не cмог отбиться.')

        #  Атакующий добирает карты из колоды, если необходимо
        self.attacker.take_cards(self.take_more_cards(self.attacker))

        #  Отбивающий берет карты из колоды, если необходимо
        self.defender.take_cards(self.take_more_cards(self.defender))

        # Если кол-во карт в бите увеличилось, то значит один из игроков отбился и игроки меняются местами
        if len(self.cards_after_cover) > cards_after_cover_cnt:
            self.attacker, self.defender = self.defender, self.attacker

    @decorator_main
    def main(self):

        self.attacker.take_cards(self.deck.draw(self.draw_cards))
        self.defender.take_cards(self.deck.draw(self.draw_cards))

        while self.attacker.cards:

            self.one_move()

            self.move_cnt += 1
