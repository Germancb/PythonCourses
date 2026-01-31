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
  # define INSERT statement
  add_manufacturer = ('INSERT INTO manufacturers '
    '(manufacturer_id, manufacturer) '
    'VALUES (101, \'Airbus\')')
 
  # run INSERT statement
  cursor.execute(add_manufacturer)
 
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