import mysql.connector
# mysql  -u root -p
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password="Gerco&9371"
)
print(mydb)