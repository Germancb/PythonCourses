import pandas as pd
import sqlite3

# Conectar a la base de datos descargada
conn = sqlite3.connect('temp_chinook.db')

query = """
SELECT 
    c.CustomerId,
    c.Country,
    COUNT(i.InvoiceId) AS TotalCompras,
    SUM(i.Total) AS GastoTotal,
    GROUP_CONCAT(DISTINCT t.GenreId) AS GenerosEscuchados
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
JOIN InvoiceLine ii ON i.InvoiceId = ii.InvoiceId
JOIN Track t ON ii.TrackId = t.TrackId
GROUP BY c.CustomerId
"""

df = pd.read_sql_query(query, conn)
print(df.head())