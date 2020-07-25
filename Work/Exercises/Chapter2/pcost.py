# exercise 1.32

import csv
import gzip

def portfolio_cost(filename):
    try:
        file=gzip.open(filename,'rt')
        rows=csv.reader(file)
        headers=next(rows)
        # print(f'# | {headers[0]:^8} | {headers[1]:^8} | {headers[2]:^6}')
        # print('--|----------|----------|-------')
        records=[]
        for line in rows:
            records.append(line)

        total_cost=0.0
        for x,i in enumerate(records):
            record=dict(zip(headers,i))
            try:
                # symbol=record['name']
                shares=int(record['shares'])
                price=float(record['price'])
                # print(x,f'| {symbol:8} | {shares:8} | {price:0.2f}')
                total_cost+=shares*price
            except ValueError:
                print(f"Row {x}: Bad row: {i}")
        # print(f'\nTotal cost: ${total_cost:0.2f}')
        file.close()
    except FileNotFoundError:
        print("File not found:",filename)
        return -1
    return total_cost

# cost=portfolio_cost('portfolio.csv.gz')
cost=portfolio_cost('portfoliodate.csv.gz')
# cost=portfolio_cost('missing.csv.gz')
print(f'\nTotal cost: ${cost:0.2f}')

