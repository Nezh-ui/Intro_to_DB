import mysql.connector
from mysql.connector import Error

cursor = None
connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",      
        password="Poshi011001#"   
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("MySQL connection is closed.")