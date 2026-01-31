# import the connect and Error methods
from mysql.connector import connect, Error
 
# try to run the block of code
try:
# define a connection object
  conn = connect(
      user = 'germancbp',
      password = 'Gerco#9371',
      host = 'localhost',
      database = 'travel')
  # open cursor, define and run query, fetch results
  cursor = conn.cursor()
  query = ('SELECT plane_id, plane, max_weight FROM airplanes ' 
    'WHERE max_weight > 500000 ' 
    'ORDER BY max_weight DESC')
  cursor.execute(query)
  result = cursor.fetchall()
  # print the results in each row
  for r in result:
    print(r)
 
  # close the cursor and database connection
  cursor.close()
  conn.close()
 
# catch exception and print error message
except Error as err:
  print('Error message: ' + err.msg)