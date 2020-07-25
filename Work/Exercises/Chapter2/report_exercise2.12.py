# exercise 2.7

import csv
from pprint import pprint

def read_prices(filename):
    file=open(filename,'rt')
    rows=csv.reader(file)
    stock_list={}
    for row in rows:
        if row:
            symbol=row[0]
            price=float(row[1])
            stock_list[symbol]=price
            # print(symbol,':',stock_list[symbol])
    file.close()
    # print(stock_list)

    return stock_list

def read_portfolio(filename):
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

    print('Portfolio at purchase:')
    print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^8}')
    print('---------|----------|---------')
    for symbol in portfolio:
        name=symbol['name']
        shares=symbol['shares']
        price=symbol['price']
        price='${:,.2f}'.format(price)
        print(f'{name:>8} | {shares:>8} | {price:>8s}')

    return portfolio

def make_report(portfolio,prices):

    # headers=['Name','Shares','Price','Change']
    # print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^8} | {headers[3]:^8}')
    # print('---------|----------|----------|---------')
    report=[]
    for symbol in portfolio:
        name=symbol['name']
        shares=symbol['shares']
        price_original=symbol['price']
        price_new=prices[name]
        change=price_new-price_original
        # print(f'{name:^8} | {shares:>8} | {price_new:>8.2f} | {change:>8.2f}')
        holding=(name,shares,price_new,change)
        report.append(holding)
    print('\nPortfolio current:')
    print_report(report)
    return report

def print_report(report):

    # headers=['Name','Shares','Price','Change']
    # print(f'{headers[0]:^10} | {headers[1]:^10} | {headers[2]:^10} | {headers[3]:^10}')
    # print('-----------|------------|------------|-----------')
    # for r in report:
        # print('%10s | %10d | %10.2f | %10.2f' % r)

    headers=['Name','Shares','Price','Change']
    print(f'{headers[0]:^10} | {headers[1]:^10} | {headers[2]:^10} | {headers[3]:^10}')
    print('-----------|------------|------------|-----------')
    for name,shares,price,change in report:
        price='${:,.2f}'.format(price)
        print(f'{name:>10s} | {shares:>10d} | {price:>10s} | {change:>10.2f}')

portfolio=read_portfolio('portfolio.csv')
stock_price_list=read_prices('prices.csv')
report=make_report(portfolio,stock_price_list)
# print_report(report)

# total_cost_port=0.0
# total_cost_new=0.0
# for name in portfolio:
    # total_cost_port+=name['shares']*name['price']
    # total_cost_new+=name['shares']*stock_price_list[name['name']]
# print('Total cost portfolio:',total_cost_port)
# print('Total cost new:',round(total_cost_new,2))
# print('Gains/Loss:',round((total_cost_new-total_cost_port),2))


