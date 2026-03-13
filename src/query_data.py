import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/house_prices.db")
#Query 1: Overall Summary of data
q1 = """ SELECT 
    COUNT(*) AS total_transactions,
    ROUND(AVG(price)) AS average_price,
    ROUND(MIN(price)) AS min_price,
    ROUND(MAX(price)) AS max_price
FROM transactions"""

#Query 2: How does the town of a property affect its price ?

#Query 2a: Which town is most expensive on average ? 
q2a = """ SELECT 
    town, 
    ROUND(AVG(price)) AS average_price
    FROM transactions 
    GROUP BY town
    ORDER BY average_price DESC
    LIMIT 1
"""
#Query 2b: Which town is least expensive on average ? 
q2b = """ SELECT 
    town, 
    ROUND(AVG(price)) AS average_price
FROM transactions
GROUP BY town
ORDER BY average_price ASC
LIMIT 1
"""

#Query 2c: Rank 5 towns by average price, descending?
q2c = """ SELECT 
    town, 
    ROUND(AVG(price)) AS average_price
FROM transactions
GROUP BY town
ORDER BY average_price DESC
LIMIT 5
"""

#Query 3: Within London, which 3 boroughs are least expensive on average ?
q3= """ SELECT 
    locality,
    ROUND(AVG(price)) AS average_price
FROM transactions
WHERE locality IS NOT NULL 
AND locality != '' 
AND locality != 'LONDON'
AND town = 'LONDON'
GROUP BY locality
ORDER BY average_price ASC
LIMIT 3
"""
############## Execute and print results ################
print("=== 1. OVERALL SUMMARY ===")
print(pd.read_sql(q1, engine))

print("=== 2A. MOST EXPENSIVE TOWN ===")
print(pd.read_sql(q2a, engine))

print("=== 2B. LEAST EXPENSIVE TOWN ===")
print(pd.read_sql(q2b, engine))

print("=== 2C. TOP 5 MOST EXPENSIVE TOWNS ===")
print(pd.read_sql(q2c, engine))

print("=== 3. TOP 3 CHEAPEST BOROUGHS IN LONDON ===")
print(pd.read_sql(q3, engine))
