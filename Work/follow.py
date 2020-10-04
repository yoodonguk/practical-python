# follow.py
#
# Exercise 6.5

import os
import time

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    lines = follow('Data/stocklog.csv')
    ibm = filematch(lines, 'IBM')
    for line in ibm:
        print(line)


    ''''
    for line in lines:
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
    '''