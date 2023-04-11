"""Program to create a PortfolioCoin object.

Author: AJ McCrory
Version: 4.9.2023
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
from coin import Coin


class PortfolioCoin:
    """PorfolioCoin Object.

    Attributes:
        _price_paid_per_coin (float): The price paid per coin.
        _amount_owned (float): The amount owned of the specific coin.
        _coin (Coin): The coin object from coin.py
    """

    def __init__(self, _coin=Coin(), _price_paid_per_coin=0.0, _amount_owned=0.0):
        self.price_paid = _price_paid_per_coin
        self.amount_owned = _amount_owned
        self.coin = _coin

    def get_coin(self):
        return self.coin

    def get_price_paid_per_coin(self):
        return self.price_paid

    def get_amount_owned(self):
        return self.amount_owned

    def set_coin(self, coin=Coin()):
        self.coin = coin

    def set_price_paid_per_coin(self, price):
        self.price_paid = float(price)

    def set_amount_owned(self, amount_owned):
        self.amount_amount = float(amount_owned)

    def get_total_price_paid(self):
        """Function to return the total price paid.

        Returns:
            total (float): Float value representing total price.
        """
        total = self.price_paid * self.amount_owned
        return total

    def get_current_value(self):
        """Function to return tthe current value of the coin.

        Returns:
            cv (float): Float value representing current value.
        """
        current_price = Coin.get_price(self.coin)
        cv = current_price * self.amount_owned
        return cv

    def get_current_gain_loss(self):
        """Function to return the current gain/loss of the coin.

        Returns:
            cgl (float): Float value representing the current gain/loss of the coin.
        """
        tpp = PortfolioCoin.get_total_price_paid(self)
        current_price = PortfolioCoin.get_current_value(self)
        cgl = current_price - tpp
        return cgl

    def __str__(self):
        ao = self.amount_owned
        symb = self.coin.symbol
        pp = self.price_paid
        str_1 = f'{ao:.4f} {symb} coins were purchased at {pp:.10f} per coin.'
        return f'{str_1}{Coin.__str__(self.coin)}'

    def __eq__(self, other):
        if isinstance(other, PortfolioCoin):
            return (self.coin == other.coin) and (self.amount_owned == other.amount_owned)
        return False
