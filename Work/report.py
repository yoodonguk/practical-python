# report.py
#
# Exercise 2.4

import csv, sys

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)

        for row in rows:
            stock = {
                'names'  : row[0],
                'shares' : int(row[1]),
                'price'  : float(row[2])
            }
            portfolio.append(stock) 
    
    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)
        # header = next(rows)

        for row in rows:
            try:
                name, price = row
                price = float(price)
            except:
                print('Bad data:', row)
            else:
                prices[name] = price            

    return prices

def make_report(portfolio, prices):
    report = []

    for p in portfolio:
        names = p['names']
        shares = p['shares']
        price = p['price']
        current_price = prices[names]

        change = price - prices[names]
        report.append((names, shares, current_price, change))

    return report

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

# cost = portfolio_cost(filename)
# print('Total cost:', cost)

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = (f'{"Names":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
seperator = (f'{"-" * 10} {"-" * 10} {"-" * 10} {"-" * 10}')

print(headers)
print(seperator)
#print(f'{"Names":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
#print(f'{"-" * 10} {"-" * 10} {"-" * 10} {"-" * 10}')

for names, shares, price, change in report:
    price = f'${price:.2f}'
    print(f'{names:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')    