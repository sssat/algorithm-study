-- [핵심 아이디어]
-- CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT)처럼
-- SELECT에서 파일 경로를 문자열로 합쳐 출력하더라도, 원본 컬럼인 FILE_ID를 기준으로 정렬할 수 있다.

-- 서브쿼리 안에 LIMIT를 쓸 때,
-- 프로그래머스 MySQL 환경에서는 BOARD_ID IN (서브쿼리 LIMIT 1) 형태가 지원되지 않을 수 있다.
-- 따라서 조회수 1등 게시글 하나만 찾는 경우에는 IN 대신 = 를 사용한다.

-- HAVING은 GROUP BY 없이도 사용할 수 있다.


-- [문제 푼 날짜]
-- 1. 5월 5일 (X) => MAX(VIEWS)와 HAVING의 의미를 잘못 이해했고, IN + LIMIT 조합으로 MySQL 버전 에러 발생
-- 2. 5월 19일 ()


SELECT
    CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM
    USED_GOODS_FILE
WHERE
    BOARD_ID = (
        SELECT
            BOARD_ID
        FROM
            USED_GOODS_BOARD
        ORDER BY
            VIEWS DESC
        LIMIT 1
    )
ORDER BY
    FILE_ID DESC;