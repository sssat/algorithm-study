USE sql_practice

-- ----------------------------------------------- 테이블 삭제 -------------------------------------------------------
DROP TABLE kpop;
DROP TABLE billboard;

-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE kpop (
    ranking    INT,
    song       VARCHAR(50),
    singer     VARCHAR(20)
);

INSERT INTO kpop VALUES(1,'Super Shy','NewJeans');
INSERT INTO kpop VALUES(2,'Seven','정국');
INSERT INTO kpop VALUES(3,'ETA','NewJeans');
INSERT INTO kpop VALUES(4,'퀸카(Queencard)','(여자)아이들');
INSERT INTO kpop VALUES(5,'I AM','IVE');
INSERT INTO kpop VALUES(6,'헤어지자 말해요','박재정');
INSERT INTO kpop VALUES(7,'이브, 프시케 그리고 푸른 수염의 아내','Le SSERAFIM');
INSERT INTO kpop VALUES(8,'Spicy','aespa');
INSERT INTO kpop VALUES(9,'Steal The Show','Lauv');
INSERT INTO kpop VALUES(10,'NewJeans','NewJeans');


CREATE TABLE billboard (
    ranking    INT,
    song       VARCHAR(50),
    singer     VARCHAR(40)
);

INSERT INTO billboard VALUES(1,'Seven','정국');
INSERT INTO billboard VALUES(2,'Meltdown','Travis Scott');
INSERT INTO billboard VALUES(3,'FE!N','Travis Scott');
INSERT INTO billboard VALUES(4,'What Was I Made For?','Billie Eilish');
INSERT INTO billboard VALUES(5,'LaLa','Myke Towers');
INSERT INTO billboard VALUES(6,'Dance The Night','Dua Lipa');
INSERT INTO billboard VALUES(7,'Barbie World','Nicki Minaj and Ice Spice With Aqua');
INSERT INTO billboard VALUES(8,'Super Shy','NewJeans');
INSERT INTO billboard VALUES(9,'K-POR','Travis Scott');
INSERT INTO billboard VALUES(10,'Hyaena','Travis Scott');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------

-- (참고)
-- 바깥 쿼리 해석 순서 및 실행 순서는 다음과 같다.
-- FROM(JOIN + ON) -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
-- WHERE는 행을 필터링하는 역할이다.
-- 단, 서브쿼리는 항상 맨 먼저 해석되는 것이 아니라, 포함된 절에서 함께 해석한다.
-- 예를 들어 서브쿼리가 WHERE 절에 들어 있다면, 우선 FROM 절이 해석되고 그 다음 WHERE 절에서 조건을 평가할 때 서브쿼리도 함께 처리된다고 이해하면 된다.
-- CASE WHEN 구문 또한 독립적인 절이 아니라 표현식이므로, 작성된 절(SELECT, WHERE, ORDER BY 등)의 해석 순서에서 함께 처리된다.

-- 또한 쿼리 작성 순서는 다음과 같다.
-- SELECT - FROM - JOIN ON - WHERE - GROUP BY - HAVING - ORDER BY


-- 1. INNER JOIN
-- INNER JOIN은 두 테이블에 모두 존재하는 데이터를 출력하는데 사용된다.
-- INNER JOIN은 수학의 교집합 개념과 비슷하며 한쪽 테이블에는 있지만 다른 쪽 테이블에는 없는 데이터는 출력되지 않는다. => 다이어그램에서 교집합 그림을 떠올리자
-- ON에는 칼럼을 기준으로 두 테이블을 어떤 기준으로 연결(매칭)할 것인지 정의한다.
-- 이때 두 테이블의 칼럼명이 꼭 같을 필요는 없지만, 보통은 양쪽 테이블에서 서로 대응되는 칼럼을 기준으로 조건을 작성한다.

-- SELECT
-- 	  col1, 
-- 	  col2
-- FROM
-- 	  left_table
-- INNER JOIN
-- 	  right_table
--    ON left_table.col = right_table.col;
-- (참고) JOIN 문에서 FROM에 오는 테이블은 왼쪽 테이블 이고, JOIN 뒤에 오는 테이블은 오른쪽 테이블이다.
	
SELECT * FROM kpop;
SELECT * FROM billboard; 

-- (1) kpop 테이블(왼쪽 테이블)과 billboard 테이블(오른쪽 테이블)에서 song 칼럼의 값이 같은 행 출력
SELECT
    A.ranking AS kpop_ranking,
    B.ranking AS billboard_ranking,
    A.song,
    A.singer
FROM
    kpop AS A  
INNER JOIN
    billboard AS B
    ON A.song = B.song;
   
-- (2) 위와 똑같다.
-- (참고) FROM에 여러개의 테이블을 명시하는것이 가능하다.
SELECT
    A.ranking AS kpop_ranking,
    B.ranking AS billboard_ranking,
    A.song,
    A.singer
FROM
    kpop AS A,
    billboard AS B
WHERE 
	A.song = B.song;


-- 2. OUTER JOIN
-- OUTER JOIN은 두 테이블을 연결할 때, 조인 조건(ON)의 만족 여부와 관계없이 기준이 되는 한쪽 테이블의 모든 행을 출력할 때 사용한다.
-- 이때 기준 테이블이 왼쪽이면 LEFT OUTER JOIN, 오른쪽이면 RIGHT OUTER JOIN을 사용한다.
-- 또한 OUTER JOIN은 단독으로 OUTER JOIN으로만 쓰이지 않고 LEFT OUTER JOIN이나 RIGHT OUTER JOIN으로만 쓰인다.
-- OUTER JOIN에서도 마찬가지로 ON에는 칼럼을 기준으로 두 테이블을 어떤 기준으로 연결(매칭)할 것인지 정의한다.
-- 또한 이때도 두 테이블의 칼럼명이 꼭 같을 필요는 없지만, 보통은 양쪽 테이블에서 서로 대응되는 칼럼을 기준으로 조건을 작성한다.

-- (1) LEFT OUTER JOIN
-- 왼쪽 테이블은 모든 행이 출력되고, 오른쪽 테이블은 JOIN에 성공한 행만 출력된다.
-- 다이어그램에서 왼쪽 다이어그램은 전부 칠해져있지만 오른쪽 다이어그램은 왼쪽과 겹치는 부분만 칠해져있다.

-- SELECT
-- 	  col1, 
-- 	  col2
-- FROM
-- 	  left_table
-- LEFT OUTER JOIN
-- 	  right_table
--    ON left_table.col = right_table.col;

SELECT * FROM kpop;
SELECT * FROM billboard; 

-- 1) kpop 테이블(왼쪽 테이블)과 billboard 테이블(오른쪽 테이블)에서 song 칼럼이 같은 행을 출력하는데, 
--    kpop 테이블(왼쪽 테이블)의 행은 전부 출력하고 billboard 테이블(오른쪽 테이블)은 ON A.song = B.song 조건에 맞는 행만 출력한다.
--    만약 ON 조건에 맞는 오른쪽 테이블의 행이 없으면 NULL로 출력된다.
SELECT 
	A.ranking AS kpop_ranking,
	B.ranking AS billboard_ranking,
	A.song,
	A.singer
FROM 
	kpop AS A 
LEFT OUTER JOIN
	billboard AS B
	ON A.song = B.song;

-- 2) kpop 테이블(왼쪽 테이블)과 billboard 테이블(오른쪽 테이블)에서 song 칼럼이 같은 행을 출력하는데, 
--    kpop 테이블(왼쪽 테이블)의 행은 전부 출력하고 billboard 테이블(오른쪽 테이블)은 ON A.song = B.song 조건에 맞는 행만 출력한다.
--    만약 ON 조건에 맞는 오른쪽 테이블의 행이 없으면 NULL로 출력되지만 NULL 행이 있다면 제외하고 출력한다.
--    참고로 위의 INNER JOIN과 똑같은 결과가 출력된다.
SELECT 
	A.ranking AS kpop_ranking,
	B.ranking AS billboard_ranking,
	A.song,
	A.singer
FROM 
	kpop AS A 
LEFT OUTER JOIN
	billboard AS B
	ON A.song = B.song
WHERE
	B.ranking IS NOT NULL;
	
-- (2) RIGHT OUTER JOIN
-- 오른쪽 테이블은 모든 행이 출력되고, 왼쪽 테이블은 JOIN에 성공한 행만 출력한다. 
-- 다이어그램에서 오른쪽 다이어그램은 전부 칠해져있지만 왼쪽 다이어그램은 오른쪽과 겹치는 부분만 칠해져있다.

-- SELECT
-- 	  col1, 
-- 	  col2
-- FROM
-- 	  left_table
-- RIGHT OUTER JOIN
-- 	  right_table
--    ON left_table.col = right_table.col;

SELECT * FROM kpop;
SELECT * FROM billboard; 

-- 1) kpop 테이블(왼쪽 테이블)과 billboard 테이블(오른쪽 테이블)에서 song 칼럼이 같은 행을 출력하는데, 
--    billboard 테이블(오른쪽 테이블)의 행은 전부 출력하고 kpop 테이블(왼쪽 테이블)은 ON A.song = B.song 조건에 맞는 행만 출력한다.
--    만약 ON 조건에 맞는 왼쪽 테이블의 행이 없으면 NULL로 출력된다.
SELECT 
	A.ranking AS kpop_ranking,
	B.ranking AS billboard_ranking,
	B.song,
	B.singer
FROM 
	kpop AS A 
RIGHT OUTER JOIN
	billboard AS B
	ON A.song = B.song;
	
-- 2) kpop 테이블(왼쪽 테이블)과 billboard 테이블(오른쪽 테이블)에서 song 칼럼이 같은 행을 출력하는데, 
--    billboard 테이블(오른쪽 테이블)의 행은 전부 출력하고 kpop 테이블(왼쪽 테이블)은 ON A.song = B.song 조건에 맞는 행만 출력한다.
--    만약 ON 조건에 맞는 왼쪽 테이블의 행이 없으면 NULL로 출력되지만 NULL 행이 있다면 제외하고 출력한다.
--    위의 INNER JOIN과 똑같은 결과가 출력된다.
SELECT 
	A.ranking AS kpop_ranking,
	B.ranking AS billboard_ranking,
	B.song,
	B.singer
FROM 
	kpop AS A 
RIGHT OUTER JOIN
	billboard AS B
	ON A.song = B.song
WHERE 
	A.ranking IS NOT NULL;
	

-- 3. CROSS JOIN
-- CROSS JOIN은 두 테이블 간의 가능한 모든 조합을 출력하는데 사용된다.
-- CROSS JOIN은 별도의 JOIN 조건 없이 왼쪽 테이블과 오른쪽 테이블의 모든 행을 한 번씩 연결지어 출력하는 형태의 JOIN이다.
-- 쉽게말해 왼쪽 테이블의 모든 행 x 오른쪽 테이블의 모든 행을 전부 조합해서 결과를 출력하는 카티션 프로덕트다.
-- 예를들어 왼쪽 테이블의 행이 3개이고 오른쪽 테이블의 행이 4개라면 총 3 x 4 = 12개의 행이 출력된다.
-- 또한 CROSS JOIN은 조건없는 모든 조합이기 때문에 ON이 존재하지 않는다.

-- SELECT
-- 	  *
-- FROM
--    left_table
-- CROSS JOIN
--	  right_table;

-- 또는 아래와 같은 문법으로도 CROSS JOIN을 구현할 수 있다.
-- SELECT
-- 	  col1,
--    col2
-- FROM
--    left_table,
--    right_table


-- ----------------------------------------------- 테이블 삭제 -------------------------------------------------------
DROP TABLE kpop;
DROP TABLE billboard;

-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE kpop (
    ranking    INT,
    song       VARCHAR(50),
    singer     VARCHAR(20)
);

INSERT INTO kpop VALUES(1,'Super Shy','NewJeans');
INSERT INTO kpop VALUES(2,'Seven','정국');
INSERT INTO kpop VALUES(3,'ETA','NewJeans');


CREATE TABLE billboard (
    ranking    INT,
    song       VARCHAR(50),
    singer     VARCHAR(40)
);

INSERT INTO billboard VALUES(1,'Super Shy','정국');
INSERT INTO billboard VALUES(2,'Meltdown','Travis Scott');
INSERT INTO billboard VALUES(3,'FE!N','Travis Scott');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------

SELECT * FROM kpop; 
SELECT * FROM billboard;

-- 1) kpop 테이블과 billboard 테이블의 데이터를 CROSS JOIN 하여 출력 
-- 현재 kpop 테이블에 데이터가 3행, billboard 테이블에 데이터가 3행 있으므로
-- 가능한 모든 조합을 출력하면 총 3 X 3 = 9개의 행이 출력된다.
SELECT 
	A.ranking AS k_ranking,
	B.ranking AS b_ranking,
	A.song AS k_song,
	B.song AS b_song,
	A.singer AS k_singer,
	B.singer AS b_singer
FROM
	kpop AS A
CROSS JOIN
	billboard AS B;
	
-- 2) 위와 똑같다.
SELECT 
	A.ranking AS k_ranking,
	B.ranking AS b_ranking,
	A.song AS k_song,
	B.song AS b_song,
	A.singer AS k_singer,
	B.singer AS b_singer
FROM
	kpop AS A,
	billboard AS B;