import yfinance as yf
import random

UNIVERSE=["DDOG","NET","CELH","MDB","HUBS","TTD","AXON"]

def scenario():
    ticker=random.choice(UNIVERSE)
    df=yf.download(ticker,start="2015-01-01",auto_adjust=True,progress=False)
    df=df.dropna()
    idx=random.randint(150,len(df)-30)
    return ticker,df.iloc[idx-120:idx],df.iloc[idx:idx+20]
