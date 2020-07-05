# exercise 1.33 - reading from the command line

import csv,gzip,sys

def portfolio_cost():
    try:
        if len(sys.argv) == 2:
            filename=sys.argv[1]
        else:
            filename='portfolio.csv.gz'
        file=gzip.open(filename,'rt')
    except FileNotFoundError:
        print("File not found:",filename)
        return -1
    rows=csv.reader(file)
    headers=next(rows)
    print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^6}')
    print('---------|----------|-------')
    records=[]
    for line in rows:
        records.append(line)

    total_cost=0.0
    for i in records:
        symbol=i[0]
        try:
            shares=int(i[1])
        except ValueError:
            print(f"Unable to convert literal string to value: {symbol}")
        price=float(i[2])
        print(f'{symbol:8} | {shares:8} | {price:0.2f}')
        total_cost=total_cost+(shares*price)
    print(f'\nTotal cost: ${total_cost:0.2f}')
    file.close()
    return total_cost

cost=portfolio_cost()
# print(f'\nTotal cost: ${cost:0.2f}')

