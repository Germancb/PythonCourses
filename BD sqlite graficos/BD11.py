import sqlite3

miConexion=sqlite3.connect("GestionProductos")   #Se abre BD

miCursor=miConexion.cursor()  # Crea cursor


miCursor.execute("SELECT * FROM PRODUCTOS2 WHERE seccion='Deportes'")

miCursor.execute("DELETE FROM PRODUCTOS2 WHERE ID=4")

#prods=miCursor.fetchall() 
# print(prods)    

miConexion.commit()

miConexion.close()   #Paso 6