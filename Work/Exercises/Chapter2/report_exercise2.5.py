# exercise 2.5

import csv,sys
from pprint import pprint

def read_portfolio():
    filename='portfolio.csv'
    file=open(filename,'rt')
    rows=csv.reader(file)
    headers=next(rows)
    portfolio=[]
    for row in rows:
        name=row[0]
        shares=int(row[1])
        price=float(row[2])
        holding={'name':name,'shares':shares,'price':price}
        portfolio.append(holding)
    file.close()

    print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^6}')
    print('---------|----------|-------')
    for symbol in portfolio:
        name=symbol['name']
        shares=symbol['shares']
        price=symbol['price']
        print(f'{name:8} | {shares:8} | {price:0.2f}')

    return portfolio

portfolio=read_portfolio()
pprint(portfolio)

total_cost=0.0
for name in portfolio:
    total_cost+=name['shares']*name['price']
print('Total cost:',total_cost)
