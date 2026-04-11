-- [핵심 아이디어]
-- 이 문제는 우선 8 ~ 10월 동안 CAR_ID별 총 대여 횟수를 구해서
-- 그 중 COUNT(*) >= 5 인 자동차만 고르고
-- 그 자동차들에 대해 다시 월별 COUNT(*)를 구해야 한다.


-- [문제 푼 날짜]
-- 1. 4월 11일 (X) 
-- 2. 4월 25일 ()


SELECT
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE >= '2022-08-01'
    AND START_DATE < '2022-11-01'
    AND CAR_ID IN (
        SELECT
            CAR_ID
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            START_DATE >= '2022-08-01'
            AND START_DATE < '2022-11-01'
        GROUP BY
            CAR_ID
        HAVING
            COUNT(*) >= 5
    )
GROUP BY
    MONTH,
    CAR_ID
ORDER BY
    MONTH ASC,
    CAR_ID DESC;