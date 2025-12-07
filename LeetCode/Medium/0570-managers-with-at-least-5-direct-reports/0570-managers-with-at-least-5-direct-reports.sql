# Write your MySQL query statement below
-- managerId를 세서 5개 이상인 name을 출력
SELECT e2.name
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
GROUP BY e2.id, e2.name
HAVING COUNT(e2.id) >= 5