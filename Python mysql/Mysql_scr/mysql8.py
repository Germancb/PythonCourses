import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="mydb01"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)