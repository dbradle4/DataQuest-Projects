import sqlite3 as sql
import pandas as pd
conn = sql.connect('factbook.db')
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

facts = facts.sort_values(by='population_2050', ascending=False)

print(facts[['name', 'population_2050']].head(10))
conn.close()