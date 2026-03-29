USE sql_practice


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE student (
    id    VARCHAR(20),
    name    VARCHAR(15),
    mobile    VARCHAR(11)
);

CREATE TABLE winner_list (
    ranking   INT,
    id    VARCHAR(20)
);

INSERT INTO student VALUES ('apple', '김사과', '01011110000');
INSERT INTO student VALUES ('banana', '박나나', '01022220000');
INSERT INTO student VALUES ('strawberry', '신딸기', '01033330000');
INSERT INTO student VALUES ('lemon', '오레몬', '01044440000');
INSERT INTO student VALUES ('carrot', '주당근', '01055550000');

INSERT INTO winner_list VALUES (1, 'strawberry');
INSERT INTO winner_list VALUES (2, 'lemon');
INSERT INTO winner_list VALUES (3, 'banana');

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


-- 0. 서브쿼리
-- SQL은 기본적으로는 하나의 쿼리 블록으로 이루어지지만, 때에 따라서는 여러 개의 쿼리 블록으로 구성될 수 있다.
-- 이런 경우 바깥에 있는 쿼리를 메인 쿼리(Main query), 안쪽에 있는 쿼리를 서브 쿼리(Subquery)라고 부른다.
-- 또한 서브쿼리는 위치에 따라 다음과 같이 나뉜다.
-- (1) 스칼라 서브쿼리(Scalar Subquery): SELECT 절
-- (2) 인라인 뷰(Inline View): FROM 절
-- (3) 중첩 서브쿼리(Nested Subquery): WHERE 절, HAVING 절


-- 1. 스칼라 서브쿼리
-- 스칼라 서브쿼리는 하나의 값(1행 1열)만을 반환하는 서브 쿼리를 의미하며
-- 주로 SELECT 절에서 많이 사용되며, 단일 값이 올 수 있는 위치에서 사용할 수 있다.
-- 참고로 여기서 말하는 단일 값이란 아래 예시에서의 01033330000, 01044440000, 01022220000 등과 같은 값 하나를 말한다.
SELECT * FROM student;
SELECT * FROM winner_list;

-- (1) winner_list 테이블에서 ranking과, student 테이블의 id와 winner_list 테이블의 id가 대응되는 학생의 폰 번호를 출력하는 쿼리
-- 이 쿼리를 보면 student 테이블의 id와 winner_list 테이블의 id가 = 조건으로 연결되어 있다.
-- 즉, 메인 쿼리의 winner_list 테이블과 서브쿼리의 student 테이블이 서로 관계를 맺고 있으므로 이 쿼리는 연관 서브쿼리이다.
-- 또한 이 서브쿼리는 SELECT 절에서 사용되며, 각 행마다 하나의 값(1행 1열)만 반환하고 있으므로 스칼라 서브쿼리이다.

-- 연관 서브쿼리: 메인 쿼리의 값을 참조하는 서브쿼리
-- 비연관 서브쿼리: 메인 쿼리와 독립적으로 실행되는 서브쿼리
SELECT
    A.ranking,
    (
        SELECT
            B.mobile
        FROM
            student AS B
        WHERE
            B.id = A.id
    ) AS mobile
FROM
    winner_list AS A;
   
-- (2) 스칼라 서브쿼리 실패 예시
-- 스칼라 서브쿼리는 하나의 값만 반환해야 한다. 즉, 반환 결과는 1행 1열이어야 한다.
-- 만약 이처럼 서브쿼리가 여러 행을 반환하면, 스칼라 서브쿼리 위치에서는 사용할 수 없으므로 에러가 발생한다.
-- 참고로 여기서의 서브쿼리는 비연관 서브쿼리인데,
-- 그 이유는 현재 메인 쿼리의 winner_list 테이블과 서브 쿼리의 students 테이블이 아무런 관계를 맺지 않고 있기 때문이다.
SELECT 
	ranking,
	(
		SELECT 
			mobile 
		FROM
			students 
	) AS mobile
FROM 
	winner_list;
    
-- (3) winner_list 테이블에서 ranking과, student 테이블의 id와 winner_list 테이블의 id가 대응되는 학생의 폰 번호와 이름을 출력하는 쿼리
-- 이처럼 메인 쿼리의 SELECT 절 안에 여러 개의 스칼라 서브쿼리를 작성할 수도 있다.
-- 하지만 이 같은 쿼리는 동일한 테이블(student)에 두 번 접근 하게 되므로 성능상 바람직하지 않다. 
-- 따라서 이런 경우는 스칼라 서브쿼리를 사용하기 보다 JOIN을 활용하는 것이 성능상 더 유리하다.
SELECT 
	a.ranking,
	(
		SELECT 
			mobile
		FROM
			student b 
		WHERE 
			b.id = a.id 
	) AS mobile,
	(
		SELECT 
			name
		FROM
			student b
		WHERE 
			b.id = a.id 
	) AS name
FROM 
	winner_list AS a;
	
-- JOIN을 사용한 경우. 결과는 위와 똑같다.
SELECT 
	a.ranking,
	b.mobile,
	b.name
FROM
	winner_list AS a
LEFT OUTER JOIN
	student AS b 
	ON a.id = b.id;
	

-- 2. 인라인 뷰
-- 인라인 뷰는 FROM 절, 즉 테이블 명이 오는 자리에 대입하여 사용되며 주로 메인 쿼리에서 참조되는 가상의 테이블로 간주된다.
-- 일반적으로 인라인 뷰를 사용하면 쿼리의 가독성이 향상되며, WITH 절을 사용하여 공통 테이블 표현식(CTE)으로 정의할 수도 있다.
-- 공통 테이블 표현식(CTE) 이란 "WITH 절로 만드는, 쿼리 안에서만 잠깐 사용하는 이름 붙은 임시 결과표" 이다.

-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE product (
    product_no    VARCHAR(4),
    product_name    VARCHAR(20),
    price    INT
);

CREATE TABLE payment (
    payment_no    VARCHAR(8),
    member_id    VARCHAR(10),
    product_no    VARCHAR(4)
);

INSERT INTO product VALUES ('S100', '미니선풍기', 3500);
INSERT INTO product VALUES ('S101', '행운목', 2000);
INSERT INTO product VALUES ('S102', '야광텀블러', 6500);
INSERT INTO product VALUES ('S103', '포도당캔디', 3000);
INSERT INTO product VALUES ('S104', '아로마오일', 10000);

INSERT INTO payment VALUES ('24010101', 'tree25', 'S100');
INSERT INTO payment VALUES ('24010102', 'sky1004', 'S100');
INSERT INTO payment VALUES ('24010103', 'frog555', 'S102');
INSERT INTO payment VALUES ('24010104', 'cup14', 'S103');
INSERT INTO payment VALUES ('24010105', 'tree25', 'S104');
INSERT INTO payment VALUES ('24010106', 'phone99', 'S104');
INSERT INTO payment VALUES ('24010107', 'bear1070 ', 'S102');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


SELECT * FROM product;
SELECT * FROM payment; 

-- (1) payment 테이블에서 member_id가 'tree25'인 행들의 product_no로 인라인 뷰를 만든 뒤,
--     product 테이블 a의 product_no와 인라인 뷰 b의 product_no가 같은 행의 상품명을 출력하는 쿼리
SELECT 	
	a.product_name
FROM
	product AS a,
	(
		SELECT
			product_no
		FROM
			payment
		WHERE 
			member_id = 'tree25'
	) AS b 
WHERE 
	a.product_no = b.product_no;

-- 위와 똑같다.
SELECT 
	a.product_name
FROM
	product AS a,
	payment AS b 
WHERE 
	a.product_no = b.product_no
	AND b.member_id = 'tree25';

-- 위와 똑같다.
SELECT 
	a.product_name
FROM 
	product AS a 
INNER JOIN
	payment AS b 
	ON a.product_no = b.product_no 
WHERE 
	b.member_id = 'tree25'
	
-- (2) WITH 절을 사용하여 공통 테이블 표현식(CTE)으로 정의
--     payment 테이블에서 아이디가 'tree25'인 product_no를 먼저 구해서 이 결과에 cte_order_info라는 이름을 붙인 후 => WITH 절
--     product 테이블과 cte_order_info CTE에서 product_no이 같은 product_name을 출력하는 쿼리
--     이처럼 WITH 절을 사용하면 복잡한 쿼리를 단순화하고 가독성을 향상시킬 수 있다.
WITH cte_order_info AS (
    SELECT
        product_no
    FROM
        payment
    WHERE
        member_id = 'tree25'
)

SELECT
    a.product_name
FROM
    product AS a,
    cte_order_info AS b
WHERE
    a.product_no = b.product_no;
    

-- 3. 중첩 서브쿼리
-- 중첩 서브쿼리는 WHERE 절이나 HAVING 절 안에 포함되어 조건 비교에 사용되는 서브쿼리이다.
-- 중첩 서브쿼리는 메인 쿼리와의 관계 유무에 따라 연관 서브쿼리와 비연관 서브쿼리로 나눌 수 있다.
-- 이는 스칼라 서브쿼리와 인라인 뷰도 마찬가지로 연관과 비연관으로 구분할 수 있다.
   
-- 연관 서브쿼리: 메인 쿼리와 관계 있음
-- 비연관 서브쿼리: 메인 쿼리와 관계 없음 + 독립적으로 실행이 가능함


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE departments (
    department_id    INT,
    department_name    VARCHAR(30)
);

CREATE TABLE employees (
    employee_id    INT,
    employee_name    VARCHAR(20),
    salary    INT,
    department_id    INT
);

INSERT INTO departments VALUES (10, '데이터분석팀');
INSERT INTO departments VALUES (20, 'DB기술팀');
INSERT INTO departments VALUES (30, '클라우드팀');
INSERT INTO departments VALUES (40, 'AI팀');
INSERT INTO departments VALUES (50, '시스템개발팀');

INSERT INTO employees VALUES (100, '이익준', 9000, 10);
INSERT INTO employees VALUES (101, '안정원', 8000, 20);
INSERT INTO employees VALUES (102, '김준완', 8500, 30);
INSERT INTO employees VALUES (103, '양석형', 7000, 40);
INSERT INTO employees VALUES (104, '채송화', 9000, 50);
INSERT INTO employees VALUES (105, '장겨울', 6000, 10);
INSERT INTO employees VALUES (106, '종세혁', 7200, 20);
INSERT INTO employees VALUES (107, '황지우', 6500, 30);
INSERT INTO employees VALUES (108, '김건', 7500, 40);
INSERT INTO employees VALUES (109, '최세훈', 6000, 50);

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


-- (1) 연관 서브쿼리
-- 연관 서브쿼리는 주로 메인 쿼리의 칼럼 값을 기반으로 동적으로 수행되는 형태의 서브쿼리이다.
-- 서브쿼리의 WHERE 절에 메인 쿼리와의 관계가 존재한다.
-- 연관 서브쿼리는 메인 쿼리의 각 행마다 서브쿼리가 수행되며, 메인 쿼리의 칼럼 값에 따라 서브쿼리의 결과 데이터가 달라진다.

SELECT * FROM departments;
SELECT * FROM employees;

-- 1) employees 테이블에서 서브쿼리(각 직원이 속한 부서의 평균 연봉)보다 큰 연봉을 받는 직원의 employee_name, salary 칼럼을 출력하는 쿼리
SELECT
    A.employee_name,
    A.salary
FROM
    employees AS A
WHERE
    A.salary > (
        SELECT
            AVG(B.salary)
        FROM
            employees AS B
        WHERE
            B.department_id = A.department_id
    );
    
-- 2) departments 테이블에서 서브쿼리(해당 부서에 속한 직원 중 급여가 7000 미만인 직원)가 1행이라도 존재하면 해당 조건을 만족하는 아이디와 이름을 출력하는 쿼리
-- EXISTS 구문은 서브쿼리의 결과 데이터가 1행이라도 존재하면 TRUE를 반환하고 그렇지 않으면 FALSE를 반환한다.
-- 따라서 SELECT에 뭐가 오든 중요하지 않고 행의 존재 여부만 확인하기 때문에 관례적으로 의미 없는 상수값 1을 SELECT에 작성하는 경우가 많다.
SELECT
    D.department_id,
    D.department_name
FROM
    departments AS D
WHERE EXISTS (
    SELECT
        1
    FROM
        employees AS E
    WHERE
        E.department_id = D.department_id
        AND E.salary < 7000
);

-- (2) 비연관 서브쿼리
-- 비연관 서브쿼리는 메인 쿼리와 직접적인 관계 없이 독립적으로 수행되는 형태의 서브쿼리이다.
-- 서브쿼리의 WHERE 절에 메인 쿼리와의 관계가 존재하지 않는다.

SELECT * FROM employees;

-- 1) employees 테이블에서 연봉이 가장 큰 직원의 이름과 연봉을 출력하는 쿼리
--    이 쿼리를 살펴보면 서브 쿼리 내부에 메인 쿼리의 칼럼이 존재하지 않고 서브쿼리가 독립적으로 수행되는 것을 보아 비연관 서브쿼리임을 알 수 있다.
SELECT
    employee_name,
    salary
FROM
    employees
WHERE
    salary = ( 
        SELECT
            MAX(salary)
        FROM
            employees
    );
    
-- 2) employees 테이블에서 연봉이 평균보다 큰 직원의 이름과 연봉을 출력하는 쿼리
--    여기서는 같은 테이블이라도 쿼리 안에서 맡는 역할이 다르기 때문에 다른 별칭을 썼다.
--    문법적으로 꼭 달라야 하는 상황이라기보다, 가독성과 구분을 위해 다르게 쓴 것이다.
--    또한 이 쿼리는 서브쿼리 내부에서 메인 쿼리의 칼럼을 참조하지 않고, 서브쿼리가 독립적으로 수행되므로 비연관 서브쿼리이다.
SELECT
    A.employee_name,
    A.salary
FROM
    employees AS A
WHERE
    A.salary > (
        SELECT
            AVG(B.salary)
        FROM
            employees AS B
    );