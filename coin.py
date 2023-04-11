"""Coin Class.

Author: AJ McCrory
Version: 4.9.2023
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


class Coin:
    """Coin Object.

    Attributes:
        _symbol (str): The coin symbol for the coin object.
        _name (str): The name of the coin to be created with the object.
        _price (float): The price of the coin being created.
        _description (str): The description of the coin.
    """

    def __init__(self, _symbol='', _name='', _price=0.0):
        self.symbol = _symbol
        self.name = _name
        self.price = _price

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_description(self, desc):
        self.description = desc

    def get_description(self):
        return self.description

    def __str__(self):
        str = f'{self.symbol}: {self.name} is trading at {self.price:.10f}'
        return f'{str}\n{self.description}'

    def __eq__(self, other):
        if isinstance(other, Coin):
            return (self.symbol == other.symbol) and (self.name == other.name)

        return False
