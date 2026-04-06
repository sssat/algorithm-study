-- [문제 푼 날짜]
-- 1. 3월 28일 (X)
-- 2. 3월 29일 (O)
-- 3. 4월 6일 (O) => 쿼리는 맞았는데 DATE_FORMAT 함수랑 CASE END문 사용법이 생각안나서 서칭함
-- 4. 4월 13일 ()


SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
    CASE
        WHEN OUT_DATE IS NULL THEN '출고미정'
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        ELSE '출고대기'
    END AS 출고여부
FROM 
    FOOD_ORDER
ORDER BY 
    ORDER_ID ASC;