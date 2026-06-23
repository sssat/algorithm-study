-- [핵심 아이디어]
-- CONCAT: 문자열을 이어주는 함수
-- SUBSTR: 문자열을 추출하는 함수


-- [문제 푼 날짜]
-- 1. 5월 4일 (X) => 문자열 함수를 몰라서 틀림. 찾아보고 나서는 맞음
-- 2. 5월 5일 ()


SELECT
    B.USER_ID,
    B.NICKNAME,
    CONCAT(B.CITY, ' ', B.STREET_ADDRESS1, ' ', B.STREET_ADDRESS2) AS 전체주소,
    CONCAT(SUBSTR(B.TLNO, 1, 3), '-', SUBSTR(B.TLNO, 4, 4), '-', SUBSTR(B.TLNO, 8, 4)) AS 전화번호
FROM
    USED_GOODS_USER AS B
INNER JOIN 
    (
        SELECT
            WRITER_ID
        FROM
            USED_GOODS_BOARD
        GROUP BY
            WRITER_ID
        HAVING
            COUNT(*) >= 3
    ) AS A
    ON A.WRITER_ID = B.USER_ID
ORDER BY
    B.USER_ID DESC;