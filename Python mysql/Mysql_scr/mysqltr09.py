from mysql.connector import connect, Error
 
# define connection object
conn = connect(
  user='germancbp',
  password='Gerco#9371',
  host='localhost',
  database='travel')
#  open cursor
cursor = conn.cursor()
 
# try to run code block
try:
  # define INSERT statement
  add_airplanes = ('INSERT INTO airplanes '
    '(plane_id, plane, manufacturer_id, engine_type, engine_count, '
      'wingspan, plane_length, max_weight, icao_code) '
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')
 
  # define plane values for INSERT in an list of tuples
  plane_values = [
    (1002, 'A350-800 XWB', 101, 'Jet', 2, 212.42, 198.58, 546700, 'A358'),
    (1003, 'A350-900', 101, 'Jet', 2, 212.42, 219.16, 617295, 'A359'),
    (1004, 'A380-800', 101, 'Jet', 4, 261.65, 238.62, 1267658, 'A388'),
    (1005, 'A380-843F', 101, 'Jet', 4, 261.65, 238.62, 1300000, 'A38F')]
 
  # run INSERT statement
  cursor.executemany(add_airplanes, plane_values)
 
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