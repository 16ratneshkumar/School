import mysql.connector as mysql
# Replace the placeholders with your actual MySQL database details
host = "localhost"
user = "your_username(default is root)"
password = "your_Mysql_password"
database = "your_database_name"
# connect to the mysql server
connection = mysql.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)
# check if the connection is successful
if connection.is_connected():
    # is_connected is a Built-in method to check your connection is establish or not.
    print("Successfully connected to your mysql server")

else:
    print("Failed to connect to the mysql server")
# Perform your database operations here
# Don't forgot to close the connection
connection.close()