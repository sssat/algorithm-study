-- sql_practice 데이터베이스를 사용하겠다는 뜻
-- 이건 맨 처음에 한 번만 하면된다.
USE sql_practice  


-- 0. customer 테이블 생성
CREATE TABLE customer (
  cno        VARCHAR(4),
  name       VARCHAR(10),
  birth_date VARCHAR(8),
  mobile     VARCHAR(11),
  reg_date   DATE
);

-- customer 테이블에 데이터 집어넣기
INSERT INTO customer 
VALUES(1001, '손흥민', '19920708', '01000001111', '2023-04-03');

INSERT INTO customer 
VALUES(1002, '유재석', NULL, '01011112222', '2023-05-01');

INSERT INTO customer 
VALUES(1003, '이지은', '19930516', '01022223333', '2023-06-12');

INSERT INTO customer 
VALUES(1004, '김연아', '19900905', NULL, '2023-08-20');

INSERT INTO customer 
VALUES(1005, '차은우', '19970330', '01044445555', '2023-12-25');


-- 1. customer 테이블 전체 조회
SELECT * FROM customer;


-- 2.customer 테이블에서 특정 칼럼만 조회
SELECT 
	cno, 
	name, 
	birth_date
FROM 
	customer;


-- 3.customer 테이블에서 특정 칼럼만 조회 -> 2번이랑 동일하게 작동
SELECT 
	customer.cno, 
	customer.name, 
	customer.BIRTH_DATE 
FROM 
	customer;


-- 4. AS 키워드를 사용하여 칼럼 및 테이블에 별칭 지정. 테이블에는 AS 키워드 생략함
SELECT 
	c.cno, 
	c. name, 
	c.birth_date AS btdt 
FROM 
	customer c;


-- 5. 한글 AS를 사용시 ""로 감싸줘야 한다.
SELECT 
	cno AS "회원번호",
	name AS "이름",
	birth_date AS "생년월일"
FROM
	customer;


-- 6. NULL vs 문자 'NULL'
SELECT 
	NULL AS col1,
    'NULL' AS col2;
