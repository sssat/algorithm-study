USE sql_practice

SELECT * FROM donut_info;

-- 1번 문제
-- donut_info 테이블에서 price 별로 그룹핑 한뒤, 각 price 별로 전체 행의 개수를 구한다음 price 오름차순 출력하는 쿼리
-- 이 문제 또한 GROUP BY와 집계함수가 결합되어 사용된 예시이다.
-- 참고로 COUNT 함수는 COUNT(*) 과 COUNT(medal_type) 처럼 전체 행과 단일 칼럼 둘 다 인자로 들어올 수 있다.
SELECT 	
	price,
	COUNT(*) AS cnt
FROM
	donut_info
GROUP BY
	price
ORDER BY
	price ASC;

-- 2번 문제
-- dormitory_member 테이블에서 room_no 별로 그룹핑 한뒤, 각 room_no 별로 전체 행의 개수를 구한다음 
-- member_cnt을 내림차순 정렬 후, 같은 member_cnt 내에서는 room_no을 오름차순 하여 출력하는 쿼리
-- 이 문제 또한 GROUP BY와 집계함수가 결합되어 사용된 예시이다.
SELECT 
	room_no,
	COUNT(*) AS member_cnt
FROM
	dormitory_member
GROUP BY
	room_no 
ORDER BY 
	member_cnt DESC,
	room_no ASC;

-- 3번 문제
-- dormitory_member 테이블에서 (room_no, grade) 별로 그룹핑 한뒤, 각 (room_no, grade) 별로 전체 행의 개수를 구한다음 
-- room_no를 오름차순 정렬 후, 같은 room_no 내에서는 grade를 오름차순 하여 출력하는 쿼리
SELECT 
	room_no,
	grade,
	COUNT(*) AS member_cnt
FROM
	dormitory_member
GROUP BY
	room_no,
	grade 
ORDER BY 	
	room_no ASC,
	grade ASC;

-- 4번 문제
-- order_info 테이블에서 member_id 별로 그룹핑 한뒤, 각 member_id 별로 전체 행의 개수를 구한다음 book_cnt 내림차순 출력하는 쿼리
SELECT 
	member_id, 
	COUNT(*) book_cnt
FROM
	order_info 
GROUP BY
	member_id 
ORDER BY 
	book_cnt DESC;

-- 5번 문제
-- delivery 테이블에서 finish_date가 NULL인 행들 중에서 status 별로 그룹핑 한뒤, 
-- 각 status 별로 전체 행의 개수를 구한다음 status_cnt가 5 미만인 애들을 오름차순 하여 출력하는 쿼리
SELECT 
	status,
	COUNT(*) status_cnt 
FROM
	delivery 
WHERE 	
	finish_date IS NULL
GROUP BY 
	status
HAVING 
	status_cnt < 5
ORDER BY 
	status_cnt ASC;


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE sales (
    product_id INT,
    sale_date DATE,
    quantity INT
);

INSERT INTO sales VALUES (1001, '2024-01-01', 10);
INSERT INTO sales VALUES (1002, '2024-01-02', 15);
INSERT INTO sales VALUES (1001, '2024-01-03', 5);
INSERT INTO sales VALUES (1003, '2024-01-03', 20);
INSERT INTO sales VALUES (1002, '2024-01-04', 7);
INSERT INTO sales VALUES (1001, '2024-01-05', 12);
INSERT INTO sales VALUES (1003, '2024-01-05', 8);
INSERT INTO sales VALUES (1001, '2024-01-06', 14);
INSERT INTO sales VALUES (1002, '2024-01-07', 18);
INSERT INTO sales VALUES (1003, '2024-01-08', 11);
INSERT INTO sales VALUES (1001, '2024-01-09', 8);
INSERT INTO sales VALUES (1001, '2024-01-10', 17);
INSERT INTO sales VALUES (1002, '2024-01-11', 18);
INSERT INTO sales VALUES (1001, '2024-01-12', 11);
INSERT INTO sales VALUES (1002, '2024-01-13', 20);
INSERT INTO sales VALUES (1002, '2024-01-14', 20);

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


-- 6번 문제
-- sales 테이블에서 sale_date가 해당 날짜 범위에 속한 행들 중에서 sale_date 별로 그룹핑 한뒤, 
-- 각 sale_date 별로 quantity의 합계를 구한다음 sum_sale를 내림차순하여 5개만 출력하는 쿼리
SELECT 
	sale_date,
	SUM(quantity) AS sum_sale
FROM
	sales 
WHERE 
	sale_date >= '2024-01-01'
	AND sale_date <= '2024-01-10'
GROUP BY 
	sale_date
ORDER BY 
	sum_sale DESC
LIMIT 5;

-- 7번 문제
-- sales 테이블에서 product_id 별로 그룹핑 한뒤, 
-- 각 product_id 별로 quantity의 합계를 구한다음 sum_sale를 내림차순하여 출력하는 쿼리
SELECT 
	product_id,
	SUM(quantity) AS sum_sale
FROM
	sales 
GROUP BY
	product_id
ORDER BY 
	sum_sale DESC;

-- 8번 문제
-- sales 테이블에서 sale_date 별로 그룹핑 한뒤, 
-- 각 sale_date 별로 quantity의 합계를 구한다음 sale_date의 개수가 2개 이상인 행들 중에서 sum_sale 오름차순하여 출력하는 쿼리
-- 참고로 GROUP BY에서 사용된 칼럼과 HAVING 절에서 사용되는 칼럼은 같지 않아도 에러 없이 실행된다.
SELECT 
	sale_date,
	SUM(quantity) AS sum_sale
FROM
	sales 
GROUP BY
	sale_date
HAVING 
	COUNT(sale_date) >= 2
ORDER BY 
	sale_date ASC;