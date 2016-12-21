import sqlite3
import pandas as pd
conn = sqlite3.connect('factbook.db')
query = "select * from facts;"

facts = pd.read_sql_query(sql=query, con=conn, index_col='id')

facts = facts.dropna(axis=0)

def final_population(row, y):
    import math
    N0 = row['population']
    r = row['population_growth']/100
    t = y-2015
    N = N0*math.e**(r*t)
    return N
    
facts['population_2050'] = facts.apply(final_population, args=(2050,), axis=1)

is_negative = facts[facts['population_growth'] < 0]
print(is_negative[['name', 'population', 'population_2050']])
conn.close()