import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="classicalmodels"
)

mycursor = mydb.cursor()

sql = "SELECT orderdetails.orderNumber, orderdetails.productCode,products.productName  FROM orderdetails, products where orderdetails.productCode=products.ProductCode order by orderNumber;"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)