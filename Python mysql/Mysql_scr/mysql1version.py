import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="germancbp",
    password="Gerco#9371"
)

print(conn)

cursor = conn.cursor()

# Run version query
cursor.execute("SELECT VERSION();")

# Get and print the version
version = cursor.fetchone()
print("MySQL version:", version[0])

cursor.close()
conn.close()

#cnx = mysql.connector.connect(user='germancb', password='Gerco&9371',
#                              host='127.0.0.1'
#)
                              
#print(cnx)
# cnx.close()
