import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="chinook"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tracks LIMIT 5")

myresult = mycursor.fetchall()

print(myresult)