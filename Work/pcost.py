# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    result = 0.0
    with open(filename) as f:
        header = next(f)

        for line in f:
            _, count, cost = line.split(',')
            try:
                result += float(cost) * int(count)
            except ValueError:
                print('bad Data:', line)
            else:
                pass
 
    
    return result


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)