import mysql.connector


alx_book_store = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Poshi011001#",
    database="alx_book_store"
)

print(alx_book_store.get_server_info())