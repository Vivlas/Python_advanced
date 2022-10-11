from src.homework_day_2.card_dunder import Card, VALUES


def decorator_take_cards(function):
    def wrapper(*args, **kwargs):
        if args[1]:
            print(f'{args[0].name} берет карты: {", ".join(map(lambda card: card.__str__(), args[1]))}')
        else:
            print(f'{args[0].name} не берет карты')
        function(*args, **kwargs)
        print(f'{args[0].name} имеет следующие карты: {", ".join(map(lambda card: card.__str__(), args[0].cards))}')
    return wrapper


def decorator_put_min_card(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print(f'{args[0].name} кладет свою минимальную карту: {return_value}')
        return return_value
    return wrapper


def decorator_add_card(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        if return_value:
            print(f'{args[0].name} подкидывает карту: {return_value}')
        else:
            print(f'{args[0].name} не может подкинуть еще одну карту.')
        return return_value
    return wrapper


def decorator_cover_card(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        if return_value:
            print(f'{args[0].name} бьет картой: {return_value}')
        else:
            print(f'{args[0].name} не смог побить карту: {args[1]}')
        return return_value
    return wrapper


class Player:

    def __init__(self, name: str = 'Bob'):

        # TODO: добавить тип для cards
        self.name = name
        self.cards = []

    # TODO: добавить тип для cards
    def take_cards(self, cards: list):
        """"""
        self.cards.extend(cards)

    @decorator_put_min_card
    def put_min_card(self) -> Card or None:
        """"""

        if self.cards:
            min_card = min(self.cards)
            self.cards = [card for card in self.cards if not (card is min_card)]
            return min_card

    @decorator_cover_card
    def get_cover_card(self, card_for_cover: Card) -> Card or None:
        """"""

        if self.cards:

            # Карты в колоде игрока сортируются для того, чтобы всегда биться наименьшей подходящей картой
            self.cards.sort()

            for player_card in self.cards:

                if player_card.suit == card_for_cover.suit and \
                        VALUES.index(player_card.value) > VALUES.index(card_for_cover.value):
                    cover_card = player_card
                    self.cards = [card for card in self.cards if not (card is cover_card)]
                    return cover_card

    @decorator_add_card
    def add_card(self, cards_on_table: list) -> Card or None:
        """"""

        if self.cards:

            values = {card_from_table.value for card_from_table in cards_on_table}

            # Карты в колоде игрока сортируются для того, чтобы всегда подкидывать наименьшую подходящую карту
            self.cards.sort()

            for player_card in self.cards:

                if player_card.value in values:

                    add_card = player_card
                    self.cards = [card for card in self.cards if not (card is add_card)]
                    return add_card

    def show_cards(self):

        print(f'{self.name} имеет на руках карты: {", ".join(map(lambda card: card.__str__(), self.cards))}')
