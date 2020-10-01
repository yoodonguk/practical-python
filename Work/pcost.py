# pcost.py
#
# Exercise 1.27

import csv, sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            # print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            else:
                pass
 
    
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)