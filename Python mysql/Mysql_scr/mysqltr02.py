# import the connect method
from mysql.connector import connect
 
# define a connection object
conn = connect(option_files ="c:/users/ACER/Mysql scr/connectors.cnf")

# '/users/mac/documents/config/connectors.cnf'
# verify the connection information
print('The user ' + conn.user + ' is connected to the '
       + conn.database + ' database.')
 
# close the database connection
conn.close()

# mysql.connector.connect(option_files='/us/mysql/connectors.cnf', database='travel')