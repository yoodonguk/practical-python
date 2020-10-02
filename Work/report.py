# report.py
#
# Exercise 2.4

import csv, sys
from fileparse import parse_csv

def read_portfolio(filename):    
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])


def read_prices(filename):
    return dict(parse_csv(filename, types=[str,float], has_headers=False))


def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary =(stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(report):
    headers = (f'{"Names":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
    seperator = (f'{"-" * 10} {"-" * 10} {"-" * 10} {"-" * 10}')

    print(headers)
    print(seperator)

    for names, shares, price, change in report:
        price = f'${price:.2f}'
        print(f'{names:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')   


def portfolio_report(portfolio_csv, prices_csv):
    portfolio = read_portfolio(portfolio_csv)
    prices = read_prices(prices_csv)
    report = make_report(portfolio, prices)
    print_report(report)
 
files = ['Data/portfolio.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')
    print()