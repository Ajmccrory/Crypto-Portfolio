"""Program to hold list of currencies owned.

Author: AJ McCrory
Version: 4.9.2023
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
from portfolio_coin import PortfolioCoin


class Portfolio:
    """Portfolio object.

    Attributes:
        _coins (PortfolioCoin): PortfolioCoin objects representing coins owned.
        _market (Market): Market object showing market data.
    """

    def __init__(self, market):
        self._coins = []
        self._market = market

    def add_coin(self, coin_tuple):
        # unpack
        symbol, price, amount = coin_tuple
        # validate
        coin = self._market.get_coin(symbol)
        if coin is None:
            return False
        if price is None or price <= 0 or price > 250000:
            return False
        if amount is None or amount <= 0 or amount > 1000000:
            return False
        pc = PortfolioCoin(coin, price, amount)
        self._coins.append(pc)
        return True

    def add_coins(self, coins_desc):
        for cd in coins_desc:
            self.add_coin(cd)

    def get_original_value(self):
        total = 0.0
        for coin in self._coins:
            total += coin.get_total_price_paid()
        return total

    def get_current_value(self):
        total = 0.0
        for coin in self._coins:
            total += coin.get_current_value()
        return total

    def get_gain_loss(self):
        return self.get_current_value() - self.get_original_value()

    def get_best_earner(self):
        if len(self._coins) < 1:
            return None
        top = self._coins[0].get_current_value()
        pos = self._coins
        for i in range(len(self._coins)):
            if self._coins[i].get_current_value() > top:
                top = self._coins[i].get_current_value()
                pos = self._coins[i]
        return pos

    def get_worst_earner(self):
        if len(self._coins) < 1:
            return None
        worst = self._coins[0].get_current_value()
        pos = self._coins
        for i in range(len(self._coins)):
            if self._coins[i].get_current_value() < worst:
                worst = self._coins[i].get_current_value()
                pos = self._coins[i]
        return pos

    def get_coin(self, symbol=''):
        if len(self._coins) < 1:
            return None
        for coin in self._coins:
            str = coin.__str__()
            if symbol in str:
                return coin

    def find_new_coin(self, search_term=''):
        pass

    def __str__(self):
        a = f"Portfolio contains {len(self._coins)} cryptocurrencies.\n"
        b = f"The purchase cost of the portfolio was ${self.get_original_value():.2f} "
        c = f"and the current value is ${self.get_current_value():.2f}.\n"
        result = a + b + c
        # TODO: append PortfolioCoin strings to result
        for coin in self._coins:
            result += f'{coin.__str__()}\n'
        return result
