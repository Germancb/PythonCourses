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
  # define manufacturers INSERT statement
  add_manufacturer = ('INSERT INTO manufacturers '
    '(manufacturer_id, manufacturer) '
    'VALUES (%s, %s)')
 
  # define manufacturer values for INSERT
  manufacturer_values = (102, 'Beagle Aircraft Limited')
 
  # run manufacturers INSERT statement
  cursor.execute(add_manufacturer, manufacturer_values)
 
  # define airplanes INSERT statement
  add_airplanes = ('INSERT INTO airplanes '
    '(plane_id, plane, manufacturer_id, engine_type, engine_count, '
      'wingspan, plane_length, max_weight, icao_code) '
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')
 
  # define plane values for INSERT
  plane_values = [
    (1006, 'A.109 Airedale', 102, 'Piston', 1, 36.33, 26.33, 2750, 'AIRD'),
    (1007, 'A.61 Terrier', 102, 'Piston', 1, 36, 23.25, 2400, 'AUS6'),
    (1008, 'B.121 Pup', 102, 'Piston', 1, 31, 23.17, 1600, 'PUP'),
    (1009, 'B.206', 102, 'Piston', 2, 55, 33.67, 7500, 'BASS'),
    (1010, 'D.5-108 Husky', 102, 'Piston', 1, 36, 23.17, 2400, 'D5')]
 
  # run airplanes INSERT statement
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