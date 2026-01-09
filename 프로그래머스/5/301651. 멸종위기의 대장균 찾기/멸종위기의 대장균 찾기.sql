-- 코드를 작성해주세요
WITH RECURSIVE Generations AS (
    SELECT ID, PARENT_ID, 1 AS GEN
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT e.ID, e.PARENT_ID, g.GEN + 1
    FROM ECOLI_DATA e
    INNER JOIN Generations g ON g.ID = e.PARENT_ID
),
Distinct_Parent AS (
    SELECT GEN, COUNT(*) AS cnt, COUNT(DISTINCT PARENT_ID) AS dist_cnt
    FROM Generations
    GROUP BY GEN
)

# SELECT *
# FROM Distinct_Parent

SELECT cnt - LEAD(dist_cnt, 1, 0) OVER (ORDER BY GEN) AS COUNT, GEN AS GENERATION
FROM Distinct_Parent