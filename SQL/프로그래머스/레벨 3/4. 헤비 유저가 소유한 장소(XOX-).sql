-- [핵심 아이디어]
-- 서브쿼리에서 HOST_ID별 등록 개수를 구한 뒤, 2개 이상 등록한 HOST_ID만 바깥 쿼리에서 조회한다.
-- 이때 WHERE HOST_ID IN (...) 형태이므로, IN 뒤의 서브쿼리는 반드시 컬럼 1개만 반환해야 한다.
-- 또한 FROM 절에 오는 서브쿼리는 반드시 별칭을 지어줘야 하지만 그 외 WHERE, SELECT 절에 오는 서브쿼리에는 별칭을 붙이지 않아도 된다.


-- [문제 푼 날짜]
-- 1. 3월 27일 (X) => 서브 쿼리에 익숙치 않아서 풀지못함
-- 2. 3월 28일 (O)
-- 3. 4월 5일 (X) => 거의 다 맞았는데 HOST_ID IN 뒤의 서브쿼리에서 칼럼을 하나만 반환해야 하는데 HOST_ID, COUNT(*) 2개를 반환해서 틀림
-- 4. 4월 12일 ()


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