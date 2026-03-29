USE sql_practice


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE tokyo_olympic (
    item    VARCHAR(10),
    team    VARCHAR(3),
    player    VARCHAR(20),
    medal_type    VARCHAR(10),
    medal_cnt    INT
);

INSERT INTO tokyo_olympic VALUES('양궁','KOR','San An','금',3);
INSERT INTO tokyo_olympic VALUES('양궁','KOR','Je Deok Kim','금',2);
INSERT INTO tokyo_olympic VALUES('양궁','KOR','Woojin Kim','금',1);
INSERT INTO tokyo_olympic VALUES('양궁','KOR','Jin Hyek Oh','금',1);
INSERT INTO tokyo_olympic VALUES('양궁','TUR','Kete Gazoz','금',1);
INSERT INTO tokyo_olympic VALUES('양궁','ROC','Elena Osipova','은',2);
INSERT INTO tokyo_olympic VALUES('양궁','ROC','Ksenia Perova','은',1);
INSERT INTO tokyo_olympic VALUES('양궁','ROC','Svetlana Gomboeva','은',1);
INSERT INTO tokyo_olympic VALUES('양궁','TPE','Chih-Chun Tang','은',1);
INSERT INTO tokyo_olympic VALUES('양궁','NED','Gabriela Bayardo','은',1);
INSERT INTO tokyo_olympic VALUES('양궁','JPN','Takaharu Furukawa','동',2);
INSERT INTO tokyo_olympic VALUES('양궁','MEX','Luis Alvarez','동',1);
INSERT INTO tokyo_olympic VALUES('양궁','GER','Lisa Unruh','동',1);
INSERT INTO tokyo_olympic VALUES('양궁','JPN','Yuki Kawata','동',1);
INSERT INTO tokyo_olympic VALUES('양궁','ITA','Lucilla Boari','동',1);

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


-- 1. 단일 칼럼 정렬
-- ORDER BY 구문의 옵션으로는 오름차순(ASC)과 내림차순(DESC)이 있는데 기본값은 오름차순(ASC) 이며
-- 옵션 생략 시 데이터는 오름차순(ASC)으로 정렬된다.
-- OREDER BY 구문은 모든 데이터가 SELECT 된 뒤 마지막에 수행되며 
-- ORDER BY 구문이 없을 시 데이터는 랜덤순으로 출려된다.
SELECT * FROM tokyo_olympic;

-- (1) player 알파벳 순서로 오름차순(ASC) 정렬
SELECT
  *
FROM
  tokyo_olympic
ORDER BY
  player ASC;
 
 -- (2) medal_cnt 기준으로 내림차순(DESC) 정렬
SELECT
  *
FROM
  tokyo_olympic
ORDER BY
	medal_cnt DESC;


-- (3) birth_date 기준으로 내림차순(DESC) 정렬
-- 참고로 NULL은 최소값으로 취급되기 때문에 오름차순(ASC) 하면 가장 앞에 오고 내림차순(DESC) 하면 가장 마지막에 온다.
SELECT * FROM customer;

-- 내림차순(DESC)
SELECT
  *
FROM
  customer
ORDER BY
	birth_date DESC;

-- 오름차순(ASC)
SELECT
  *
FROM
  customer
ORDER BY
	birth_date ASC;

-- (4) birth_date가 NULL인 데이터를 맨 앞에 위치시키고, 남은 birth_date를 기준으로 내침차순(DESC) 정렬한다.
-- 만약 NULL 데이터를 맨 앞이나 맨 뒤에 위치시키고 싶다면 아래 옵션을 별도로 주어야 한다.
--   1) 칼럼 IS NULL ASC  : NULL인 데이터를 맨 뒤에 위치시킨다.
--   2) 칼럼 IS NULL DESC : NULL인 데이터를 맨 앞에 위치시킨다.
SELECT
  *
FROM
  customer
ORDER BY
	birth_date IS NULL DESC, 
	birth_date DESC;

-- (주의) birth_date IS NULL DESC를 뒤에 쓰면 1차 정렬 기준이 이미 birth_date DESC이므로, birth_date IS NULL DESC가 적용되지 않는다.
SELECT
  *
FROM
  customer
ORDER BY
	birth_date DESC,
	birth_date IS NULL DESC;

-- (5) mobile이 NULL인 데이터를 맨 뒤에 위치시키고, 남은 mobile을 기준으로 내침차순(DESC) 정렬한다.
-- 하지만 mobile DESC 하면 NULL 값이 맨 뒤에 오기 때문에 mobile IS NULL ASC 없어도 결과는 똑같다.
SELECT
  *
FROM
  customer
ORDER BY
	mobile IS NULL ASC, 
	mobile DESC;


-- 2. 다중 칼럼 정렬
-- 다중 칼럼 정렬을 하기 위해선 ORDER BY 절에 두 개 이상의 칼럼을 지정해야 한다.
-- 각 칼럼에는 옵션을 별개로 설정할 수 있고, 먼저 적은 칼럼 순서대로 우선순위가 부여된다.

-- (1) medal_type을 기준으로 오름차순(ASC) 정렬 한 후, 각 medal_type에 대해 medal_cnt로 내림차순(DESC) 정렬하여 출력
-- 참고로 OREDR BY 절에서 오름차순(ASC)은 키워드를 명시하지 않아도 기본값으로 작용한다.
SELECT * FROM tokyo_olympic; 

SELECT
  *
FROM
  tokyo_olympic
ORDER BY
	medal_type, 
	medal_cnt DESC;

-- (2) medal_cnt를 기준으로 내림차순(DESC) 한 뒤, 각 medal_cnt에 대하여 player 알파벳 순으로 오름차순(ASC) 하여 출력
SELECT
  item,
  player,
  medal_cnt
FROM
  tokyo_olympic
ORDER BY
	medal_cnt DESC,
 	player;


-- 3. LIMIT 절
-- LIMIT 절은 출력할 데이터의 행의 개수를 지정할 수 있다.
SELECT * FROM tokyo_olympic;

-- (1) tokyo_olympic 테이블의 전체 데이터 중에서 7개만 출력
SELECT 
	*
FROM 
	tokyo_olympic 
LIMIT 7;

-- (2) medal_cnt를 기준으로 내림차순(DESC) 한 뒤, 상위 5개의 데이터만 출력
SELECT 
	*
FROM 
	tokyo_olympic 
ORDER BY
	medal_cnt DESC 
LIMIT 5;

-- 4. OFFSET 절
-- 중간에 위치한 행을 출력하고자 한다면 OFFSET 키워드를 사용할 수 있다.

-- (1) medal_cnt를 기준으로 내림차순(DESC) 한 뒤, 1번째 데이터부터 5개 데이터만 출력 (1번 ~ 6번 데이터 출력)
SELECT 
	*
FROM 
	tokyo_olympic 
ORDER BY
	medal_cnt DESC 
LIMIT 5 OFFSET 0;

-- (2) medal_cnt를 기준으로 오름차순(ASC) 한 뒤, 각 medal_cnt에 대하여 player 알파벳 순으로 내림차순(DESC) 하여 
--     4번째 데이터부터 3개 데이터만 출력 (4번 ~ 6번 데이터 출력)
SELECT 
	*
FROM 
	tokyo_olympic 
ORDER BY
	medal_cnt,
	player DESC
LIMIT 3 OFFSET 3;