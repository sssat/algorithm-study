USE sql_practice

-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE donut_info (
    name    VARCHAR(30),
    price    int,
    description    VARCHAR(100),
    nutrition    VARCHAR(20),
    allergy    VARCHAR(20),
    reg_date    VARCHAR(8)
    
);

INSERT INTO donut_info 
VALUES('커피도넛',2500,'커피 우유를 재해석한 부드러운 우유 도넛','244kcal','밀,대두,계란,우유','20230404');

INSERT INTO donut_info 
VALUES('먼치킨',500,'부드러운 크림을 넣은 한입 크기 도넛','40kcal','밀,대두','20230201');

INSERT INTO donut_info 
VALUES('카페모카롤',1800,'향긋한 모카의 맛과 향을 느낄 수 있는 제품','329kcal','밀,대두,우유','20220112');

INSERT INTO donut_info 
VALUES('스트로베리 필드',1700,'예쁜 딸기가 상큼, 새하얀 슈가 파우더가 입안에서 스르륵','223kcal','밀,대두','20220522');

INSERT INTO donut_info 
VALUES('허니후리터',1800,'도너츠 반죽을 손가락으로 꾹꾹, 틈새 사이로 진한 벌꿀 시럽','322kcal',NULL,'20230211');

INSERT INTO donut_info 
VALUES('보스톤 크림',1500,'부드러운 크림과 달콤한 초콜릿이 조화를 이룬 제품','226kcal','밀,대두,우유','20230715');

INSERT INTO donut_info 
VALUES('글레이즈드',1500,'더욱 촉촉하고 부드러워진 달콤한 정통 도넛','199kcal','밀,대두','20221224');

INSERT INTO donut_info 
VALUES('올리브 츄이스티',1700,'향긋한 올리브유가 들어간 쫄깃한 도넛','216kcal','밀,대두,계란,우유','20220829');

INSERT INTO donut_info 
VALUES('카카오 후로스티드',1700,'카카오의 진한 맛과 부드러운 도넛, 일곱 빛깔 무지개 컬러','198kcal','밀,대두,우유','20220602');

INSERT INTO donut_info 
VALUES('스위트 듀얼하트',2500,NULL,'297kcal','밀,대두,우유','20231114');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------

SELECT * FROM donut_info;

-- 1번 문제
SELECT 
	name, 
	price
FROM
	donut_info
WHERE 
	description IS NULL 
	OR allergy IS NULL;
	
-- 2번 문제
SELECT 
	name,
	price,
	nutrition
FROM 
	donut_info
WHERE
	price >= 1500
	AND price <= 2000;

-- 위와 똑같다.
SELECT 
	name,
	price,
	nutrition
FROM 
	donut_info
WHERE
	price BETWEEN 1500 AND 2000;
	
-- 3번 문제
SELECT 
	*
FROM 
	donut_info
WHERE
	name = '커피도넛'
	OR name = '카페모카롤'
	OR name = '글레이즈드';
	
-- 위와 똑같다.
SELECT 
	*
FROM 
	donut_info
WHERE
	name IN ('커피도넛', '카페모카롤', '글레이즈드');
	
-- 4번 문제
SELECT 
	name,
	nutrition,
	allergy
FROM 
	donut_info
WHERE
	allergy LIKE '%우유%'


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE book (
    book_id    VARCHAR(6),
    book_name  VARCHAR(30),
    writer     VARCHAR(15),
    price      INT
);

CREATE TABLE order_info (
    order_code       VARCHAR(8),
    member_id        VARCHAR(20),
    book_id       VARCHAR(6),
    order_date    DATE
);

CREATE TABLE delivery (
	delivery_code    VARCHAR(4),
	order_code       VARCHAR(8),
	status           VARCHAR(10),
	finish_date      DATE
);



INSERT INTO book VALUES('230907','마흔에 읽는 쇼펜하우어','강용수',17000);
INSERT INTO book VALUES('231214','흔한남매','백난도',14500);
INSERT INTO book VALUES('240105','내가 한 말을 내가 오해하지 않기로 함','문상훈',19800);
INSERT INTO book VALUES('230302','세이노의 가르침','세이노',7200);
INSERT INTO book VALUES('230830','퓨처 셀프','벤저민 하디',19800);
INSERT INTO book VALUES('230428','도둑맞은 집중력','요한 하리',18800);
INSERT INTO book VALUES('231030','남에게 보여주려고 인생을 낭비하지 마라','쇼펜하우어',17500);
INSERT INTO book VALUES('230925','생각이 너무 많은 어른들을 위한 심리학','김혜남',17800);
INSERT INTO book VALUES('230922','요즘 어른을 위한 최소한의 세계사','임소미',18800);
INSERT INTO book VALUES('231127','이처럼 사소한 것들','클레어 키건',13800);

INSERT INTO order_info VALUES('24010901','aaa10','230907','2024-01-09');
INSERT INTO order_info VALUES('24010902','bbb20','230302','2024-01-09');
INSERT INTO order_info VALUES('24010903','ccc30','231127','2024-01-09');
INSERT INTO order_info VALUES('24010904','ddd40','230922','2024-01-09');
INSERT INTO order_info VALUES('24011001','aaa10','231030','2024-01-10');
INSERT INTO order_info VALUES('24011002','ccc30','230907','2024-01-10');
INSERT INTO order_info VALUES('24011003','eee50','231127','2024-01-10');
INSERT INTO order_info VALUES('24011004','fff60','230428','2024-01-10');
INSERT INTO order_info VALUES('24011005','bbb20','240105','2024-01-10');
INSERT INTO order_info VALUES('24011006','ggg70','230428','2024-01-10');
INSERT INTO order_info VALUES('24011101','aaa10','230907','2024-01-11');
INSERT INTO order_info VALUES('24011102','ccc30','230925','2024-01-11');
INSERT INTO order_info VALUES('24011103','eee50','231127','2024-01-11');
INSERT INTO order_info VALUES('24011104','ggg70','230922','2024-01-11');
INSERT INTO order_info VALUES('24011105','bbb20','231030','2024-01-11');
INSERT INTO order_info VALUES('24011106','ddd40','230907','2024-01-11');
INSERT INTO order_info VALUES('24011107','fff60','230830','2024-01-11');
INSERT INTO order_info VALUES('24011201','aaa10','230830','2024-01-12');
INSERT INTO order_info VALUES('24011202','bbb20','240105','2024-01-12');
INSERT INTO order_info VALUES('24011203','ccc30','230428','2024-01-12');

INSERT INTO delivery VALUES('C211','24010901','배송완료','2024-01-12');
INSERT INTO delivery VALUES('C212','24010902','배송완료','2024-01-13');
INSERT INTO delivery VALUES('C213','24010903','배송중',NULL);
INSERT INTO delivery VALUES('C214','24010904','배송완료','2024-01-12');
INSERT INTO delivery VALUES('C215','24011001','배송준비중',NULL);
INSERT INTO delivery VALUES('C216','24011002','상품준비중',NULL);
INSERT INTO delivery VALUES('C217','24011003','배송완료','2024-01-13');
INSERT INTO delivery VALUES('C218','24011004','상품준비중',NULL);
INSERT INTO delivery VALUES('C219','24011005','배송중',NULL);
INSERT INTO delivery VALUES('C220','24011006','상품준비중',NULL);
INSERT INTO delivery VALUES('C221','24011101','상품준비중',NULL);
INSERT INTO delivery VALUES('C222','24011102','결제완료',NULL);
INSERT INTO delivery VALUES('C223','24011103','배송중',NULL);
INSERT INTO delivery VALUES('C224','24011104','상품준비중',NULL);
INSERT INTO delivery VALUES('C225','24011105','상품준비중',NULL);
INSERT INTO delivery VALUES('C226','24011106','상품준비중',NULL);
INSERT INTO delivery VALUES('C227','24011107','결제완료',NULL);
INSERT INTO delivery VALUES('C228','24011201','결제완료',NULL);
INSERT INTO delivery VALUES('C229','24011202','결제완료',NULL);
INSERT INTO delivery VALUES('C230','24011203','상품준비중',NULL);

COMMIT;
-- -------------------------------------------------------------------------------------------------------------

SELECT * FROM book;

-- 5번 문제
SELECT 
	*
FROM 
	book
WHERE
	book_name LIKE '%쇼펜하우어%'
	OR writer LIKE '%쇼펜하우어';
	
-- 6번 문제
SELECT 
	book_id
FROM 
	order_info 
WHERE
	(order_date >= '2024-01-09' AND order_date <= '2024-01-10')
	AND member_id = 'aaa10';

-- 7번 문제
SELECT 
	delivery_code AS '배송 코드',
	status AS '배송상태',
	finish_date AS '배송완료 일자'
FROM 
	delivery
WHERE
	status IN ('배송중', '배송완료');