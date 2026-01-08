-- 코드를 입력하세요
WITH Heavy_Users AS (
    SELECT *, COUNT(*) OVER (PARTITION BY HOST_ID) AS cnt_places
    FROM PLACES
)

SELECT ID, NAME, HOST_ID
FROM Heavy_Users
WHERE cnt_places >= 2
ORDER BY ID