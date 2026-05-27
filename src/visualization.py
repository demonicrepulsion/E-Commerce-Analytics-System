import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bhavya@240004012",
    database="ecommerce_analytics"
)

query = """
SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;
"""

df = pd.read_sql(query, connection)

plt.bar(df["product_name"], df["total_quantity_sold"])

plt.xlabel("Products")
plt.ylabel("Quantity Sold")
plt.title("Top Selling Products")

plt.show()