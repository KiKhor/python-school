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

request_text3 ='''SELECT G.Name, T.Name, Al.Title, Ar.Name
                FROM Track AS T
                INNER JOIN (SELECT G.Name AS Name, G.GenreId AS GenreId
                    FROM InvoiceLine AS I
                    LEFT JOIN Track AS T ON I.TrackId = T.TrackId
                    LEFT JOIN Genre AS G ON T.GenreId = G.GenreId
                    GROUP BY G.Name 
                    HAVING  SUM(I.UnitPrice)
                    ORDER BY SUM(I.UnitPrice) desc
                    LIMIT 1) AS G ON T.GenreId = G.GenreId
                LEFT JOIN Album AS Al ON T.AlbumId = Al.AlbumId
                LEFT JOIN Artist AS Ar ON Al.ArtistId = Ar.ArtistId
                ORDER BY T.Name, Al.Title, Ar.Name'''

request_text31 = '''SELECT G.Name AS Name, SUM(I.UnitPrice) AS InvoiceForGenre
                    FROM InvoiceLine AS I
                    LEFT JOIN Track AS T ON I.TrackId = T.TrackId
                    LEFT JOIN Genre AS G ON T.GenreId = G.GenreId
                    GROUP BY G.Name 
                    HAVING  InvoiceForGenre
                    ORDER BY InvoiceForGenre desc
                    LIMIT 1'''

cursor.execute(request_text3)
results = cursor.fetchall()
pprint.pprint(results)

conn.close()
