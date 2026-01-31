import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="mydb01"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)