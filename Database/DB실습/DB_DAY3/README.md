###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT smoking, COUNT(*) FROM healthcare WHERE smoking != '' GROUP BY smoking;
```

```sql
smoking  COUNT(*)
-------  --------------
1        626138        
2        189808        
3        183711 
```

###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, COUNT(*) FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;
```

```sql
is_drinking  COUNT(*)
-----------  ------------------
0            415119            
1            584685   
```

### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(blood_pressure) hypertension FROM healthcare WHERE blood_pressure>=200 GROUP BY is_drinking;
```

```sql
hypertension
------------
6064        
1770   
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT sido, COUNT(sido) FROM healthcare GROUP BY sido HAVING COUNT(sido)>=50000;
```

```sql
sido  COUNT(sido)
----  -----------
11    166231     
26    69025      
28    58345      
41    247369     
47    54438      
48    68530   
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height, COUNT(height) FROM healthcare GROUP BY height ORDER BY COUNT(height) DESC LIMIT 5;
```

```sql
height  COUNT(height)
------  -------------
160     184993       
155     181306       
165     179352       
170     152585       
150     128555  
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT weight, height, COUNT(*) FROM healthcare GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;
```

```sql
weight  height  COUNT(*)
------  ------  --------
55      155     45866   
60      160     42454   
65      165     40385   
50      155     38582   
55      160     38066  
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT ROUND(AVG(waist), 1) "평균 허리둘레", COUNT(*) FROM healthcare GROUP BY is_drinking;
```

```sql
평균 허리둘레  COUNT(*)
-------  --------
81.2     415119  
83.2     584685  
82.8     196 
```

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT gender, ROUND(AVG(va_left), 2) "평균 왼쪽 시력", ROUND(AVG(va_right), 2) "평균 오른쪽 시력" FROM healthcare GROUP BY gender;
```

```sql
gender  평균 왼쪽 시력  평균 오른쪽 시력
------  --------  ---------
1       0.98      0.99     
2       0.88      0.88 
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT age, ROUND(AVG(height), 1) "평균 키", ROUND(AVG(weight), 1) "평균 몸무게" FROM healthcare GROUP BY age HAVING "평균 키">=160 AND "평균 몸무게">=60;
```

```sql
age  평균 키   평균 몸무게
---  -----  ------
9    165.7  67.2  
10   164.1  65.7  
11   162.1  63.9  
12   160.7  62.6  
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
ELECT is_drinking, smoking, AVG(weight/(height*height*0.0001)) AVG_BMI FROM healthcare WHERE is_drinking != '' and smoking != ''GROUP BY is_drinking, smoking;
```

```sql
is_drinking  smoking  AVG_BMI         
-----------  -------  ----------------
0            1        23.8724603942955
0            2        24.6073677352564
0            3        24.3193273448558
1            1        23.9341328992508
1            2        25.0333550564281
1            3        24.6363247421328
```

