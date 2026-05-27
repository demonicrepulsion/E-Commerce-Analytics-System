SELECT * FROM customers;

SELECT 
    SUM(total_amount) AS total_revenue
FROM orders;

SELECT
    MONTH(order_date) AS month,
    SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY MONTH(order_date);

SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1;