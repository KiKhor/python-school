import sqlite3
import pprint

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

request_text1 ='''SELECT DISTINCT C.FirstName||' '||C.LastName AS FullName, C.Phone
                FROM Customer AS C
                INNER JOIN (SELECT City, COUNT(*) AS CountInCity
                            FROM Customer
                            GROUP BY City
                            HAVING CountInCity > 1) AS N ON N.City = C.City
                LEFT JOIN Invoice AS I ON C.CustomerId = I.CustomerId
                WHERE I.Total > 0
                ORDER BY FullName'''

request_text2 ='''SELECT BillingCity, SUM(Total)
                FROM Invoice
                GROUP BY BillingCity
                HAVING SUM(Total)
                ORDER BY SUM(Total) desc
                LIMIT 3'''

request_text3 ='''SELECT FirstName||' '||LastName AS FullName, City, COUNT(*)
                FROM Customer
                GROUP BY City
                HAVING COUNT(*) > 1'''

cursor.execute(request_text2)
results = cursor.fetchall()
pprint.pprint(results)

conn.close()
