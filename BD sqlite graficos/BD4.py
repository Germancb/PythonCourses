import sqlite3

miConexion=sqlite3.connect("primeraBD")   #Se crea BD ya que no eciste abrir-crear

miCursor=miConexion.cursor()  # Crea cursor

# miCursor.execute("DROP TABLE IF EXISTS PRODUCTOS")
# miCursor.execute("CREATE TABLE PRODUCTOS (Nombre_Articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

# variosProductos=[

#   ("Camiseta", 10, "Deportes"),
#   ("Jarron", 10, "Ceramica"),
#   ("Camion", 10, "Jugueteria")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")
# Almacenar un lote de registros  del select
variosProductos=miCursor.fetchall()
for producto in variosProductos:
    print("Nombre articulo: ", producto[0], "Seccion: ", producto[2])
    print(producto)

miConexion.commit()

miConexion.close()   #Paso 6