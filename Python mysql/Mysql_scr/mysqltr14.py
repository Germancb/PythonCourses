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
  # define UPDATE statement
  update_plane = ("UPDATE airplanes "
    "SET wingspan = wingspan + %s, plane_length = plane_length + %s "
    "WHERE plane_id = %s")
 
  # define values for UPDATE in a tuple
  plane_values = (5, 8, 1005)
 
  # run UPDATE statement
  cursor.execute(update_plane, plane_values)
 
  # commit transaction
  conn.commit()
 
  # define SELECT statement
  select_query = (
    "SELECT plane_id, plane, wingspan, plane_length "
    "FROM airplanes WHERE plane_id = %s")
 
  # run SELECT statement
  cursor.execute(select_query, (plane_values[2],))
  results = cursor.fetchone()
 
  # print query results
  print('Rows updated:', cursor.rowcount)
  print('plane_id:', results[0])
  print('plane:', results[1])
  print('new wingspan:', results[2])
  print('new plane_length:', results[3])
 
# catch exception, roll back transaction, print error message
except Error as err:
  conn.rollback()
  print('Error message: ' + err.msg)
 
# close cursor, close connection
finally:
  cursor.close()
  conn.close()