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
  update_planes = ("UPDATE airplanes "
    "SET wingspan = ROUND(wingspan), plane_length = ROUND(plane_length) "
    "WHERE manufacturer_id = "
      "(SELECT manufacturer_id FROM manufacturers "
      "WHERE manufacturer = %s)")
 
  # define plane_id value for UPDATE
  manufacturer = ('Beagle Aircraft Limited',)
 
  # run UPDATE statement
  cursor.execute(update_planes, manufacturer)
 
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