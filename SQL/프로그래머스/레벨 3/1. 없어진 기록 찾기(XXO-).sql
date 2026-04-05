-- [핵심 아이디어]
-- WHERE A.ANIMAL_ID IS NULL 자체는 A 테이블에서 ANIMAL_ID 값이 NULL인 행들만 필터링 하는 것이지만,
-- 여기에서 처럼 LEFT OUTER JOIN과 함께 쓰이면 의미가 조금 달라진다.
-- 왜냐하면 LEFT OUTER JOIN을 하게되면 ON 조건에 ID가 동일한 행들만 출력하도록 되어있어도 LEFT 테이블의 행은 전부 출력하기 때문이다.

-- 따라서 LEFT OUTER JOIN을 하면 결과가 다음과 같아진다.
-- B.ANIMAL_ID	B.NAME	A.ANIMAL_ID
-- A349733	    Allie	NULL
-- A352713	    Gia	    A352713
-- A349990	    Spice	NULL

-- 위의 결과 값을 보고 싶으면 아래와 같이 출력하면 된다.
-- SELECT
--     B.ANIMAL_ID,
--     B.NAME,
--     A.ANIMAL_ID
-- FROM
--     ANIMAL_OUTS AS B
-- LEFT OUTER JOIN
--     ANIMAL_INS AS A
--     ON A.ANIMAL_ID = B.ANIMAL_ID;

-- 이때 그리고 이때 WHERE A.ANIMAL_ID IS NULL을 적용하면 A.ANIMAL_ID 값이 NULL인 행들만 필터링 되므로 최종적으로 아래와 같아진다.
-- B.ANIMAL_ID	B.NAME	A.ANIMAL_ID
-- A349733	    Allie	NULL
-- A349990	    Spice	NULL


-- [문제 푼 날짜]
-- 1. 3월 20일 (x)
-- 2. 3월 27일 (X) => LEFT OUTER JOIN이 먼저 실행되고 그 다음 WHERE가 실행된다.
-- 3. 4월 5일 (O)
-- 4. 4월 12일 ()


-- 정석 풀이
SELECT
    B.ANIMAL_ID,
    B.NAME
FROM
    ANIMAL_OUTS AS B
LEFT OUTER JOIN
    ANIMAL_INS AS A
    ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE
    A.ANIMAL_ID IS NULL
ORDER BY
    B.ANIMAL_ID ASC;