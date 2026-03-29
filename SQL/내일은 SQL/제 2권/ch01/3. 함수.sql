USE sql_practice


-- (참고)
-- 바깥 쿼리 해석 순서 및 실행 순서는 다음과 같다.
-- FROM(JOIN + ON) -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
-- WHERE는 행을 필터링하는 역할이다.
-- 서브쿼리는 항상 맨 먼저 해석되는 것이 아니라, 포함된 절에서 함께 해석한다.
-- 예를 들어 서브쿼리가 WHERE 절에 들어 있다면, 우선 FROM 절이 해석되고 그 다음 WHERE 절에서 조건을 평가할 때 서브쿼리도 함께 처리된다고 이해하면 된다.
-- CASE WHEN 구문 또한 독립적인 절이 아니라 표현식이므로, 작성된 절(SELECT, WHERE, ORDER BY 등)의 해석 순서에서 함께 처리된다.

-- 쿼리 작성 순서는 다음과 같다.
-- SELECT - FROM - JOIN ON - WHERE - GROUP BY - HAVING - ORDER BY


-- 1. 문자 함수(String Functions)
-- (1) CONCAT(문자열1, 문자열2, 문자열3, ...) 함수
-- 1) 3개의 문자열을 모두 하나로 연결
SELECT 
	CONCAT('Hello', ' ', 'SQL') AS CancatString;
	

-- (2) SUBSTRING(문자열, 시작점, 길이) 함수
-- 1) 'Hello SQL' 문자열의 7번째 자리를 시작점으로해서 2글자만 추출
SELECT 
	SUBSTRING('Hello SQL', 7, 2) AS ExtractString;
	
-- 2) 만약 시작점 매개변수가 음수라면 시작점이 오른쪽 끝에서부터 시작한다. 
--    따라서 문자열의 오른쪽부터 7번째 자리를 시작점으로 2글자만 추출
SELECT 
	SUBSTRING('Hello SQL', -7, 2) AS ExtractString;
	

-- (3) UPPER(문자열)/LOWER(문자열) 함수
-- 1) 'Hello SQL' 문자열을 모두 대문자로 변경
SELECT 
	UPPER('Hello SQL') AS UpperString;
	
-- 2) 'Hello SQL' 문자열을 모두 소문자로 변경
SELECT 
	LOWER('Hello SQL') AS LowerString;
	
-- (4) LENGTH(문자열) 함수
-- 1) 'Hello SQL' 문자열의 길이를 출력
SELECT
	LENGTH('Hello SQL') AS LengthOfString;
	

-- (5) TRIM(문자열) 함수
-- 1) '      Hello SQL             ' 문자열의 앞뒤 공백을 제거
SELECT 
	TRIM('      Hello SQL             ') AS TrimmedString;
	

-- (6) REPLACE(문자열, 특정 문자열, 대체 문자열) 함수
-- 1) 'Hello SQL' 문자열을 'Hi SQL'로 변경하여 출력
SELECT 
	REPLACE('Hello SQL', 'Hello', 'Hi') AS UpdatedString;
	

-- (7) LPAD(str, len, padstr)/RPAD(str, len, padstr) 함수
-- str: 가공이 필요한 문자열
-- len: 결과 문자열의 총 길이
-- padstr: 채워 넣을 문자열

-- 1) 'abc' 문자열에 'x'를 왼쪽에 채워넣어 길이 6으로 출력
SELECT 
	LPAD('abc', 6, 'x');
	
-- 2) 'abc' 문자열에 'x'를 오른쪽에 채워넣어 길이 6으로 출력
SELECT 
	RPAD('abc', 6, 'x');
	

-- 2. 숫자 함수(Numeric Functions)
-- (1) ROUND(숫자) 함수
-- 1) 182.345를 반올림하여 소수점 둘째 자리까지 출력
SELECT 
	ROUND(182.345, 2) AS RoundedNumber;
	

-- (2) ABS(숫자) 함수
-- 1) -256.5의 절댓값을 출력
SELECT 
	ABS(-256.5) AS AbsoluteNumber;
	

-- (3) CEIL(숫자) 함수
-- 1) 35.75를 올림하여 출력
SELECT 	
	CEIL(35.75) AS CeilNumber;
	

-- (4) FLOOR(숫자) 함수
-- 1) 35.75를 버림하여 출력
SELECT 	
	FLOOR(35.75) AS FloorNumber;
	

-- (5) TRUNCATE(숫자, 자릿수) 함수
-- 1) 182.345를 버림하여 소수점 둘째 자리까지 출력
SELECT 
	TRUNCATE(182.345, 2) AS TruncatedNumber;
	
-- 2) 만약 이처럼 자릿수 매개변수가 음수라면 버림하는 부분이 소수점 아랫자리가 아니라 정수 부분이다.
SELECT 
	TRUNCATE(1823.45, -2) AS TruncatedNumber;
	

-- 3. 날짜 함수(Date Functions)
-- NOW() vs SYSDATE()
-- 두 함수는 모두 현재의 날짜와 시간을 출력하는 함수지만,
-- NOW() 함수는 쿼리 수행이 시작되는 시점을 출력하고
-- SYSDATE() 함수는 실제로 함수가 실행되는 시점을 출력한다.

-- (1) NOW() 함수
-- 1) 현재의 날짜와 시간을 출력
SELECT  
	NOW() AS Now;
	

-- (2) SYSDATE() 함수
-- 1) 현재의 날짜와 시간을 출력
SELECT 
	SYSDATE() AS SysDate;
	

-- (3) CURRENT_DATE() 함수
-- 1) 현재의 날짜를 출력
SELECT 
	CURRENT_DATE() AS CurrentDate;


-- (4) CURRENT_TIME() 함수
-- 1) 현재의 시간을 출력
SELECT 
	CURRENT_TIME() AS CurrentTime;


-- (5) DATE_FORMAT(날짜, 항식) 함수
-- 1) NOW() 함수의 결과를 2026/03/16 형태로 출력
SELECT 
	DATE_FORMAT(NOW(), '%Y/%m/%d') AS FormattedDate;


-- (6) DATE_ADD(날짜, INTERVAL n 단위) 함수
-- 1) NOW()의 10일 뒤 날짜를 출력
SELECT 
	DATE_ADD(NOW(), INTERVAL 10 DAY) AS AddedDate;

-- 2) NOW()의 10달 뒤 날짜를 출력
SELECT 
	DATE_ADD(NOW(), INTERVAL 10 MONTH) AS AddedDate;


-- (7) DATE_SUB(날짜, INTERVAL n 단위) 함수
-- 1) NOW()의 10일 전 날짜를 출력 
SELECT 
	DATE_SUB(NOW(), INTERVAL 10 DAY) AS SubstractedDate;
	
-- 2) NOW()의 10년 전 날짜를 출력 
SELECT 
	DATE_SUB(NOW(), INTERVAL 10 YEAR) AS SubstractedDate;
	

-- (8) DATEDIFF(날짜1, 날짜2) 함수
-- 1) NOW()에서 '2026-01-01'를 빼서 출력
-- 만약 날짜1이 날짜2보다 더 작을 경우에는 음수가 출력된다.
SELECT 
	DATEDIFF(NOW(), '2026-01-01') AS DifferenceDay;
	

-- (9) YEAR(날짜)/MONTH(날짜)/DAY(날짜) 함수
-- 1) 현재 날짜의 년, 월, 일 출력
SELECT 
	YEAR(NOW()) AS Year,
	MONTH(NOW()) AS Month,
	DAY(NOW()) AS Day;
	

-- (10) HOUR(시간)/MINUTE(시간)/SECOND(시간) 함수
-- 1) 현재 날짜의 시간, 분, 초 출력
SELECT 
	HOUR(NOW()) AS Hour,
	MINUTE(NOW()) AS Minute,
	SECOND(NOW()) AS Second;
	

-- 4.변환 함수(Conversion Functions)
-- (1) CAST(데이터 AS 변환할 데이터 타입) 함수
-- 1) 문자열 '2026-03-16'을 DATE 형으로 변환
SELECT 
	CAST('2026-03-16' AS DATE) AS ConvertedDate;
	

-- (2) CONVERT(데이터, 변환할 데이터 타입)
-- 1) 문자열 '2026-03-16'을 DATE 형으로 변환
SELECT 
	CONVERT('2026-03-16', DATE) AS ConvertedDate;
	

-- 5. NULL 관련 함수(Null Functions)
-- (1) IFNULL(데이터, 대체 값) 함수
-- 1) 만약 데이터가 NULL이라면 대체 값을 출력하고 NULL이 아니라면 데이터를 그대로 출력
SELECT 
	IFNULL(NULL, 'Hello SQL') AS NullData;
	

-- (2) ISNULL(데이터) 함수
-- 1) 만약 데이터가 NULL이면 1을 출력하고 아니면 0을 출력
SELECT 
	ISNULL(NULL) AS NullData,
	ISNULL('SQL') AS NonNullData;
	

-- (3) COALESCE(데이터, 대체 값1, 대체 값2, ...) 함수
-- 1) 만약 데이터가 NULL이면 대체 값1을 출력하고, 대체 값1도 NULL이면 대체 값2를 출력하고, .... 의 반복
SELECT 
	COALESCE(NULL, NULL, 'Hello', NULL, 'SQL') AS NullData;
	

-- (4) NULLIF(데이터1, 데이터2) 함수
-- 1) 데이터1과 데이터2가 동일한 값이면 NULL을 출력하고 그렇지 않으면 데이터1을 출력
SELECT
	NULLIF('SQL', 'SQL') AS NullData;
	

-- 5. 집계 함수(책 p.92)
-- (1) COUNT 함수
-- COUNT 함수는 주어진 조건을 만족하는 행의 수를 계산할 때 사용된다.
-- COUNT 함수의 매개변수는 특정 칼럼이 될 수도 있고, *이나 1과 같은 상수 값이 될 수도 있다.

-- COUNT(*): 전체 행의 수를 반환, NULL 값도 포함
-- COUNT(1): 전체 행의 수를 반환, NULL 값도 포함
-- COUNT(칼럼명): NULL 값을 제외한 특정 칼럼 값의 수를 반환
-- COUNT(DISTINCT 칼럼명): NULL값과 중복 값을 제외한 특정 칼럼 값의 수를 반환


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE customer_info (
    cust_id    VARCHAR(20),
    birthdate    VARCHAR(8),
    gender    VARCHAR(1),
    type    VARCHAR(10)
);

INSERT INTO customer_info VALUES ('aaa111', '19770101', 'M', 'Naver');
INSERT INTO customer_info VALUES ('bbb222', '19820303', 'F', 'Kakao');
INSERT INTO customer_info VALUES ('ccc333', '19930201', 'F', 'Facebook');
INSERT INTO customer_info VALUES ('ddd444', '19970501', NULL, 'Naver');
INSERT INTO customer_info VALUES ('eee555', '19790505', 'M', 'Naver');
INSERT INTO customer_info VALUES ('fff666', '19870601', 'F', 'Kakao');
INSERT INTO customer_info VALUES ('ggg777', '19950210', 'M', 'Naver');
INSERT INTO customer_info VALUES ('hhh888', '19990701', 'M', 'Naver');
INSERT INTO customer_info VALUES ('iii999', '20001201', NULL, 'Kakao');
INSERT INTO customer_info VALUES ('jjj000', '19920801', 'M', 'Facebook');

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


SELECT * FROM customer_info;

-- 1) customer_info 테이블에서 type이 Naver인 행을 먼저 필터링한 뒤, 그 결과에서 모든 행의 개수와 NULL을 제외한 type 칼럼 값의 개수를 출력하는 쿼리
SELECT 
	COUNT(*) AS all_cnt,
	COUNT(type) AS type_cnt
FROM
	customer_info 
WHERE 	
	type = 'Naver';

-- 2) customer_info 테이블에서 type이 Naver인 행을 먼저 필터링한 뒤, 그 결과에서 NULL을 제외한 gender 칼럼 값의 개수를 출력
SELECT 
	COUNT(gender) AS gender_cnt
FROM
	customer_info 
WHERE 	
	type = 'Naver';
	
-- 3) customer_info 테이블의 데이터를 type 별로 그룹핑 한 뒤, 각 그룹(type)별로 행의 개수를 출력하는 쿼리
SELECT 
	type, 
	COUNT(*) AS customer_cnt 
FROM
 	customer_info 
GROUP BY 
	type;
	

-- (2) SUM 함수
-- SUM 함수는 특정 칼럼의 합을 계산할 때 사용되며 만약 해당 칼럼 데이터 중 NULL이 존재하면 NULL 값은 무시된다.


-- ----------------------------------------------- 데이터 삽입 -------------------------------------------------------
CREATE TABLE exam_score (
    student_name    VARCHAR(10),
    subject    VARCHAR(10),
    score    INT
);

INSERT INTO exam_score VALUES ('공기준', '국어', 97);
INSERT INTO exam_score VALUES ('공기준', '영어', 89);
INSERT INTO exam_score VALUES ('공기준', '수학', 95);
INSERT INTO exam_score VALUES ('진지원', '국어', 90);
INSERT INTO exam_score VALUES ('진지원', '영어', NULL);
INSERT INTO exam_score VALUES ('진지원', '수학', 92);
INSERT INTO exam_score VALUES ('정영주', '국어', 80);
INSERT INTO exam_score VALUES ('정영주', '영어', 95);
INSERT INTO exam_score VALUES ('정영주', '수학', 100);

COMMIT;
-- -------------------------------------------------------------------------------------------------------------


SELECT * FROM exam_score;

-- 1) exam_score 테이블에서 이름이 공기준인 행을 먼저 필터링한 뒤, 그 결과에서 NULL을 제외한 score 값의 합을 출력
SELECT 
	SUM(score) AS sum_score 
FROM 
	exam_score 
WHERE 
	student_name = '공기준';
	
-- 2) exam_score 테이블의 데이터를 student_name 별로 그룹핑 한 뒤, 각 그룹(student_name)별로 score의 합을 출력하는 쿼리
SELECT
	student_name,
	SUM(score) AS sum_score
FROM 
	exam_score 
GROUP BY
	student_name;
	

-- (3) AVG 함수
-- AVG 함수는 특정 칼럼의 평균값을 계산하는데 사용되며 만약 해당 칼럼 데이터 중 NULL이 존재하는 경우 평균값 계산 대상에서 제외된다.

SELECT * FROM exam_score;

-- 1) exam_score 테이블에서 과목이 수학인 행을 먼저 필터링한 뒤, 그 결과에서 NULL을 제외한 score 값의 평균을 출력
SELECT 
	AVG(score) AS avg_score 
FROM
	exam_score 
WHERE 
	subject = '수학';
	
-- 2) exam_score 테이블에서 과목이 수학인 행을 먼저 필터링한 뒤, 그 결과에서 NULL을 제외한 score 값의 평균을 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지 출력
SELECT 
	ROUND(AVG(score), 2) AS avg_score 
FROM
	exam_score 
WHERE 
	subject = '수학';
	
-- 3) exam_score 테이블의 데이터를 student_name 별로 그룹핑 한 뒤, 각 그룹(student_name)별로 score의 평균을 출력하는 쿼리
SELECT 	
	student_name,
	AVG(score) AS avg_score
FROM
	exam_score 
GROUP BY 
	student_name;
	
-- 4) exam_score 테이블의 데이터를 student_name 별로 그룹핑 한 뒤, 각 그룹(student_name)별로 score의 평균을 출력하는 쿼리
-- 단, 데이터가 NULL일 경우 해당 score는 0으로 계산
SELECT 	
	student_name,
	AVG(IFNULL(score, 0)) AS avg_score
FROM
	exam_score 
GROUP BY 
	student_name;
	

-- (4) MIN/MAX 함수
-- MIN/MAX 함수는 특정 칼럼의 최솟값/최댓값을 계산하는 데 사용되며 만약 해당 칼럼 데이터 중 NULL이 존재하는 경우 NULL은 무시된다.

SELECT * FROM exam_score;

-- 1) exam_score 테이블에서 과목이 국어인 행을 필터링 한 뒤, score의 최소값과 최대값 출력
SELECT 
	MIN(score) AS min_score,
	MAX(score) AS max_score
FROM
	exam_score 
WHERE 
	subject = '국어';
	
-- 2) exam_score 테이블의 데이터를 subject로 그룹핑 한 뒤, 각 그룹(subject)별로 score의 최소값과 최대값을 출력
SELECT 
	subject,
	MIN(score) AS min_score,
	MAX(score) AS max_score 
FROM
	exam_score 
GROUP BY 
	subject;	