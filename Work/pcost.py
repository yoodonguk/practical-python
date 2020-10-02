# pcost.py
#
# Exercise 1.27

import csv, sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    
    return sum([s['shares'] * s['price'] for s in portfolio])

def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)


if __name__ == '__main__':
    import sys
    main(sys.argv)
