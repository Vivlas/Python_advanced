from random import choice


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = choice(['heads', 'tails'])


def main():

    result_flip = {'heads': 0, 'tails': 0}

    n = int(input('Enter qty of coins: '))

    coins_list = [Coin() for _ in range(n)]

    for coin in coins_list:
        coin.flip()

    for coin in coins_list:
        result_flip[coin.side] += 1

    print(f"Выпало орлов, %: {(result_flip['heads']/n)*100}\nВыпало решек, %: {(result_flip['tails']/n)*100}")
