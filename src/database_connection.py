import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bhavya@240004012",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

print("Database connected successfully")


