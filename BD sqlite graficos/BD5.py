import sqlite3

miConexion=sqlite3.connect("GestionProductos")   #Se crea BD ya que no eciste abrir-crear

miCursor=miConexion.cursor()  # Crea cursor

miCursor.execute("DROP TABLE IF EXISTS PRODUCTOS")

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')

vProductos=[

    ("AR01","Camiseta", 10, "Deportes"),
    ("AR02","Jarron", 10, "Ceramica"),
    ("AR03","Camion", 10, "Jugueteria"),
    ("AR04","Camisa", 10, "Deportes")
]
      
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", vProductos)

miConexion.commit()

miConexion.close()   #Paso 6