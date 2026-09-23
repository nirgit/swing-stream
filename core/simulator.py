import random
def create_scenario(df):
    s=random.randint(250,len(df)-40)
    return df.iloc[s-120:s],df.iloc[s:s+20]
