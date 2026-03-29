USE sql_practice

-- 1번 문제
SELECT 
	a.book_name,
	a.writer,
	a.price
FROM 
	book AS a
WHERE NOT EXISTS (
	SELECT 
		1
	FROM
		order_info AS b
	WHERE 
		a.book_id = b.book_id
);

-- 위와 똑같다.
SELECT 
	a.book_name,
	a.writer,
	a.price
FROM
	book AS a
WHERE
	a.book_id NOT IN (
		SELECT
			b.book_id
		FROM
			order_info AS b
	);

-- 2번 문제
SELECT 
	a.member_id,
	a.order_date,
	(
		SELECT 
			b.status
		FROM 
			delivery AS b
		WHERE 
			a.order_code = b.order_code
	) AS status
FROM 
	order_info AS a
WHERE 
	a.order_date = '2024-01-10' 
	OR a.order_date = '2024-01-11'
ORDER BY 
	a.order_date ASC,
	a.member_id ASC;

-- 위와 똑같다.
-- SELECT 절에 쓰인 스칼라 서브쿼리는 LEFT OUTER JOIN과 논리적 동작 방식이 동일하기 때문에 INNER JOIN이 아니라 LEFT OUTER JOIN과 같다.
SELECT 
	a.member_id,
	a.order_date,
	b.status
FROM 
	order_info AS a
LEFT OUTER JOIN
	delivery AS b 
	ON a.order_code = b.order_code
WHERE 
	a.order_date = '2024-01-10' 
	OR a.order_date = '2024-01-11'
ORDER BY 
	a.order_date ASC,
	a.member_id ASC;


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE offline_class (
    class_no    VARCHAR(4),
    class_name    VARCHAR(20),
    teacher    VARCHAR(10),
    capacity    INT
);

CREATE TABLE online_class (
    class_no    VARCHAR(4),
    class_name    VARCHAR(20),
    teacher    VARCHAR(10),
    capacity    INT
);


INSERT INTO offline_class VALUES ('A101','천연 화장품 만들기','류미인',20);
INSERT INTO offline_class VALUES ('A102','아침 건강 요가','백진주',15);
INSERT INTO offline_class VALUES ('A103','원어민 영어 놀이터','신남정',10);
INSERT INTO offline_class VALUES ('A104','수채화 그리기','오미지',20);
INSERT INTO offline_class VALUES ('A105','세무사가 알려주는 상속과 증여','박동국',15);
INSERT INTO offline_class VALUES ('A106','부수입을 위한 체험단 블로그','한혜인',20);
INSERT INTO offline_class VALUES ('A107','SNS마케팅 활용','장현주',20);
INSERT INTO offline_class VALUES ('A108','메타인지 학습법','김성준',15);


INSERT INTO online_class VALUES ('B101','꽃풍선 만들기','이지현',20);
INSERT INTO online_class VALUES ('B102','아침 건강 요가','백진주',15);
INSERT INTO online_class VALUES ('B103','부수입을 위한 이모티콘 만들기','유주영',20);
INSERT INTO online_class VALUES ('B104','수채화 그리기','오미지',20);
INSERT INTO online_class VALUES ('B105','세무사가 알려주는 상속과 증여','박동국',15);
INSERT INTO online_class VALUES ('B106','부수입을 위한 체험단 블로그','한혜인',20);
INSERT INTO online_class VALUES ('B107','SNS마케팅 활용','장현주',20);
INSERT INTO online_class VALUES ('B108','영화같은 브이로그 만들기','안슬기',20);

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


-- 3번 문제
SELECT 
	a.class_name,
	a.teacher,
	a.capacity
FROM 
	offline_class AS a
WHERE EXISTS (
	SELECT 
		1
	FROM 
		online_class AS b 
	WHERE 
		a.class_name = b.class_name
);

-- 위와 똑같다.
SELECT 
	a.class_name,
	a.teacher,
	a.capacity
FROM 
	offline_class AS a
WHERE
	a.class_name IN (
		SELECT 
			b.class_name
		FROM 
			online_class AS b 	
	);