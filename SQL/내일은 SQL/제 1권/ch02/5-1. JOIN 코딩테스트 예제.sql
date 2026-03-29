USE sql_practice


-- 1번 문제
-- order_info 테이블(왼쪽 테이블)과 book 테이블(오른쪽 테이블)에서 book_id 칼럼의 값이 같은 행 중에서
-- member_id의 값이 ccc30인 데이터를 order_date 기준으로 오름차순 하여 출력
SELECT 
	A.order_date,
	B.book_name,
	B.writer,
	B.price
FROM 
	order_info AS A
INNER JOIN 
	book AS B
	ON A.book_id = B.book_id 
WHERE 
	member_id = 'ccc30'
ORDER BY
	A.order_date ASC;
	
-- 2번 문제
-- 참고로 INNER JOIN은 여러번 사용할 수 있다.
-- SELECT
--     A.col1,
--     B.col2,
--     C.col3
-- FROM
--     table_a AS A
-- INNER JOIN
--     table_b AS B
--     ON A.id = B.id
-- INNER JOIN
--     table_c AS C
--     ON B.id = C.id;
-- 예를들어 이와 같다면 첫 번째 JOIN 문에서 왼쪽 테이블은 A, 오른쪽 테이블은 B이고
-- 두번째 JOIN 문에서 왼쪽 테이블은 이미 조인된 결과인 (A INNER JOIN B) 이고 오른쪽 테이블은 C이다.
-- 즉, 앞에서 조인된 결과를 다시 다음 테이블과 INNER JOIN하는 방식으로 이해하면 된다.
-- 다이어그램으로 생각하면, 먼저 A와 B의 교집합을 구한 뒤 그 결과를 다시 C와 교집합시키는 방식으로 이해하면 된다.

-- delivery 테이블과 order_info 테이블을 order_code 칼럼 값이 같은 조건으로 INNER JOIN하고,
-- 그 결과를 다시 book 테이블과 book_id 칼럼 값이 같은 조건으로 INNER JOIN한 뒤,
-- status 값이 '배송완료'인 행만 조회하여 finish_date 기준 내림차순으로 출력하는 쿼리
SELECT 
	A.finish_date,
	B.order_date,
	B.member_id,
	C.book_name
FROM 
	delivery AS A
INNER JOIN
	order_info AS B
	ON B.order_code = A.order_code
INNER JOIN
	book AS C	
	ON B.book_id = C.book_id
WHERE 
	A.status = '배송완료'
ORDER BY 
	A.finish_date DESC;

-- 3번 문제
-- order_info 테이블(왼쪽 테이블)과 book 테이블(오른쪽 테이블)에서 book_id 칼럼의 값이 같은 행 중에서
-- order_info 테이블에서 member_id 별로 그룹핑 한뒤, 각 member_id 별로 price의 평균을 구한다음 
-- 평균 가격이 17000 이상인 그룹만 조회하여 member_id를 기준으로 오름차순하여 출력
SELECT 
	A.member_id,
	AVG(B.price) AS avg_price
FROM 
	order_info AS A
INNER JOIN
	book AS B
	ON A.book_id = B.book_id 
GROUP BY 
	A.member_id
HAVING
	AVG(B.price) >= 17000
ORDER BY 
	A.member_id ASC;

-- 위와 똑같다.
SELECT 
	A.member_id,
	AVG(B.price) AS avg_price
FROM 
	order_info AS A,
	book AS B
WHERE
	A.book_id = B.book_id 
GROUP BY 
	A.member_id
HAVING
	AVG(B.price) >= 17000
ORDER BY 
	A.member_id ASC;
	
-- 4번 문제
-- 아직 잘 이해가 안됨
SELECT 
	A.room_no,
	A.head_count,
	A.head_count - COUNT(B.name) AS empty_count
FROM 
	dormitory_info AS A
LEFT OUTER JOIN
	dormitory_member AS B
	ON A.room_no = B.room_no 
GROUP BY 
	A.room_no, 
	A.head_count 
HAVING 
	A.head_count <> COUNT(B.name);


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE train_schedule (
    train_no         INT,
    departure_time   DATETIME,
    departures       VARCHAR(15),
    arrivals         VARCHAR(15)
);

CREATE TABLE train_reservation (
    customer_name    VARCHAR(15),
    train_no         INT,
    seat_no          VARCHAR(3)
);

INSERT INTO train_schedule VALUES (1, '2024-02-01 13:15:00', '서울', '부산');
INSERT INTO train_schedule VALUES (2, '2024-02-01 15:45:00', '여수', '서울');
INSERT INTO train_schedule VALUES (3, '2024-02-01 16:30:00', '대전', '광주');
INSERT INTO train_schedule VALUES (4, '2024-02-01 16:50:00', '부산', '대구'); -- 예약 없는 열차

INSERT INTO train_reservation VALUES ('박홍준', 1, 'A1');
INSERT INTO train_reservation VALUES ('이건호', 1, 'A2');
INSERT INTO train_reservation VALUES ('주원경', 1, 'B1');
INSERT INTO train_reservation VALUES ('양상준', 1, 'C2');
INSERT INTO train_reservation VALUES ('여은비', 1, 'D1');
INSERT INTO train_reservation VALUES ('김민재', 1, 'D2');
INSERT INTO train_reservation VALUES ('한지상', 1, 'C4');
INSERT INTO train_reservation VALUES ('고우리', 1, 'B3');
INSERT INTO train_reservation VALUES ('안현진', 1, 'F1');
INSERT INTO train_reservation VALUES ('임건호', 1, 'F4');

INSERT INTO train_reservation VALUES ('김지은', 2, 'B1');
INSERT INTO train_reservation VALUES ('반효정', 2, 'A2');
INSERT INTO train_reservation VALUES ('김덕근', 2, 'B3');
INSERT INTO train_reservation VALUES ('김진영', 2, 'B4');
INSERT INTO train_reservation VALUES ('남은영', 2, 'D1');
INSERT INTO train_reservation VALUES ('최성익', 2, 'D2');
INSERT INTO train_reservation VALUES ('유상길', 2, 'C4');

INSERT INTO train_reservation VALUES ('오혜민', 3, 'C1');
INSERT INTO train_reservation VALUES ('송진현', 3, 'C2');
INSERT INTO train_reservation VALUES ('안해경', 3, 'C3');
INSERT INTO train_reservation VALUES ('박다솔', 3, 'C4');
INSERT INTO train_reservation VALUES ('김연수', 3, 'F1');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


-- 5번 문제
-- 만약 여기서 INNER JOIN을 사용하면 train_schedule과 train_reservation의 train_no 값이 서로 매칭되는 행만 출력된다.
-- 따라서 예약 정보가 없는 열차는 출력되지 않으므로, train_schedule의 모든 행을 출력하려면 LEFT OUTER JOIN을 사용해야 한다.
SELECT 
	a.departure_time,
	a.departures,
	a.arrivals,
	b.customer_name,
	b.seat_no
FROM 
	train_schedule AS a
LEFT OUTER JOIN
	train_reservation AS b 
	ON a.train_no = b.train_no
WHERE 
	a.departure_time >= '2024-02-01 15:00:00'
	AND a.departure_time <= '2024-02-01 17:00:00'
ORDER BY 
	a.train_no ASC,
	b.seat_no ASC;
	
-- INNER JOIN을 사용한 결과
-- train_schedule과 train_reservation의 train_no가 서로 매칭되는 행만 출력된다.
-- 따라서 예약 정보가 없는 train_no 4번 열차는 제외되고, 총 12개 행만 출력된다.
SELECT 
	a.departure_time,
	a.departures,
	a.arrivals,
	b.customer_name,
	b.seat_no
FROM 
	train_schedule AS a
INNER JOIN
	train_reservation AS b 
	ON a.train_no = b.train_no
WHERE 
	a.departure_time >= '2024-02-01 15:00:00'
	AND a.departure_time <= '2024-02-01 17:00:00'
ORDER BY 
	a.train_no ASC,
	b.seat_no ASC;