USE sql_practice

-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
-- body_profile 테이블 생성
CREATE TABLE body_profile(
    name	VARCHAR(40),
    height  INT,
    weight  INT
);

-- body_profile 테이블에 데이터 집어넣기
INSERT INTO body_profile 
VALUES('손흥민', 183, 77);

INSERT INTO body_profile 
VALUES('리오넬 메시', 170, 72);

INSERT INTO body_profile 
VALUES('크리스티아누 호날두', 189, 85);

INSERT INTO body_profile 
VALUES('킬리안 음바페', 178, 75);

INSERT INTO body_profile 
VALUES('엘링 홀란드', 194, 88);

INSERT INTO body_profile 
VALUES('네이마르 주니오르', 175, 68);

COMMIT
-- -------------------------------------------------------------------------------------------------------------


-- 1. 산술 연산자
-- (1) 더하기
SELECT 
	3 + 4 AS result

-- (2) 빼기
SELECT 
	5 - 2 AS result

-- (3) 곱하기
SELECT 
	7 * 3 AS result

-- (4) 나누기
SELECT 
	10 / 2 AS result

-- (5) 나머지
SELECT 
	7 % 2 AS result

-- (6) bmi 계산
SELECT * FROM body_profile;

SELECT 
	name,
	weight / ((height * 0.01) * (height * 0.01)) AS bmi
FROM
	body_profile;

-- (7) 0으로 나누기
-- 수학에서 0으로 나누는 것은 정의되지 않은 연산이다.
-- 따라서 DB에서도 0으로 나누거나 0으로 나눈 나머지를 구하려고 할 경우 NULL이 출력된다.
SELECT 
	10/0 AS result1,
	10%0 AS result2;


-- 2. 비교 연산자
SELECT * FROM customer;

-- (1) = 연산자
-- customer 테이블에서 name이 손흥민인 행만 필터링하여 출력
SELECT 
	* 
FROM 
	customer
WHERE 
	name = '손흥민';

-- (2) > 연산자
-- 참고로 cno의 타입은 VARCHAR이지만, MySQL이 비교 시 문자열 cno 값을 숫자로 암시적 형변환하여 비교한다.
-- customer 테이블에서 cno가 1003보다 큰 행만 필터링하여 출력
SELECT 
	* 
FROM 
	customer 
WHERE 
	cno > 1003;

-- customer 테이블에서 name이 손흥민인 뒤쪽에 위치한 행만 필터링하여 출력
SELECT 
	* 
FROM 
	customer  
WHERE 
	name > '손흥민';

-- customer 테이블에서 가나다 순으로 정렬했을때 name이 손흥민보다 앞쪽에 위치한 행만 필터링하여 출력
SELECT 
	* 
FROM 
	customer  
WHERE 
	name < '손흥민';

-- customer 테이블에서 가나다 순으로 정렬했을때 name이 손흥민보다 뒤쪽에 위치하거나 같은 행만 필터링하여 출력
SELECT 
	* 
FROM 
	customer  
WHERE 
	name >= '손흥민';

-- (3) <> 연산자
-- <> 연산자를 이용하여 name이 손흥민이 아닌 데이터를 출력
SELECT 
	* 
FROM 
	customer 
WHERE 
	name <> '손흥민';


-- 3. 논리 연산자
SELECT * FROM body_profile;

-- (1) AND 연산자
SELECT 
	* 
FROM 
	body_profile
WHERE  
	height = 170 
	AND weight = 72;
	
SELECT 
	* 
FROM 
	body_profile
WHERE 
	height > 180
	AND weight > 80;

-- (2) OR 연산자
SELECT 
	* 
FROM 
	body_profile
WHERE 
	name = '킬리안 음바페'
	OR name = '엘링 홀란드';

SELECT 
	* 
FROM 
	body_profile
WHERE 
	height > 180
	OR weight > 80;

-- (3) NOT 연산자
SELECT 
	* 
FROM 
	body_profile
WHERE 
	NOT height > 180;

SELECT 
	* 
FROM 
	body_profile
WHERE 
	NOT (name = '크리스티아누 호날두' OR name = '리오넬 메시');

-- (4) 연산자 우선순위: NOT > AND > OR 
-- 따라서 height > 180 OR (weight < 80 AND name = '손흥민') 와 같다.
-- 근데 웬만하면 괄호를 사용해서 구분짓자.
SELECT 
	* 
FROM 
	body_profile
WHERE 
	height > 180 
	OR weight < 80 
	AND name = '손흥민';


-- 4. NULL 조건
-- NULL은 항상 fasle를 반환하기 때문에 WHERE birth_date = NULL; 와 같은 비교 연산자(=, <, >, <>)를 사용할 수 없다.
SELECT * FROM customer;

-- (1) IS NULL
SELECT 
	* 
FROM 
	customer 
WHERE 
	birth_date IS NULL;

-- (2) IS NOT NULL
SELECT 
	* 
FROM 
	customer 
WHERE 
	mobile IS NOT NULL;


-- 5. BETWEEN 연산자
-- BETWEEN은 두 값 사이에 있는 데이터를 출력하는 연산자이다.
-- 또한 BETWEEN의 시작 값과 끝 값이 포함된다.
-- AND 연산자와 함께 사용한다.
SELECT * FROM customer;

-- (1) cno BETWEEN 1002 AND 1004
SELECT 
	* 
FROM 
	customer 
WHERE 
	cno BETWEEN 1002 AND 1004;

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	cno >= 1002
	AND cno <= 1004;

-- (2) 가나다 순서대로 유재석과 차은우 사이에 오는 이름 출력
SELECT 
	* 
FROM 
	customer
WHERE 
	name BETWEEN '유재석' AND '차은우';

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	name >= '유재석' 
	AND name <= '차은우';

-- (3) reg_date가 DATE 타입이기 때문에 날짜 순서대로 데이터 출력
SELECT 
	* 
FROM 
	customer
WHERE 
	reg_date BETWEEN '2023-04-01' AND '2023-05-31'

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	reg_date >= '2023-04-01' 
	AND reg_date <= '2023-05-31'

-- (4) 1002 <= cno <= 1004가 아닌 데이터 출력
SELECT 
	* 
FROM 
	customer 
WHERE 
	cno NOT BETWEEN 1002 AND 1004;

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer 
WHERE 
	NOT (cno >= 1002 AND cno <= 1004);

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer 
WHERE 
	cno < 1002 OR cno > 1004;

-- (5) 가나다 순서대로 유재석 <= name <= 차은우가 아닌 데이터 출력
SELECT 
	* 
FROM 
	customer 
WHERE 
	name NOT BETWEEN '유재석' AND '차은우';

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer 
WHERE 
	NOT (name >= '유재석' AND name <= '차은우');

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer 
WHERE 
	name < '유재석' OR name > '차은우';

-- (6) '2023-04-01' AND '2023-05-31' 아닌 데이터 출력
SELECT 
	* 
FROM 
	customer 
WHERE 
	reg_date NOT BETWEEN '2023-04-01' AND '2023-05-31';

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer 
WHERE 
	NOT (reg_date >= '2023-04-01' AND reg_date <= '2023-05-31');

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer 
WHERE 
	reg_date < '2023-04-01' OR reg_date > '2023-05-31';


-- 6. IN 연산자
-- 주어진 리스트 중에 일치하는 데이터가 있는 행을 출력
-- OR 연산자로 대체될 수 있다.
SELECT * FROM customer;

-- (1) cno IN (1002, 1004)
SELECT 
	* 
FROM 
	customer
WHERE 
	cno IN (1002, 1004);

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	cno = 1002 
	OR cno = 1004;

-- (2) cno NOT IN (1002, 1004)
SELECT 
	* 
FROM 
	customer
WHERE 
	cno NOT IN (1002, 1004);

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	NOT (cno = 1002 OR cno = 1004);

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	cno <> 1002 
	AND cno <> 1004;

-- (3) name NOT in ('유재석', '차은우')
SELECT 
	* 
FROM 
	customer
WHERE 
	name NOT in ('유재석', '차은우');

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	NOT (name = '유재석' OR name = '차은우');

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	name <> '유재석' 
	AND name <> '차은우';

-- (4) reg_date NOT IN ('2023-04-03', '2023-05-01')
SELECT 
	* 
FROM 
	customer
WHERE 
	reg_date NOT IN ('2023-04-03', '2023-05-01');

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	NOT (reg_date = '2023-04-03' 
	OR reg_date = '2023-05-01');

-- 위와 똑같다.
SELECT 
	* 
FROM 
	customer
WHERE 
	reg_date <> '2023-04-03' 
	AND reg_date <> '2023-05-01';


-- 7. LIKE 연산자
-- 주어진 패턴을 포함하는 문자를 조회하는 패턴 매칭 조건
-- 와일드카드인 %와 _를 이용하여 기술할 수 있다.
-- S% : S로 시작하는
-- %L : L로 끝나는
-- %Q% : Q가 포함되는
-- S%L : S로 시작해서 L로 끝나는
-- S__ : S로 시작하는 3글자
-- __L : L로 끝나는 3글자
-- _Q_ : 가운데 글자가 Q인 3글자
-- %R_ : 오른쪽 끝에서 두 번째 글자가 R인 => R로 끝나는데 뒤에 한 칸이 더 있는
-- _Q% : 왼쪽 끝에서 두 번째 글자가 Q인 => Q로 시작하는데 앞에 한 칸이 더 있는
SELECT * FROM customer;

-- (1) name에 '은'이 포함되는 데이터 출력
SELECT 
	*
FROM 
	customer 
WHERE 
	name LIKE '%은%';

-- (2) birth_date가 7월인 데이터 출력 <=> 07로 시작하는데 앞에 4칸이 더 있는
SELECT 
	*
FROM 
	customer 
WHERE 
	birth_date LIKE '____07%'

-- 위와 똑같다. <=> 07로 끝나는데 뒤에 2칸이 더 있는
SELECT 
	*
FROM 
	customer 
WHERE 
	birth_date LIKE '%07__'
	
-- (3) name에 '은'이 포함되는 데이터를 제외한 나머지 레코드 출력
SELECT 
	*
FROM 
	customer 
WHERE 
	name NOT LIKE '%은%'

-- (4) birth_date가 7월인 데이터를 제외한 레코드 출력 <=> 07로 시작하는데 뒤에 2칸이 더 있는 애들 제외하고 출력
SELECT 
	*
FROM 
	customer 
WHERE 
	birth_date NOT LIKE '%07__'
	
-- 위와 똑같다. <=> 07로 시작하는데 앞에 4칸이 더 있는 애들 제외하고 출력
SELECT 
	*
FROM 
	customer 
WHERE 
	birth_date NOT LIKE '____07%'
	
