USE sql_practice


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE member_info (
    member_no    INT,
    name    VARCHAR(10),
    gender    VARCHAR(1)
);

INSERT INTO member_info VALUES (10, '이장현', 'M');
INSERT INTO member_info VALUES (20, '유길채', 'F');
INSERT INTO member_info VALUES (30, '남연준', 'M');
INSERT INTO member_info VALUES (40, '경은애', 'F');
INSERT INTO member_info VALUES (50, '량음', 'M');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


-- (참고)
-- 바깥 쿼리 해석 순서 및 실행 순서는 다음과 같다.
-- FROM(JOIN + ON) -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
-- WHERE는 행을 필터링하는 역할이다.
-- 서브쿼리는 항상 맨 먼저 해석되는 것이 아니라, 포함된 절에서 함께 해석한다.
-- 예를 들어 서브쿼리가 WHERE 절에 들어 있다면, 우선 FROM 절이 해석되고 그 다음 WHERE 절에서 조건을 평가할 때 서브쿼리도 함께 처리된다고 이해하면 된다.
-- CASE WHEN 구문 또한 독립적인 절이 아니라 표현식이므로, 작성된 절(SELECT, WHERE, ORDER BY 등)의 해석 순서에서 함께 처리된다.

-- 쿼리 작성 순서는 다음과 같다.
-- SELECT - FROM - JOIN ON - WHERE - GROUP BY - HAVING - ORDER BY


-- 1. CASE WHEN 구문
-- CASE WHEN 구문은 조건에 따라 결과를 다르게 반환하고자 할 때 사용하는 구문이다.
-- 첫 번째 조건부터 차례대로 충족이 되는지 안되는지 여부를 판단하는데 
-- 만약 TRUE로 판단이 되는 조건을 만나면 읽기를 중지하고 결과를 반환하지만 그렇지 않을 경우 ELSE 절의 값을 반환한다.
-- 그리고 만약 ELSE 구문이 없고 TRUE인 조건이 없는 경우라면 NULL을 반환한다.
-- 또한 CASE WHEN 구문은 단순형 CASE 문과 검색형 CASE 문이 있는데 이 중에서 검색형 CASE문이 더 많이 쓰인다.

SELECT * FROM member_info;

-- (1) 단순형 CASE 문
-- member_info 테이블에서 이름(name)과 성별(gender)을 한글로 바꾼 결과를 출력하는 쿼리

-- CASE gender: gender 값을 기준으로 아래 조건에 따라 값을 변환한다.
-- WHEN 'F' THEN '여자': gender 값이 'F'이면 '여자'로 출력한다.
-- WHEN 'M' THEN '남자': gender 값이 'M'이면 '남자'로 출력한다.
-- ELSE '해당없음': 위 조건에 모두 해당하지 않거나 값이 NULL이면 '해당없음'으로 출력한다.
-- END AS gender: CASE문의 끝을 나타내며, 변환된 결과 칼럼에 gender라는 별칭을 붙인다.
SELECT 
	name, 
	CASE gender
		WHEN 'F' THEN '여자'
		WHEN 'M' THEN '남자'
		ELSE '해당없음'
	END AS gender 
FROM
	member_info;

-- (2) 검색형 CASE 문
-- 같은 결과를 검색형 CASE 문으로 표현한 쿼리이다.
-- 검색형 CASE 문이 단순형 CASE 문 보다 더 직관적으로 이해하기 쉽다.
-- 또한 실무와 문제풀이에서는 검색형 CASE 문이 더 자주 사용된다.
SELECT
	name, 
	CASE
		WHEN gender = 'F' THEN '여자'
		WHEN gender = 'M' THEN '남자'
		ELSE '해당없음'
	END AS gender 
FROM 
	member_info;


-- 2. IF 구문
-- IF 구문도 CASE WHEN 구문과 마찬가지로 조건에 따라 다른 값을 반환하는 구문이다.
-- IF 절의 기본 문법은 다음과 같다.

-- IF(condition, value_if_true, value_if_false)
-- condition: 충족 여부를 판단하기 위해 주오진 조건
-- value_if_true: 조건을 충족할 경우의 반환값
-- value_if_false: 조건을 충족하지 않을 경우의 반환값

-- IF 절은 CASE WHEN 절에 비해 간단하지만 하나의 조건만 사용 가능하다는 특징이 있다.
-- 반면 CASE WHEN은 조금 더 복잡한 구조를 가지고 있지만 여러 조건들에 대한 처리가 가능하다. 
-- 한마디로 간단한 조건을 처리하는 경우에는 IF 절을 사용하고, 복잡한 조건을 처리하는 경우에는 CASE WHEN 절을 이용하는 것이 효율적이다.

SELECT * FROM member_info;

-- (1) member_info 테이블에서 이름과 성별이 F 라면 '여자'로 출력하고 아니라면 '남자'로 출력하는 쿼리
SELECT 
	name,
	IF(gender = 'F', '여자', '남자') AS gender 
FROM
	member_info;