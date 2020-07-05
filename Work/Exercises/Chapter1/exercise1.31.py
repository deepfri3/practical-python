# exercise 1.31 - error handling

import gzip

def portfolio_cost(filename):
    try:
        file=gzip.open(filename,'rt')
    except FileNotFoundError:
        print("File not found:",filename)
        return -1
    headers=next(file).split(',')
    headers[2]=headers[2].strip('\n')
    # print(f'{headers[0]:^8} | {headers[1]:^8} | {headers[2]:^6}')
    # print('---------|----------|-------')
    records=[]
    for line in file:
        record=line.split(',')
        records.append(record)

    total_cost=0.0
    for i in records:
        symbol=i[0]
        try:
            shares=int(i[1])
        except ValueError:
            print(f"Unable to convert literal string to value: {symbol}")
        price=float(i[2])
        # print(f'{symbol:8} | {shares:8} | {price:0.2f}')
        total_cost=total_cost+(shares*price)
    # print(f'\nTotal cost: ${total_cost:0.2f}')
    file.close()
    return total_cost

# cost=portfolio_cost('portfolio.csv.gz')
# print(f'\nTotal cost: ${cost:0.2f}')

