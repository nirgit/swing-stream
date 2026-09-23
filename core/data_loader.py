import yfinance as yf
def load_stock(symbol):
    return yf.download(symbol,start="2010-01-01",auto_adjust=True)
