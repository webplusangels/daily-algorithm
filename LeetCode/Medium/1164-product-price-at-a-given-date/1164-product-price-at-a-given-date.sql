# Write your MySQL query statement below
SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
)

UNION

SELECT product_id, new_price AS price
FROM (
    SELECT *, MAX(change_date) OVER (PARTITION BY product_id) AS max_date
    FROM Products
    WHERE change_date <= '2019-08-16'
) sub
WHERE max_date = change_date