-- [핵심 아이디어]
-- 서브쿼리에서 HOST_ID별 등록 개수를 구한 뒤,
-- 2개 이상 등록한 HOST_ID만 바깥 쿼리에서 조회한다.


-- [문제 푼 날짜]
-- 1. 3월 27일 (X) => 서브 쿼리에 익숙치 않아서 풀지못함
-- 2. 3월 28일 (O)
-- 3. 4월 5일 ()


SELECT 
    ID, 
    NAME, 
    HOST_ID
FROM 
    PLACES
WHERE 
    HOST_ID IN 
    (
        SELECT 
            HOST_ID
        FROM 
            PLACES
        GROUP BY 
            HOST_ID
        HAVING 
            COUNT(*) >= 2
    )
ORDER BY 
    ID ASC;