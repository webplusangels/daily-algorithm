# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM (
    SELECT p.product_name, unit
    FROM Orders o
    JOIN Products p ON o.product_id = p.product_id
    WHERE MONTH(order_date) = 2
) sub
GROUP BY product_name
HAVING unit >= 100