import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

cursor.execute(
'''SELECT Name 
FROM Artist
ORDER BY Name''')

results = cursor.fetchall()
print(results)

conn.close()