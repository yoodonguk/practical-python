# stock.py
#
# Exercise 4.1

from typedproperty import String, Integer, Float

class Stock():
    #__slots__ = ('name','_shares','price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value,int):
            raise TypeError("expeted an integer")
        self._shares = value