# report.py
#
# Exercise 2.4

import csv, sys
from fileparse import parse_csv
import stock

def read_portfolio(filename):
    with open(filename) as lines:
        portdicts = parse_csv(lines, 
                                        select=['name','shares','price'], 
                                        types=[str,int,float])
        portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
        return portfolio


def read_prices(filename):
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))


def make_report(portfolio, prices):
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary =(s.name, s.shares, current_price, change)
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
 

def main(args):
    if len(args) == 3:
        portfolio = args[1]
        price = args[2]
    else:
        portfolio = 'Data/portfolio.csv'
        price = 'Data/prices.csv'
    
    portfolio_report(portfolio, price)
 

if __name__ == '__main__':
    import sys
    main(sys.argv) 
