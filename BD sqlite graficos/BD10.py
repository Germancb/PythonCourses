import sqlite3

miConexion=sqlite3.connect("GestionProductos")   #Se abre BD

miCursor=miConexion.cursor()  # Crea cursor


miCursor.execute("SELECT * FROM PRODUCTOS2 WHERE seccion='Deportes'")

miCursor.execute("UPDATE PRODUCTOS2 SET PRECIO=35 WHERE NOMBRE_ARTICULO='Camiseta'")

#prods=miCursor.fetchall() 
# print(prods)
      


miConexion.commit()

miConexion.close()   #Paso 6