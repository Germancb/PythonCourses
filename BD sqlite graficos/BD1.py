import sqlite3

miConexion=sqlite3.connect("primeraBD")   #Se crea BD ya que no eciste abrir-crear

miCursor=miConexion.cursor()  # Crea cursor

miCursor.execute("DROP TABLE IF EXISTS PRODUCTOS")
miCursor.execute("CREATE TABLE PRODUCTOS (Nombre_Articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

miConexion.commit()

miConexion.close()   #Paso 6