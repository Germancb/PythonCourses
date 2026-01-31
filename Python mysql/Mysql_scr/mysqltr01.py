# import the connect method
from mysql.connector import connect
# define a connection object
conn = connect(
      user = 'germancbp',
      password = 'Gerco#9371',
      host = 'localhost',
      database = 'travel')
 
print('A connection object has been created.')
print('The user ' + conn.user + ' is connected to the '
       + conn.database + ' database.')
 
# close the database connection
conn.close()

