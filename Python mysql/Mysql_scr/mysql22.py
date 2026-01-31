import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="mydb01"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")