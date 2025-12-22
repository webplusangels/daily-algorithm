# Write your MySQL query statement below
-- 부서에서 연봉 3위 이내
SELECT Department, Employee, Salary
FROM (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS ranks
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) sub
WHERE ranks <= 3