import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="mydb01"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)