# exercise 2.7

import csv
from pprint import pprint

def read_prices(filename):
    file=open(filename,'rt')
    rows=csv.reader(file)
    stock_list={}
    for row in rows:
        # if row:
        if row == []:
            continue
        else:
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
    # select=['name','shares','price']
    # indices=[headers.index(colname) for colname in select]
    # total_cost=0.0
    # portfolio=[{colname:row[index] for colname,index in zip(select,indices)} for row in rows]
    portfolio=[]
    types=[str,int,float]
    for row in rows:
        # r=dict(zip(types,row))
        # print(r)
        # converted=[]
        # for func,val in zip(types,row):
            # converted.append(func(val))
        # converted=[func(val) for func,val in zip(types,row)]
        # print(converted)
        # holding={'name':converted[0],'shares':converted[1],'price':converted[2]}
        # holding=dict(zip(headers,converted))
        holding={name:func(val) for name, func, val in zip(headers,types,row)}
        # name=types[0](row[0])
        # shares=types[1](row[1])
        # price=types[2](row[2])
        # holding={'name':name,'shares':shares,'price':price}
        portfolio.append(holding)
    print(portfolio)
    # for i,row in enumerate(rows):
        # record=dict(zip(headers,row))
        # try:
            # shares=int(record['shares'])
            # price=float(record['price'])
            # total_cost+=shares*price
            # portfolio.append(record)
        # except ValueError:
            # print(f"Row {i}: Bad row: {row}")
    file.close()

    print('Portfolio at purchase:')
    name_idx=headers.index('name')
    shares_idx=headers.index('shares')
    price_idx=headers.index('price')
    print(f'{headers[name_idx]:^8} | {headers[shares_idx]:^8} | {headers[price_idx]:^8}')
    print('---------|----------|---------')
    total_cost=0.0
    for symbol in portfolio:
        name=types[0](symbol['name'])
        shares=types[1](symbol['shares'])
        price=types[2](symbol['price'])
        total_cost+=shares*price
        price='${:,.2f}'.format(price)
        print(f'{name:>8} | {shares:>8} | {price:>8s}')
    print('Total Cost:',total_cost)

    return portfolio

def make_report(portfolio,prices):

    # headers=['Name','Shares','Price','Change']
    # print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^8} | {headers[3]:^8}')
    # print('---------|----------|----------|---------')
    report=[]
    for symbol in portfolio:
        name=symbol['name']
        shares=int(symbol['shares'])
        price_original=float(symbol['price'])
        price_new=prices[name]
        change=price_new-price_original
        # print(f'{name:^8} | {shares:>8} | {price_new:>8.2f} | {change:>8.2f}')
        holding=(name,shares,price_new,change)
        report.append(holding)
    print('\nPortfolio current:')
    print_report(report)
    return report

def print_report(report):

    total_cost=0.0
    headers=['Name','Shares','Price','Change']
    print(f'{headers[0]:^10} | {headers[1]:^10} | {headers[2]:^10} | {headers[3]:^10}')
    print('-----------|------------|------------|-----------')
    for name,shares,price,change in report:
        total_cost+=shares*price
        price='${:,.2f}'.format(price)
        print(f'{name:>10s} | {shares:>10d} | {price:>10s} | {change:>10.2f}')
    print('Total cost:',total_cost)

portfolio=read_portfolio('portfolio.csv')
# portfolio2=read_portfolio('portfolio2.csv')
# portfolio=read_portfolio('portfoliodate.csv')
# portfolio=read_portfolio('missing.csv')
# stock_price_list=read_prices('prices.csv')
# report=make_report(portfolio,stock_price_list)
# print_report(report)

# total_cost_port=0.0
# total_cost_new=0.0
# for name in portfolio:
    # total_cost_port+=name['shares']*name['price']
    # total_cost_new+=name['shares']*stock_price_list[name['name']]
# print('Total cost portfolio:',total_cost_port)
# print('Total cost new:',round(total_cost_new,2))
# print('Gains/Loss:',round((total_cost_new-total_cost_port),2))


