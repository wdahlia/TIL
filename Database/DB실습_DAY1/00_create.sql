-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare


-- column 출력 설정
.headers on
.mode column

-- 스키마 조회
.schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- 추가되어 있는 모든 데이터의 수 출력
SELECT COUNT(*) FROM healthcare;
-- COUNT(*)
-- --------
-- 1000000 

-- 나이 그룹이 10미만인 사람의 수를 출력
SELECT COUNT(*) FROM healthcare WHERE age <= 10;
-- COUNT(*)
-- --------
-- 300442

-- 성별이 1인 사람의 수를 출력
SELECT COUNT(*) FROM healthcare WHERE gender=1;
-- COUNT(*)
-- --------
-- 510689

-- 흡연 수치가 3이면서 음주가 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE smoking=3 and is_drinking=1;
-- COUNT(*)
-- --------
-- 150361 

-- 양쪽 시력이 모두 2.0이상인 사람의 수를 출력
SELECT COUNT(*) FROM healthcare WHERE va_left>=2.0 and va_right>=2.0;
-- COUNT(*)
-- --------
-- 2614

-- 시도를 모두 중복 없이 출력
SELECT DISTINCT sido FROM healthcare;
-- sido
-- ----
-- 36  
-- 27  
-- 11
-- 31 
-- 41  
-- 44  
-- 48  
-- 30  
-- 42  
-- 43  
-- 46  
-- 28  
-- 26  
-- 47  
-- 45  
-- 29  
-- 49

-- 추가 출력
-- gender별로 gender, 키의 평균, 몸무게 평균, 나이의 평균 표시
SELECT gender, AVG(height), AVG(weight), AVG(age) FROM healthcare group by gender;
-- gender  AVG(height)       AVG(weight)       AVG(age)        
-- ------  ----------------  ----------------  ----------------
-- 1       167.452735422145  69.7131620222875  11.7788007965709
-- 2       154.191945408953  56.1177758112938  12.0627842006413

-- 키가 180 이상인 사람들 구하기
SELECT COUNT(*) FROM healthcare WHERE height >= 180;
-- COUNT(*)
-- --------
-- 28829   

-- 키가 150 이하인 사람들 구하기
SELECT COUNT(*) FROM healthcare WHERE height <= 150;
-- COUNT(*)
-- --------
-- 193404