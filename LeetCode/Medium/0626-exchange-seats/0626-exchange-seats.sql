# Write your MySQL query statement below
SELECT IF(new_id, new_id, id) as id, student
FROM (
    SELECT *, IF(id % 2, LEAD(id) OVER (), LAG(id) OVER ()) AS new_id
    FROM Seat
) sub
ORDER BY id