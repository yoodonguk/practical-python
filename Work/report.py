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

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

# cost = portfolio_cost(filename)
# print('Total cost:', cost)

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']

print('Total cost', total_cost)

total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['names']]

print('Curent value', total_value)
print('Gain', total_value - total_cost)

for p in portfolio:
    names = p['names']
    shares = p['shares']
    price = p['price']
    t_price = prices[names]
    print(f'{names:4s} {shares:5d}주 매입가 {price:7.2f} 현재가 {t_price:7.2f} 평가손익 {(t_price - price) * shares:10.2f}')