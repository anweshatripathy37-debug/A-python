import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="22011975",
    host="localhost",
    port=3306
)

print("connected")