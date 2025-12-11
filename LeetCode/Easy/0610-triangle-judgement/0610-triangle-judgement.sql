# Write your MySQL query statement below
SELECT x, y, z, 
    IF(x + y + z - GREATEST(x, y, z) < GREATEST(x, y, z), 'No', 'Yes') AS triangle
FROM Triangle