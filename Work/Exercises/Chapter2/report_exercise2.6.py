# exercise 2.6

import csv
from pprint import pprint

def read_prices():
    filename='prices.csv'
    file=open(filename,'rt')
    rows=csv.reader(file)
    stock_list={}
    for row in rows:
        if not row:
            print('ignored blank record')
        else:
            symbol=row[0]
            price=float(row[1])
            stock_list[symbol]=price
            # print(symbol,':',stock_list[symbol])
    file.close()
    # print(stock_list)

    return stock_list

stock_price_list=read_prices()
pprint(stock_price_list)

# total_cost=0.0
# for name in portfolio:
    # total_cost+=name['shares']*name['price']
# print('Total cost:',total_cost)
