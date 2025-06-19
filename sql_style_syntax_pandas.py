# Run this code without change

import sqlite3
import pandas as pd
from pandasql import sqldf
from matplotlib import pyplot as plt

conn = sqlite3.Connection('data.sqlite')

df = pd.read_sql("""
SELECT *
 FROM products;
""", conn)

df.head()

query = ("""
SELECT productLine, AVG(MSRP) AS avgMSRP
 FROM products
 GROUP BY productLine
 ORDER By productLine;
""")

df_query = pd.read_sql(query, conn)
df_query.head()

df.plot(kind='scatter', x='buyPrice', y='MSRP', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

df = df.eval('Price_Difference = MSRP-buyPrice')
df.head()

df['Price_Difference'].plot(kind='hist', bins=20, title='Price_Difference')
plt.gca().spines[['top', 'right',]].set_visible(False)

df_50 = df[df['Price_Difference'] > 50]
len(df_50)
comparison = len(df)-len(df_50)
comparison

conn.close()
