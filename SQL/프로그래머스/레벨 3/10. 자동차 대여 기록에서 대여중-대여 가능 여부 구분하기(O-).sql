-- [핵심 아이디어]
-- 이 문제는 우선 대여중에 해당하는 CAR_ID를 구해야 한다.


-- [문제 푼 날짜]
-- 1. 5월 2일 (O) 29분 14초 OK 
-- 2. 5월 16일 ()


SELECT
    CAR_ID,
    CASE 
        WHEN CAR_ID IN 
        (
            SELECT
                CAR_ID
            FROM 
                CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE
                START_DATE <= '2022-10-16'
                AND END_DATE >= '2022-10-16'
        ) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY
    CAR_ID
ORDER BY
    CAR_ID DESC;