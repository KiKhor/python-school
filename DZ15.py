import sqlite3
import pprint

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

request_text1 ='''SELECT FirstName||' '||LastName AS FullName, City, COUNT(*)
                FROM Customer
                GROUP BY City
                HAVING COUNT(*) > 1'''

request_text2 ='''SELECT FirstName||' '||LastName AS FullName, City, COUNT(*)
                FROM Customer
                GROUP BY City
                HAVING COUNT(*) > 1'''

request_text3 ='''SELECT FirstName||' '||LastName AS FullName, City, COUNT(*)
                FROM Customer
                GROUP BY City
                HAVING COUNT(*) > 1'''

cursor.execute(request_text1)
results = cursor.fetchall()
pprint.pprint(results)

conn.close()