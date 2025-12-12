# Write your MySQL query statement below
SELECT person_name
FROM (
    SELECT *, SUM(weight) OVER (
        ORDER BY turn
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS sum_weight
    FROM Queue
) sub
WHERE sum_weight >= 1000
LIMIT 1