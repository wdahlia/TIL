
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
);s

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- column 출력 설정
.headers on
.mode column

-- 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력
SELECT smoking, COUNT(*) FROM healthcare WHERE smoking != '' GROUP BY smoking;
-- smoking  COUNT(smoking)
-- -------  --------------
-- 1        626138        
-- 2        189808        
-- 3        183711 

-- 음주 여부(is_drinking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.
SELECT is_drinking, COUNT(*) FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;
-- is_drinking  COUNT(*)
-- -----------  ------------------
-- 0            415119            
-- 1            584685 

-- 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.
SELECT COUNT(blood_pressure) hypertension FROM healthcare WHERE blood_pressure>=200 GROUP BY is_drinking;
-- hypertension
-- ------------
-- 6064        
-- 1770 

-- 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.
SELECT sido, COUNT(sido) FROM healthcare GROUP BY sido HAVING COUNT(sido)>=50000;
-- sido  COUNT(sido)
-- ----  -----------
-- 11    166231     
-- 26    69025      
-- 28    58345      
-- 41    247369     
-- 47    54438      
-- 48    68530   

-- 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.
SELECT height, COUNT(height) FROM healthcare GROUP BY height ORDER BY COUNT(height) DESC LIMIT 5;
-- height  COUNT(height)
-- ------  -------------
-- 160     184993       
-- 155     181306       
-- 165     179352       
-- 170     152585       
-- 150     128555

-- 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 
SELECT weight, height, COUNT(*) FROM healthcare GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;
-- weight  height  COUNT(*)
------  ------  --------
-- 55      155     45866   
-- 60      160     42454   
-- 65      165     40385   
-- 50      155     38582   
-- 55      160     38066  

-- 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.
SELECT ROUND(AVG(waist), 1) "평균 허리둘레", COUNT(*) FROM healthcare GROUP BY is_drinking;
-- 평균 허리둘레  COUNT(*)
-- -------  --------
-- 81.2     415119  
-- 83.2     584685  
-- 82.8     196 

-- 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.
SELECT gender, ROUND(AVG(va_left), 2) "평균 왼쪽 시력", ROUND(AVG(va_right), 2) "평균 오른쪽 시력" FROM healthcare GROUP BY gender;
-- gender  평균 왼쪽 시력  평균 오른쪽 시력
-- ------  --------  ---------
-- 1       0.98      0.99     
-- 2       0.88      0.88 

-- 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.
SELECT age, ROUND(AVG(height), 1) "평균 키", ROUND(AVG(weight), 1) "평균 몸무게" FROM healthcare GROUP BY age HAVING "평균 키">=160 AND "평균 몸무게">=60;
-- age  평균 키   평균 몸무게
-- ---  -----  ------
-- 9    165.7  67.2  
-- 10   164.1  65.7  
-- 11   162.1  63.9  
-- 12   160.7  62.6  

-- 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.
SELECT is_drinking, smoking, AVG(weight/(height*height*0.0001)) AVG_BMI FROM healthcare WHERE is_drinking != '' and smoking != ''GROUP BY is_drinking, smoking;
-- is_drinking  smoking  AVG_BMI         
-- -----------  -------  ----------------
-- 0            1        23.8724603942955
-- 0            2        24.6073677352564
-- 0            3        24.3193273448558
-- 1            1        23.9341328992508
-- 1            2        25.0333550564281
-- 1            3        24.6363247421328
