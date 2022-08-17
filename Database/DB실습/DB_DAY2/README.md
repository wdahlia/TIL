# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
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

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```sql
COUNT(*)
--------
1000000 
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT max(age), min(age) FROM healthcare;
```

```sql
max(age)  min(age)
--------  --------
18        9     
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT max(height), min(height), max(weight), min(weight)FROM healthcare;
```

```sql
max(height)  min(height)  max(weight)  min(weight)
-----------  -----------  -----------  -----------
195          130          135          30 
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(height) FROM healthcare WHERE height>=160 and height<=170;
```

```sql
COUNT(height)
-------------
516930   
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
SELECT waist FROM healthcare WHERE is_drinking=1 and not waist='' ORDER BY WAIST DESC LIMIT 5;
```

```sql
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(is_drinking) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking=1;
```

```sql
COUNT(is_drinking)
------------------
36697    
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(blood_pressure) FROM healthcare WHERE blood_pressure<120;
```

```sql
COUNT(blood_pressure)
---------------------
360808 
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure>=140;
```

```sql
AVG(waist)      
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender=1;
```

```sql
AVG(height)       AVG(weight)     
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```sql
id      height  weight
------  ------  ------
836005  195     110  
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE weight/(height*height*0.0001)>=30;
```

```sql
COUNT(*)
--------
53121   
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, ROUND(weight/(height*height*0.0001)) AS BMI FROM healthcare WHERE smoking=3 ORDER BY BMI DESC LIMIT 5;
```

```sql
id      BMI 
------  ----
231431  51.0
934714  50.0
722707  49.0
947281  48.0
948801  48.0
```

### 13. 허리둘레가 70보다 큰 사람의 id, age, weight, BMI를 5번째 부터 10개 출력

```sql
SELECT id, age, weight, ROUND(weight/(height*height*0.0001)) AS BMI FROM healthcare WHERE waist>70 LIMIT 10 OFFSET 4;
```

```sql
id  age  weight  BMI 
--  ---  ------  ----
6   9    85      25.0
7   9    80      29.0
8   13   65      25.0
9   17   50      22.0
10  14   45      20.0
11  16   55      23.0
13  14   80      26.0
14  10   75      29.0
15  11   50      24.0
16  10   75      28.0
```

### 14. BMI가 25이상인 사람의 age, blood_pressure, smoking, is_drinking를 age, blood_pressure 내림차순 순으로 5개 출력

```sql
SELECT age, blood_pressure, smoking, is_drinking FROM healthcare WHERE weight/(height*height*0.0001)>=25 and not blood_pressure='' ORDER BY age DESC, blood_pressure DESC LIMIT 5;
```

```sql
age  blood_pressure  smoking  is_drinking
---  --------------  -------  -----------
18   208             1        0          
18   203             1        0          
18   198             1        1          
18   198             2        0          
18   197             2        1  
```

### 15. 왼쪽 눈이 2.0 이고 오른쪽 눈이 0.5이하이거나 오른쪽 눈이 2.0이고 왼쪽눈이 0.5이하인 사람을 COUNT 하라 column이름은 wear_glasses

```sql
SELECT COUNT((va_left-va_right)) AS wear_glasses FROM healthcare WHERE (va_left=2.0 and va_right<=0.5) or (va_left<=0.5 and va_right=2.0);
```

```sql
wear_glasses
------------
89       
```

<br>