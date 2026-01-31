import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="classicalmodels"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("DROP TABLE IF EXISTS orders")
# DROP TABLE IF EXISTS customers

# Create a cursor object
mycursor = mydb.cursor()

# SQL query to create a table
create_table_query = """
CREATE TABLE orders (
  orderNumber int(11) NOT NULL,
  orderDate date NOT NULL,
  requiredDate date NOT NULL,
  shippedDate date DEFAULT NULL,
  status varchar(15) NOT NULL,
  comments text,
  customerNumber int(11) NOT NULL,
  PRIMARY KEY (orderNumber),
  KEY customerNumber (customerNumber),
  CONSTRAINT orders_ibfk_1 FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""

# Execute the SQL query to create the table
mycursor.execute(create_table_query)

# Commit the changes
mydb.commit()

# Close the cursor and the database connection
mycursor.close()
mydb.close()
#In this example, the cursor mycursor is used to execute the SQL query that creates a table named "mytable" with columns "id," "name," and "age." After executing the query, the changes are committed to the database, and then the cursor and database connection are closed.

# emember to replace placeholders like "localhost," "username," "password," and "databasename" with your actual database connection details.









