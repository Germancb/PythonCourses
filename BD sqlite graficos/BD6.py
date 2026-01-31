import sqlite3

miConexion=sqlite3.connect("GestionProductos")   #Se crea BD ya que no eciste abrir-crear

miCursor=miConexion.cursor()  # Crea cursor

      
miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05', 'Tren', 15, 'Jugueteria')")

miConexion.commit()

miConexion.close()   #Paso 6