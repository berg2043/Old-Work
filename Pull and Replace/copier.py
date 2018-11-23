import sqlite3
import pandas as pd
import numpy as np

df1 = pd.read_csv('new.csv')
df2 = pd.read_csv('original.csv')

conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

df2.to_sql('t', conn, if_exists = 'append', index = False)
df1.to_sql('t', conn, if_exists = 'append', index = False)

#df3 = pd.read_sql_query('SELECT * FROM t', conn)

df3 = pd.read_sql_query('SELECT Date, Source, max(count) AS Count FROM t Group BY Date, Source', conn)

df3['Date'] = pd.to_datetime(df3['Date'].astype(str)).dt.strftime('%m/%d/%y')

df3 = df3.sort_values(['Date', 'Source'])

conn.close()

print(df3)