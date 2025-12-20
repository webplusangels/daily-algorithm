# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT *, 
        COUNT(*) OVER (PARTITION BY lat, lon) AS cnt,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_cnt
    FROM Insurance
) sub
WHERE cnt = 1 AND tiv_cnt > 1