-- [핵심 아이디어]
-- 쿼리 해석순서
-- 1. FROM
-- 2. JOIN
-- 3. WHERE
-- 4. GROUP BY
-- 5. HAVING
-- 6. SELECT
-- 7. DISTINCT
-- 8. ORDER BY
-- 9. LIMIT

-- 또한 SELECT 절에서 집계 함수가 아닌 칼럼은 GROUP BY에 넣어야 한다.
-- 예를들어 이건 가능하다.
-- SELECT FOOD_TYPE, MAX(FAVORITES)
-- FROM REST_INFO
-- GROUP BY FOOD_TYPE

-- 그러나 이건 불가능하다.
-- 여기서 REST_ID는 집계 함수도 아니고 GROUP BY에도 없기 때문이다.
-- SELECT FOOD_TYPE, REST_ID, MAX(FAVORITES)
-- FROM REST_INFO
-- GROUP BY FOOD_TYPE

-- 따라서 SELECT 절에서 집계 함수가 아닌 칼럼은 전부 GROUP BY에 넣어야 한다.
-- 아니면 에러가 나거나, 의미가 애매한 쿼리가 된다.


-- [문제 푼 날짜]
-- 1. 3월 30일 (X) => JOIN 절에 오는 서브 쿼리는 테이블처럼 취급된다. 그래서 반드시 별칭이 필요하다.
-- 2. 3월 31일 (X) => 서브 쿼리에 테이블 별칭을 안붙였고 서브 쿼리 내부의 FROM에 별칭을 붙여버림
-- 3. 4월 8일 (X)
-- 4. 4월 15일 ()


SELECT 
    A.FOOD_TYPE, 
    A.REST_ID, 
    A.REST_NAME, 
    A.FAVORITES
FROM 
    REST_INFO AS A
INNER JOIN 
    (
        SELECT 
            FOOD_TYPE, 
            MAX(FAVORITES) AS MAX_FAVORITES
        FROM 
            REST_INFO
        GROUP BY 
            FOOD_TYPE
    ) AS B
    ON A.FOOD_TYPE = B.FOOD_TYPE
    AND A.FAVORITES = B.MAX_FAVORITES
ORDER BY
    A.FOOD_TYPE DESC;