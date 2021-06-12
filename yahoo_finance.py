import csv
import time
import pandas_datareader.data as web


fn = 'ticker.txt'

with open(fn) as f: 
    for i, ticker in enumerate(f):
        line = i
        print(i, ticker)

columns = ['shortName', 'price', 'trailingAnnualDividendRate']
data = [[i for i in range(len(columns)+1)] for j in range(line + 1)]

csv_fn = 'data.csv'
csv_f = open(csv_fn, 'w', newline='')
csvw = csv.writer(csv_f, delimiter='\t')

with open(fn) as f:
    for i, ticker in enumerate(f):
        print(f'reading..{i}th')
        ticker = ticker.rstrip()
        try:
            tsd = web.get_quote_yahoo(ticker)
            data[i][0] = ticker

            for j, column in enumerate(columns):
                try:
                    data[i][j+1] = tsd[column][ticker]
                except:
                    data[i][j+1] = 0.0    

            csvw.writerow(data[i])                    
            print(i, data[i])
            time.sleep(1.8)
        except:
            print(f'{i} {ticker} error')    

csv_f.close()            