import random,yfinance as yf
UNIVERSE=["DDOG","NET","MDB","CELH","TTD","AXON","HUBS"]
def scenario():
 t=random.choice(UNIVERSE)
 df=yf.download(t,start="2018-01-01",auto_adjust=True,progress=False)
 if hasattr(df.columns,"nlevels") and df.columns.nlevels>1: df.columns=df.columns.get_level_values(0)
 df=df.dropna()
 idx=random.randint(150,max(180,len(df)-30))
 return t,df.iloc[idx-120:idx].copy(),df.iloc[idx:idx+20].copy()
