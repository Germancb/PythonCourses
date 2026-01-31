import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="germancbp",
    password="Gerco#9371"
)

print(mydb)

#cnx = mysql.connector.connect(user='germancb', password='Gerco&9371',
#                              host='127.0.0.1'
#)
                              
#print(cnx)
# cnx.close()
