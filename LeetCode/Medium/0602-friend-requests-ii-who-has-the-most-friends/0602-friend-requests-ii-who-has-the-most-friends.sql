# Write your MySQL query statement below
SELECT id, COUNT(id) AS num
FROM (
    SELECT *
    FROM (
        SELECT requester_id AS id
        FROM RequestAccepted
    ) sub

    UNION ALL

    SELECT *
    FROM(
        SELECT accepter_id AS id
        FROM RequestAccepted
    ) sub
) outersub
GROUP BY id
ORDER BY num DESC
LIMIT 1