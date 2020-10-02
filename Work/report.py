# report.py
#
# Exercise 2.4

import csv, sys
from fileparse import parse_csv
import stock
import tableformat

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


def print_report(reportdata, formatter):
    '''
    (name, shares, price, change) 튜플의 리스트로부터 보기 좋게 포매팅한 테이블을 프린팅
    '''
    formatter.headings(['Names', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
    
    
    
    #headers = (f'{"Names":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
    #seperator = (f'{"-" * 10} {"-" * 10} {"-" * 10} {"-" * 10}')

    #print(headers)
    #print(seperator)

    #for names, shares, price, change in reportdata:
    #    price = f'${price:.2f}'
    #    print(f'{names:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')   


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    주어진 포트폴리오와 가격 데이터 파일을 가지고 주식 보고서를 작성
    '''
    # 데이터 파일 읽기
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    
    # 보고서 데이터 생성
    report = make_report(portfolio, prices)

    # 프린트
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
 

def main(args):
    if len(args) == 4:
        portfolio = args[1]
        price = args[2]
        fmt = args[3]
    else:
        portfolio = 'Data/portfolio.csv'
        price = 'Data/prices.csv'
        fmt = 'txt'
    
    portfolio_report(portfolio, price, fmt)
 

if __name__ == '__main__':
    import sys
    main(sys.argv) 
