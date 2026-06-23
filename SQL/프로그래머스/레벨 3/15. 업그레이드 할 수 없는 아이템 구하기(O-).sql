-- [핵심 아이디어]
-- IN 안에 NULL이 있는 것 자체는 가능하다.
-- 하지만 NOT IN 안에 NULL이 있으면 결과가 의도와 다르게 나올 수 있다.
-- 그래서 NOT IN 서브쿼리에서는 NULL을 제거하는 게 안전하다.


-- [문제 푼 날짜]
-- 1. 5월 9일 (O) 11분 5초 OK
-- 2. 5월 23일 () 


SELECT
    ITEM_ID,
    ITEM_NAME,
    RARITY
FROM
    ITEM_INFO
WHERE
    ITEM_ID NOT IN 
    (
        SELECT
            PARENT_ITEM_ID
        FROM
            ITEM_TREE
        WHERE
            PARENT_ITEM_ID IS NOT NULL
    )
ORDER BY
    ITEM_ID DESC;
