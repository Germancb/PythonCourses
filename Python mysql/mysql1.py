
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gerco&9371"
)

cursor = conn.cursor()
#cursor.execute(sql)

print("Usuario actualizado correctamente.")

cursor.close()
conn.close()
mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  # user="germancb79@gmail.com",
  password="Gerco&9371"
)

print(mydb)

