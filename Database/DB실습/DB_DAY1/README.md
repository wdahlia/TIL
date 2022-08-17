# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

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

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age <= 10;
```

```sqlite
COUNT(*)
--------
300442  
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender=1;
```

```sqlite
COUNT(*)
--------
510689  
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sqlite
SELECT COUNT(*) FROM healthcare WHERE smoking=3 and is_drinking=1;
```

```sqlite
COUNT(*)
--------
150361 
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sqlite
SELECT COUNT(*) FROM healthcare WHERE va_left>=2.0 and va_right>=2.0;
```

```sqlite
COUNT(*)
--------
2614    
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sqlite
SELECT DISTINCT sido FROM healthcare;
```

```sqlite
sido
----
36  
27  
11  
31  
41  
44  
48  
30  
42  
43  
46  
28  
26  
47  
45  
29  
49  
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

### 1. gender 별로 gender, 키의 평균, 몸무게, 나이의 평균 표시

```sqlite
SELECT gender, AVG(height), AVG(weight), AVG(age) FROM healthcare group by gender;
```

```sqlite
gender  AVG(height)       AVG(weight)       AVG(age)        
------  ----------------  ----------------  ----------------
1       167.452735422145  69.7131620222875  11.7788007965709
2       154.191945408953  56.1177758112938  12.0627842006413
```

### 2. 키가 180 이상인 사람들을 구하기

```sqlite
SELECT COUNT(*) FROM healthcare WHERE height >= 180;
```

```sqlite
COUNT(*)
--------
28829   
```

