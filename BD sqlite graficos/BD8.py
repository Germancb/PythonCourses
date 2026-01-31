import sqlite3

miConexion=sqlite3.connect("GestionProductos")   #Se crea BD ya que no eciste abrir-crear

miCursor=miConexion.cursor()  # Crea cursor

miCursor.execute("DROP TABLE IF EXISTS PRODUCTOS2")

miCursor.execute('''
    CREATE TABLE PRODUCTOS2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')

vProductos=[

    ("Camiseta", 10, "Deportes"),
    ("Jarron", 10, "Ceramica"),
    ("Camion", 10, "Jugueteria"),
    ("Camisa", 10, "Deportes")
]
      
miCursor.executemany("INSERT INTO PRODUCTOS2 VALUES (NULL,?,?,?)", vProductos)

miConexion.commit()

miConexion.close()   #Paso 6