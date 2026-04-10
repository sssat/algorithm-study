-- [문제 푼 날짜]
-- 1. 3월 31일 (X) 
-- 2. 4월 1일 (O)
-- 3. 4월 10일 (O)
-- 4. 4월 24일 ()


-- 정석 풀이
-- 일반적인 JOIN(INNER/LEFT/RIGHT)은 반드시 연결 조건이 필요하고, 보통 ON으로 쓴다.
SELECT
    A.CATEGORY,
    SUM(B.SALES) AS TOTAL_SALES
FROM
    BOOK AS A
INNER JOIN 
    BOOK_SALES AS B
    ON A.BOOK_ID = B.BOOK_ID
WHERE
    B.SALES_DATE >= '2022-01-01'
    AND B.SALES_DATE <= '2022-01-31'
GROUP BY
    A.CATEGORY
ORDER BY
    A.CATEGORY ASC;


-- 3번째로 푼 풀이
-- JOIN 절에 들어가있는 서브쿼리는 FROM 절에 들어가있는 서브쿼리와 마찬가지로 테이블 취급하기 때문에 반드시 별칭을 붙여줘야 한다.
-- 또한 기본적인 SQL 절 순서는 지켜야 오류가 발생하지 않는다.
-- SELECT
-- FROM
-- JOIN
-- ON
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY
SELECT
    A.CATEGORY,
    SUM(B.TOTAL_SALES) AS TOTAL_SALES
FROM
    BOOK AS A
INNER JOIN
    (
        SELECT
            BOOK_ID,
            SUM(SALES) AS TOTAL_SALES
        FROM
            BOOK_SALES
        WHERE
            SALES_DATE >= '2022-01-01'
            AND SALES_dATE <= '2022-01-31'
        GROUP BY
            BOOK_ID
    ) AS B
ON A.BOOK_ID = B.BOOK_ID
GROUP BY
    A.CATEGORY
ORDER BY
    A.CATEGORY ASC;
