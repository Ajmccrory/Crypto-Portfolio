"""Program to hold list of currencies owned.

Author: AJ McCrory
Version: 4.9.2023
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
from portfolio_coin import PortfolioCoin
from market import Market


class Portfolio:
    """Portfolio object.

    Attributes:
        _coins (PortfolioCoin): PortfolioCoin objects representing coins owned.
        _market (Market): Market object showing market data.
    """

    def __init__(self, _coins, _market):
        pass

    def add_coin(self, coin_desc):
        return False

    def add_coins(self, coins_desc):
        return False

    def get_original_value(self):
        return 0.0

    def get_current_value(self):
        return 0.0

    def get_gain_loss(self):
        return 0.0

    def get_best_earner(self):
        pass

    def get_worst_earner(self):
        pass

    def get_coin(self, symbol=''):
        pass

    def find_new_coin(self, search_term=''):
        """Function to find new coins.

        Args:
            search_term (str): Given search term to find.

        Returns:
            new_coin (str): New coin value.
        """
        pass

    def __str__(self):
        return ''
