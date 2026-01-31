import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371"
)

print(mydb)
# mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydb01")
# mycursor.execute("CREATE DATABASE classicalmodels")