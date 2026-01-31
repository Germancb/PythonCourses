import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="germancbp",
  password="Gerco#9371",
  database="classicalmodels"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("DROP TABLE IF EXISTS customers")
# DROP TABLE IF EXISTS customers


# Create a cursor object
mycursor = mydb.cursor()

# SQL query to create a table
create_table_query = """
CREATE TABLE customers (
  customerNumber int(11) NOT NULL,
  customerName varchar(50) NOT NULL,
  contactLastName varchar(50) NOT NULL,
  contactFirstName varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  city varchar(50) NOT NULL,
  state varchar(50) DEFAULT NULL,
  postalCode varchar(15) DEFAULT NULL,
  country varchar(50) NOT NULL,
  salesRepEmployeeNumber int(11) DEFAULT NULL,
  creditLimit decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (customerNumber),
  KEY salesRepEmployeeNumber_idx (salesRepEmployeeNumber),
  CONSTRAINT customers_ibfk_1  FOREIGN KEY (salesRepEmployeeNumber) REFERENCES employees (employeeNumber)
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









