import sqlite3 as sql
conn = sql.connect('factbook.db')
query = "select name,population from facts order by population asc limit 10;"
c = conn.execute(query).fetchall()
print(c)
conn.close