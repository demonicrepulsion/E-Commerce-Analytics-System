DELIMITER //

CREATE PROCEDURE GetCustomerOrders(IN cust_id INT)

BEGIN

SELECT
    order_id,
    order_date,
    total_amount
FROM orders
WHERE customer_id = cust_id;

END //

DELIMITER ;