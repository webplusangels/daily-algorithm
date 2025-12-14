# Write your MySQL query statement below
SELECT name AS results
FROM (
    SELECT u.name, COUNT(*) AS count_id
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY mr.user_id
    ORDER BY count_id DESC, u.name
    LIMIT 1
) sub

UNION ALL

SELECT title AS results
FROM (
    SELECT m.title, AVG(rating) AS avg_score
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE created_at LIKE '2020-02-%'
    GROUP BY mr.movie_id
    ORDER BY avg_score DESC, m.title
    LIMIT 1
) sub