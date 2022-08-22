### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT * FROM playlist_track AS A ORDER BY PlaylistId DESC LIMIT 5;
```

```sql
PlaylistId  TrackId
----------  -------
18          597    
17          3290   
17          2096   
17          2095   
17          2094  
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요

| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM tracks AS B ORDER BY TrackId LIMIT 5;
```

<img width="1320" alt="2번문제" src="https://user-images.githubusercontent.com/108653518/185889454-042e1185-bce1-478b-85e6-2a88ce847976.png">

### 3. 각 playlist_track 해당하는 tracks 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
SELECT A.PlaylistId, B.Name FROM playlist_track AS A JOIN tracks AS B ON A.TrackId = B.TrackId ORDER BY A.PlaylistId DESC LIMIT 10;
```

```SQL
PlaylistId  Name                   
----------  -----------------------
18          Now's The Time         
17          The Zoo                
17          Flying High Again      
17          Crazy Train            
17          I Don't Know           
17          Looks That Kill        
17          Live To Win            
17          Ace Of Spades          
17          Creeping Death         
17          For Whom The Bell Tolls
```

### 4. `PlaylistId`가 `10`인 tracks 데이터를 함께 출력하세요. 

| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.PlaylistId, B.Name FROM playlist_track AS A JOIN tracks AS B ON A.TrackId = B.TrackId WHERE A.PlaylistId = 10 ORDER BY B.Name DESC LIMIT 5;
```

```SQL
PlaylistId  Name                    
----------  ------------------------
10          Women's Appreciation    
10          White Rabbit            
10          Whatever the Case May Be
10          What Kate Did           
10          War of the Gods, Pt. 2  
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.

```sql
ELECT COUNT(*) FROM tracks JOIN artists ON tracks.Composer = artists.Name;
```

```SQL
COUNT(*)
--------
402     
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.

```sql
SELECT COUNT(*) FROM tracks LEFT JOIN artists ON tracks.Composer = artists.Name;
```

```SQL
COUNT(*)
--------
3503  
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.

```plain
INNER JOIN은 tracks 테이블과 artists 테이블의 교집합 즉 겹치는 부분만 출력이 되기 때문이고
LEFT JOIN은 교집합 뿐만 아니라 tracks 테이블 안의 모든 Composer 행과 artists 테이블의 Name과 join하는 것
NULL값이면 NULL 출력
```

### 8. invoice_items 테이블의 데이터를 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT InvoiceLineId, InvoiceId FROM invoice_items ORDER BY InvoiceId LIMIT 5;
```

```SQL
InvoiceLineId  InvoiceId
-------------  ---------
1              1        
2              1        
3              2        
4              2        
5              2       
```

### 9. invoices 테이블의 데이터를 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT InvoiceId, CustomerId FROM invoices ORDER BY InvoiceId LIMIT 5;
```

```SQL
InvoiceId  CustomerId
---------  ----------
1          2         
2          4         
3          8         
4          14        
5          23  
```

### 10. 각 invoice_items에 해당하는 invoices 데이터를 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```SQL
SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items AS A JOIN invoices AS B ON A.InvoiceId = B.InvoiceId ORDER BY A.InvoiceId DESC LIMIT 5;	
```

```SQL
InvoiceLineId  InvoiceId
-------------  ---------
2240           412      
2239           411      
2238           411      
2237           411      
2236           411 
```

### 11. 각 invoices에 해당하는 customers 데이터를 함께 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.InvoiceId, B.CustomerId FROM invoices AS A JOIN customers AS B ON A.CustomerId = B.CustomerId ORDER BY A.InvoiceId DESC LIMIT 5;
```

```SQL
InvoiceId  CustomerId
---------  ----------
412        58        
411        44        
410        35        
409        29        
408        25
```

### 12. 각 invoice_items(상품)을 포함하는 invoices(송장)와 해당 invoice를 받을 customers(고객) 데이터를 모두 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.InvoiceLineId, B.InvoiceId, C.CustomerId FROM invoice_items AS A JOIN invoices AS B ON A.InvoiceId = B.InvoiceId JOIN customers AS C ON B.CustomerId = C.CustomerId ORDER BY A.InvoiceId DESC LIMIT 5;
```

```sql
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58        
2239           411        44        
2238           411        44        
2237           411        44        
2236           411        44   
```

### 13. 각 customers가 주문한 invoices_item의 개수를 출력하세요.

| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT C.CustomerId, COUNT(*) FROM invoice_items AS A JOIN invoices AS B ON A.InvoiceId = B.InvoiceId JOIN customers AS C ON B.CustomerId = C.CustomerId GROUP BY C.CustomerId ORDER BY C.CustomerId LIMIT 5;
```

```sql
CustomerId  COUNT(*)
----------  --------
1           38      
2           38      
3           38      
4           38      
5           38  
```

<img width="430" alt="13번문제" src="https://user-images.githubusercontent.com/108653518/185889466-acb66721-f329-4b66-8757-6cdb50081213.png">

<br>

