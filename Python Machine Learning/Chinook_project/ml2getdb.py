import pandas as pd
from sqlalchemy import create_engine

# Tus datos de conexión
engine = create_engine(f"mysql+mysqlconnector://root:Gerco&9371@localhost/chinook")

# SQL con JOIN de 3 tablas:
# Customers (Clientes) + Invoices (Facturas) + InvoiceItems (Detalle de productos)
query = """
SELECT 
    c.CustomerId,
    c.Country,
    c.City,
    i.InvoiceDate,
    il.invoiceid,
    i.Total AS FacturaTotal,
    SUM(il.Quantity) AS CantidadProductos
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items il ON i.InvoiceId = il.InvoiceId
GROUP BY i.InvoiceId
"""

df_ml = pd.read_sql(query, engine)

print("DataFrame unido y listo:")
print(df_ml.head())