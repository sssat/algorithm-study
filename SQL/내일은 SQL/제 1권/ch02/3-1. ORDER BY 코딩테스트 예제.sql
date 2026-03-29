USE sql_practice

-- 1번 문제
SELECT 
	name,
	price,
	reg_date
FROM
	donut_info 
ORDER BY
	reg_date DESC 
LIMIT 5;

-- 2번 문제
SELECT 
	name,
	price,
	description
FROM
	donut_info 
ORDER BY
	price DESC,
	name ASC 
LIMIT 2;

-- 3번 문제
SELECT 
	name,
	nutrition,
	allergy
FROM
	donut_info 
WHERE 
	price >= 1500
	AND price <= 2000
ORDER BY
	allergy IS NULL ASC,
	allergy ASC;

-- 4번 문제
SELECT 
	book_name,
	writer,
	price
FROM
	book 
WHERE 
	price >= 10000
ORDER BY 
	price ASC
LIMIT 5;


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE dormitory_info (
	room_no    VARCHAR(3),
	room_type	VARCHAR(1),
	head_count    INT
);

CREATE TABLE dormitory_member (
	name    VARCHAR(15),
	major    VARCHAR(20),
	gender    VARCHAR(1),
	grade    INT,
	room_no    VARCHAR(3)  
);

INSERT INTO dormitory_info VALUES('101','M',2);
INSERT INTO dormitory_info VALUES('102','M',4);
INSERT INTO dormitory_info VALUES('103','F',2);
INSERT INTO dormitory_info VALUES('104','F',4);
INSERT INTO dormitory_info VALUES('201','M',2);
INSERT INTO dormitory_info VALUES('202','M',4);
INSERT INTO dormitory_info VALUES('203','F',2);
INSERT INTO dormitory_info VALUES('204','F',4);

INSERT INTO dormitory_member VALUES('정만수','컴퓨터공학','M',4,'101');
INSERT INTO dormitory_member VALUES('정경식','국어국문','M',4,'101');
INSERT INTO dormitory_member VALUES('이민재','전자전기','M',2,'102');
INSERT INTO dormitory_member VALUES('마이클','생명공학','M',1,'102');
INSERT INTO dormitory_member VALUES('강재욱','산업디자인','M',2,'102');
INSERT INTO dormitory_member VALUES('이해성','작곡','M',2,'102');
INSERT INTO dormitory_member VALUES('신남희','법학','F',4,'103');
INSERT INTO dormitory_member VALUES('민경진','항공우주','F',3,'104');
INSERT INTO dormitory_member VALUES('박채영','컴퓨터공학','F',2,'104');
INSERT INTO dormitory_member VALUES('구지원','컴퓨터공학','F',2,'104');
INSERT INTO dormitory_member VALUES('이희정','의예','F',1,'104');
INSERT INTO dormitory_member VALUES('김정태','기계','M',2,'202');
INSERT INTO dormitory_member VALUES('정명환','물리학','M',1,'202');
INSERT INTO dormitory_member VALUES('이규한','항공우주','M',1,'202');
INSERT INTO dormitory_member VALUES('양병석','사회체육','M',3,'202');
INSERT INTO dormitory_member VALUES('추은주','국어국문','F',3,'203');
INSERT INTO dormitory_member VALUES('오옥주','산업디자인','F',4,'203');
INSERT INTO dormitory_member VALUES('윤지민','전자전기','F',1,'204');
INSERT INTO dormitory_member VALUES('류중희','법학','F',1,'204');
INSERT INTO dormitory_member VALUES('최재영','생명공학','F',1,'204');
INSERT INTO dormitory_member VALUES('김영우','건축','F',2,'204');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------

	
-- 5번 문제
SELECT 
	room_no,
	name,
	major
FROM
	dormitory_member 
ORDER BY
	room_no ASC,
	name DESC;