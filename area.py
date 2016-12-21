import sqlite3 as sql
conn = sql.connect('factbook.db')
c = conn.cursor()
query_land = "select sum(area_land) from facts where area_land != '';"
query_water = "select sum(area_water) from facts where area_water != '';"
area_land = c.execute(query_land).fetchone()
area_water = c.execute(query_water).fetchone()
print(area_land[0]/area_water[0])
conn.close()