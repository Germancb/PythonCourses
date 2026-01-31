from mysql.connector import connect, Error
 
# define connection object
conn = connect(
  user='germancbp',
  password='Gerco#9371',
  host='localhost',
  database='travel')
# open cursor
cursor = conn.cursor()
 
# try to run code block
try:
  # define DELETE statement
  delete_plane = ("DELETE FROM airplanes "
    "WHERE manufacturer_id = %(mfc_id)s AND max_weight < %(weight)s")
 
  # define values for DELETE in a tuple
  plane_values = {'mfc_id': 102, 'weight': 5000}
 
  # run DELETE statement
  cursor.execute(delete_plane, plane_values)
  print('Number of rows deleted: ', cursor.rowcount)
 
  # commit transaction
  conn.commit()
 
# catch exception, roll back transaction, print error message
except Error as err:
  conn.rollback()
  print('Error message: ' + err.msg)
 
# close cursor, close connection
finally:
  cursor.close()
  conn.close()