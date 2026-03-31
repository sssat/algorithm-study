-- [문제 푼 날짜]
-- 1. 3월 30일 (X) => JOIN 절에 오는 서브 쿼리는 테이블처럼 취급된다. 그래서 반드시 별칭이 필요하다.
-- 2. 3월 31일 (X) => 서브 쿼리에 테이블 별칭을 안붙였고 서브 쿼리 내부의 FROM에 별칭을 붙여버림
-- 3. 4월 7일 ()


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