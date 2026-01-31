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
  add_airplane = ('INSERT INTO airplanes '
    '(plane_id, plane, manufacturer_id, engine_type, engine_count, '
      'wingspan, plane_length, max_weight, icao_code) '
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')
 
  # define plane values for INSERT in a tuple
  plane_values = (1001, 'A340-600', 101, 'Jet', 4, 208.17, 247.24, 837756, 'A346')
 
  # run INSERT statement
  cursor.execute(add_airplane, plane_values)
 
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