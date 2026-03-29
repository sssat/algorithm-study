USE sql_practice


-- 1번 문제
-- 참고로 FROM에 여러 테이블만 적는 것은 기본적으로 CROSS JOIN 성격이고,
-- FROM에 여러 테이블을 나열한 뒤 WHERE 절에서 테이블 간 연결 조건을 주면 INNER JOIN과 같은 결과가 된다.
SELECT 
	a.member_id,
	b.book_name,
	b.price,
	c.status,
	CASE 
		WHEN c.finish_date IS NULL THEN '배송 예정'
		ELSE c.finish_date
	END AS finish_date
FROM 
	order_info AS a,
	book AS b,
	delivery AS c
WHERE 
	a.book_id = b.book_id
	AND a.order_code = c.order_code;

-- 위와 같다.
SELECT 
	a.member_id,
	b.book_name,
	b.price,
	c.status,
	CASE 
		WHEN c.finish_date IS NULL THEN '배송 예정'
		ELSE c.finish_date
	END AS finish_date
FROM 
	order_info AS a
INNER JOIN
	book AS b 
	ON a.book_id = b.book_id 
INNER JOIN 
	delivery AS c 
	ON a.order_code = c.order_code;

-- IF 절을 사용했을 때
SELECT 
	a.member_id,
	b.book_name,
	b.price,
	c.status,
	IF(c.finish_date IS NOT NULL, c.finish_date, '배송 예정') AS finish_date
FROM 
	order_info AS a,
	book AS b,
	delivery AS c
WHERE 
	a.book_id = b.book_id
	AND a.order_code = c.order_code;
	

-- 2번 문제
-- 여기서도 마찬가지로 FROM에 여러 테이블만 적는 것은 기본적으로 CROSS JOIN 성격이고,
-- FROM에 여러 테이블을 나열한 뒤 WHERE 절에서 테이블 간 연결 조건을 주면 INNER JOIN과 같은 결과가 된다.
-- 같은 책별로 주문 건수를 집계하기 위해 GROUP BY를 사용했다.
-- 즉, book_name과 writer가 같은 행끼리 그룹을 만든 뒤 각 그룹의 주문 수를 COUNT(*)로 계산한다.
SELECT 
	a.book_name,
	a.writer,
	CASE 
		WHEN COUNT(*) >= 3 THEN 'BestSeller'
	END AS best_yn
FROM 
	book AS a,
	order_info AS b
WHERE 
	a.book_id = b.book_id
GROUP BY 
	a.book_name,
	a.writer;

-- 위와 똑같다.
SELECT 
	a.book_name,
	a.writer,
	CASE 
		WHEN COUNT(*) >= 3 THEN 'BestSeller'
	END AS best_yn
FROM 
	book AS a
INNER JOIN
	order_info AS b 
	ON a.book_id = b.book_id
GROUP BY 
	a.book_name,
	a.writer;

-- IF 절을 사용했을 때
SELECT 
	a.book_name,
	a.writer,
	IF(COUNT(*) >= 3, 'BestSeller', NULL) AS best_yn
FROM 
	book AS a,
	order_info AS b
WHERE 
	a.book_id = b.book_id
GROUP BY 
	a.book_name,
	a.writer;
	

-- 3번 문제
-- 아직 모르겠음