from urllib import request
goog_url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1543525807&period2=1575061807&interval=1d&events=history&crumb=/0R7y2X4gKj"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(desturl, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)