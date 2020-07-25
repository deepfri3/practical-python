# exercise 2.4 - reading from the command line

import csv,sys

def read_portfolio():
    filename='portfolio.csv'
    file=open(filename,'rt')
    rows=csv.reader(file)
    headers=next(rows)
    print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^6}')
    print('---------|----------|-------')
    portfolio=[]
    for row in rows:
        symbol=row[0]
        shares=int(row[1])
        price=float(row[2])
        holding=(symbol,shares,price)
        print(f'{holding[0]:8} | {holding[1]:8} | {holding[2]:0.2f}')
        portfolio.append(holding)
    file.close()
    return portfolio

portfolio=read_portfolio()
print(portfolio)

total_cost=0.0
for s in portfolio:
    total_cost+=s[1]*s[2]
print('Total cost:',total_cost)

total_cost=0.0
for name,shares,price in portfolio:
    total_cost+=shares*price
print('Total cost:',total_cost)


