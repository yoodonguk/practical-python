# stock.py
#
# Exercise 4.1

class Stock():
    def cost(self):
        return self.shares * self.price

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
