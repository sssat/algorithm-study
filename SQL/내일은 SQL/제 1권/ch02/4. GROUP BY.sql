USE sql_practice

-- (참고)
-- 바깥 쿼리 해석 순서 및 실행 순서는 다음과 같다.
-- FROM(JOIN + ON) -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
-- WHERE는 행을 필터링하는 역할이다.
-- 단, 서브쿼리는 항상 맨 먼저 해석되는 것이 아니라, 포함된 절에서 함께 해석한다.
-- 예를 들어 서브쿼리가 WHERE 절에 들어 있다면, 우선 FROM 절이 해석되고 그 다음 WHERE 절에서 조건을 평가할 때 서브쿼리도 함께 처리된다고 이해하면 된다.
-- CASE WHEN 구문 또한 독립적인 절이 아니라 표현식이므로, 작성된 절(SELECT, WHERE, ORDER BY 등)의 해석 순서에서 함께 처리된다.

-- 또한 쿼리 작성 순서는 다음과 같다.
-- SELECT - FROM - JOIN ON - WHERE - GROUP BY - HAVING - ORDER BY


-- 1. GROUP BY 절
-- GROUP BY 절은 데이터를 동일한 그룹끼리 묶는 데 사용된다.
-- 참고로 GROUP BY 절을 작성할 때 주의해야 할 점은 SELECT 절에 명시된 칼럼은 GROUP BY 절에도 반드시 추가해야 한다는 점이다.
-- SELECT 절에 명시된 칼럼 중 GROUP BY 절에 추가하지 않아도 되는 칼럼은 집계 함수(SUM, COUNT, AVG, MAX, MIN 등)내부에서 사용된 칼럼 밖에 없다.
-- 또한 집계 함수에 대한 데이터를 WHERE 절을 사용해 필터링하려고 하면 오류가 발생한다.
-- 따라서 집계 결과를 필터링할때는 WHERE 절 대신 HAVING 절을 사용해야한다.

SELECT * FROM tokyo_olympic;

-- (1) team을 기준으로 그룹핑하여 출력
SELECT 
	team
FROM
	tokyo_olympic
GROUP BY 
	team;

-- (2) DISTINCT 키워드
-- DISTINCT는 중복된 데이터를 제거하여 출력하고자 할 때 사용되는 구문이다.
-- DISTINCT 키워드 다음에 오는 칼럼의 개수에 따라 의미가 달라진다.
-- 예를들어 DISTINCT col1, col2는 (col1, col2) 데이터 셋의 중복을 제거하고 출력한다.
SELECT 
	DISTINCT team
FROM 
	tokyo_olympic;

-- 비교를 위해 DISTINCT 없이 team 출력
SELECT 
	team
FROM 
	tokyo_olympic;

-- (3) GROUP BY 절은 종종 집계 함수(SUM, COUNT, AVG, MIN, MAX 등)와 결합하여 사용된다.
-- tokyo_olympic 테이블의 데이터를 team 별로 그룹핑 한 뒤, 각 그룹(team)별로 메달 개수 합계(SUM)를 출력하는 쿼리
-- 여기서 team 칼럼은 GROUP BY 절에 반드시 존재해야 하지만, 집계 함수 내부에서 사용되는 medal_cnt 칼럼은 GROUP BY 절에 없어도된다.
-- 참고로 SUM() 함수에는 인자 한개만 들어갈 수 있다. 예를들어 SUM(medal_cnt), SUM(price), SUM(price * quantity) 이런 칼럼들은 인자로 들어갈 수 있지만
-- SUM(*), SUM(medal_cnt, price) 와 같은 인자들은 들어갈 수 없다.
SELECT
	team,
	SUM(medal_cnt) AS medal_cnt
FROM
	tokyo_olympic
GROUP BY
	team;
	
-- (4) tokyo_olympic 테이블의 데이터를 team 별로 그룹핑 한 뒤, 각 그룹(team)별로 메달 개수 합계(SUM)를 구한다음 내림차순(DESC) 정렬해 출력하는 쿼리
-- 이 문제 또한 GROUP BY와 집계함수가 결합되어 사용된 예시이다.
SELECT 
	team,
	SUM(medal_cnt) AS medal_cnt
FROM
	tokyo_olympic
GROUP BY
	team
ORDER BY
	medal_cnt DESC;
	

-- (5) tokyo_olympic 테이블의 데이터를 (team, medal_type) 데이터 셋 별로 그룹핑 한 뒤, 각 그룹(team, medal_type) 별로 메달 개수 합계(SUM)를 출력하는 쿼리
-- 현재 tokyo_olympic 테이블은 각 팀별로 금메달만 있거나 은메달만 있거나 동메달만 있어서 현재 출력결과의 medal_type이 금/은/동 중 하나만 나오지만
-- 만약 KOR 팀에 금도 있고 은도 있다면 출력은 아래와 같이 나올 수 있다.
-- KOR | 금 | 4
-- KOR | 은 | 3
-- 이 문제 또한 GROUP BY와 집계함수가 결합되어 사용된 예시이다.

SELECT 
	team,
	medal_type,
	SUM(medal_cnt) AS medal_cnt
FROM 
	tokyo_olympic
GROUP BY
	team,
	medal_type;
	
-- (6) tokyo_olympic 테이블의 데이터를 (team, medal_type) 데이터 셋 별로 그룹핑 한 뒤, 
--     각 그룹(team, medal_type) 별로 메달 개수 합계(SUM)를 집계한 뒤,
--     medal_type을 알파벳 순으로 가나다 순으로 오름차순 정렬 후, 같은 medal_type 내에서는 medal_cnt를 내림차순 하여 출력하는 쿼리
-- 이 문제 또한 GROUP BY와 집계함수가 결합되어 사용된 예시이다.
SELECT 
	team,
	medal_type,
	SUM(medal_cnt) AS medal_cnt
FROM 
	tokyo_olympic
GROUP BY
	team,
	medal_type
ORDER BY
	medal_type ASC,
	medal_cnt DESC;
	

-- 2. HAVING 절
-- HAVING 절은 집계 함수에 대한 조건을 설정하는 기능을 제공한다.
-- 집계 함수에 대한 데이터를 WHERE 절을 사용해 필터링하려고 하면 오류가 발생하기 때문에 집계 결과를 필터링할때는 WHERE 절 대신 HAVING 절을 사용해야한다.
-- 또한 HAVING 절에는 medal_type = '금'과 같은 일반 조건이 아니라 집계 함수에 대한 조건을 작성하는 것이 일반적(관례)이다.

SELECT * FROM tokyo_olympic;

-- (1) tokyo_olympic 테이블의 데이터를 team 별로 그룹핑 한 뒤, 각 그룹(team)별로 메달 개수 합계(SUM)를 출력하는데, medal_cnt의 합계(SUM)가 1보다 큰 그룹만 출력하는 쿼리
-- (참고) SUM 함수로 데이터의 합을 계산할 때는 medal_cnt의 칼럼의 값이 NULL인 행은 제외하고 계산을 하게된다.
--       이는 다른 집계 함수를 사용할때도 동일하게 적용된다.
SELECT 
	team,
	SUM(medal_cnt) AS medal_cnt
FROM
	tokyo_olympic 
GROUP BY
	team
HAVING 
	SUM(medal_cnt) > 1;

-- (2) tokyo_olympic 테이블의 데이터를 team 별로 그룹핑 한 뒤, 
--     각 그룹(team)별로 메달 개수 합계(SUM)를 출력하는데, medal_cnt의 합계(SUM)가 1보다 큰 그룹만 오름차순으로 출력하는 쿼리
SELECT 
	team,
	SUM(medal_cnt) AS medal_cnt
FROM
	tokyo_olympic 
GROUP BY
	team
HAVING 
	SUM(medal_cnt) > 1
ORDER BY
	medal_cnt ASC;
	
-- (3) tokyo_olympic 테이블의 데이터 중 medal_type이 '금'인 행을 먼저 필터링 한뒤
--     team 별로 그룹핑 하고, 각 그룹(team)별로 메달 개수 합계(SUM)를 출력하는데, medal_cnt의 합계(SUM)가 1보다 큰 그룹만 출력하는 쿼리
SELECT 
	team,
	SUM(medal_cnt) AS medal_cnt
FROM
	tokyo_olympic 
WHERE 
	medal_type = '금'
GROUP BY
	team
HAVING 
	SUM(medal_cnt) > 1;