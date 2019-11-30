from urllib import request
stockData = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1543525807&period2=1575061807&interval=1d&events=history&crumb=/0R7y2X4gKj"

def downloadStockInfo(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    formatted = csv_str.split("\\n")
    filename = r'stockData.csv'
    fx = open(filename, 'w')
    for line in formatted:
        fx.write(line + "\n")
    fx.close()

downloadStockInfo(stockData)