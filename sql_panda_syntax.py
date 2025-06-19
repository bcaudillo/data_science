import sqlite3
import pandas as pd
from pandasql import sqldf

conn = sqlite3.Connection('data.sqlite')

products_df = pd.read_sql("""
                          SELECT *
                          FROM products
                          """, conn)
products_df.head()

od_df = pd.read_sql("""
                    SELECT *
                    FROM orderDetails
                    """, conn)

od_df.head()

# Need to make buyPrice numeric
products_df['buyPrice'] = products_df['buyPrice'].astype(float)

# Getting Data using slicing syntax
foo_df1 = products_df[products_df["buyPrice"] >= 50]

# These two lines are equivalent!
print(foo_df1.shape, foo_df2.shape)
foo_df1.head()
foo_df2.head()


foo_df = products_df.query("buyPrice >=50 & productLine == 'Classic Cars'")
foo_df.head()

pysqldf = lambda q: sqldf(q, globals())

# Query for Pandas
top_5_query_pandas = """
SELECT productCode, productName, SUM(quantityOrdered) as TotalOrdered
    FROM products_df
        JOIN od_df
            USING(productCode)
GROUP BY productCode
ORDER BY TotalOrdered DESC
Limit 5
"""

# Query for SQL
top_5_query_sql = """
SELECT productCode, productName, SUM(quantityOrdered) as TotalOrdered
    FROM products
        JOIN orderDetails
            USING(productCode)
GROUP BY productCode
ORDER BY TotalOrdered DESC
Limit 5
"""

top_5 = pysqldf(top_5_query_pandas)
top_5.head()

# Use Pandas to read query
top_5_best = pd.read_sql(top_5_query_sql, conn)
top_5_best.head()

# Should have same results
top_5 == top_5_best

# Easy summary statistics
top_5_best.describe()


# Calculate the percentage of total sales for each product among the top 5
total_sales = top_5_best['TotalOrdered'].sum()

# Add as new column
top_5_best['SalesPercentage'] = top_5_best['TotalOrdered'] / total_sales * 100

top_5_best.head()

import matplotlib.pyplot as plt

# Create Bar chart
top_5_best.plot(x='productName', y='SalesPercentage', kind='bar')
plt.title('Sales Percentage of Top 5 Products')
plt.ylabel('Percentage of Total Sales')
plt.xlabel('Product Name')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Remember to close the connection when you are done
conn.close()