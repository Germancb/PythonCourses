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
    "SET plane = 'D.5/108 Husky' WHERE plane_id = %s")
 
  # define plane_id value for UPDATE as a tuple
  id_value = (1010,)
 
  # run UPDATE statement
  cursor.execute(update_plane, id_value)
 
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