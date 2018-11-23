# this was me testing out how to eddit the date lol 
import pandas as pd

import numpy as np

df = pd.read_csv('pull.csv')

df['date'] = pd.to_datetime(df['date'].astype(str)).dt.strftime('%m/%d/%y')

#df['date'] = df['date'].dt.strftime('%m/%d/%y')

print (df.to_csv(index=False))