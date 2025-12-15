# Write your MySQL query statement below
SELECT *
FROM (
    SELECT visited_on, 
    SUM(sum_amount) OVER (
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
    ROUND(
        SUM(sum_amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) / 7, 2
        ) AS average_amount
    FROM (
        SELECT visited_on, SUM(amount) AS sum_amount, COUNT(*) AS sum_count
        FROM Customer
        GROUP BY visited_on
    ) sub
) subb 
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    FROM Customer
)