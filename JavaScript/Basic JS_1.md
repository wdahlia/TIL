📓`목차`

- [2.1 Hello, world!](#21-hello-world)
- [2.2 코드 구조](#22-코드-구조)
- [2.3 엄격 모드](#23-엄격-모드)
- [2.4 변수와 상수](#24-변수와-상수)
- [2.5 자료형](#25-자료형)
- [2.6 alert, prompt, confirm을 이용한 상호작용](#26-alert-prompt-confirm을-이용한-상호작용)
- [2.7 형 변환](#27-형-변환)
- [2.8 기본 연산자와 수학](#28-기본-연산자와-수학)
- [2.9 비교 연산자](#29-비교-연산자)

<br>


# 2.1 Hello, world!

<br>

- 모던 마크업
  - script 태그의 `type`, `language` 속성은 필수가 아님

- HTML 문서에 자바스크립트 프로그램을 삽입하고 싶다면

  - **내부 스크립트**

    - `<script>` 태그를 사용하여 안쪽에 자바스크립트 코드를 작성

  - **외부 스크립트**

    - 자바스크립트 코드의 양이 많은 경우, 파일로 소분하여 저장

    - 스크립트를 별도의 파일에 작성할 때 장점 

      > 브라우저가 스크립트를 다운받아 캐시에 저장, 성능상의 이점 존재
      >
      > 동일한 스크립트 사용할 경우, 새로 다운 받지 않고 캐시로부터 스크립트를 가져와 사용 트래픽 절약, 속도가 빨라짐

    - ```html
      # 절대 경로
      <script src="/path/to/script.js"></script>
      
      # url 전체를 속성으로 사용
      <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js"></script>
      
      # 복수의 스크립트를 삽입하고 싶다면 스크립트 태그를 여러개 사용
      ```

  - `<script>` 태그 `src` 속성과, 내부 코드 동시에 가지지 못함

    - 사용하기 위해서는 스크립트 두개로 분리하여 실행시켜야함

    - 예시코드

      ```html
      <script src="file.js"></script>
      <script>
        alert(1);
      </script>
      ```

<br>

## 과제

<img width="828" alt="2-1 과제" src="https://user-images.githubusercontent.com/108653518/205445192-cc108f2d-972e-4439-baad-0b659ca0eda8.png">

- 두 과제 모두 결과 창은 동일

### 1️⃣ alert 창 띄우기

```html
<!-- html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

  <script>
  	alert('자바스크립트!')
  </script>
  
</body>
</html>
```

<br>

### 2️⃣ 외부 스크립트를 이용해 alert 창 띄우기

```html
<!-- html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

  <script src="2-1.js"></script>
  
</body>
</html>
```

```javascript
// js
alert('자바스크립트!');
```
<br>

# 2.2 코드 구조

<br>

- `문(statement)` : 어떤 작업을 수행하는 문법 구조, 명령어를 의미

- 서로 다른 문(statement)은 세미콜론으로 구분

- **줄 바꿈**이 있다면 세미콜론을 **생략**하는 것도 **가능**

  - 암시적 세미콜론으로 해석

- 세미콜론이 정말로 필요하나 자바스크립트가 이를 추정하지 못하는 상황도 존재

  - 예를 들어, `대괄호([])` 앞에는 세미콜론이 있다고 가정하지 않음

  - 이 외에도 많은 상황들이 존재하기에, **문 사이에 세미콜론을 넣는것이 좋음 규칙으로 권장**

    ```javascript
    alert("에러가 발생합니다.")
    [1, 2].forEach(alert)
    
    >> alert("에러가 발생합니다.")[1,2].forEach(alert)
    // 이렇게 단일문으로 처리가 됨
    ```

    ```javascript
    alert("정상적으로 동작!")
    [1, 2].forEach(alert)
    
    // alert창으로 정상적으로 동작!이 실행 된 후, 1, 2 순서대로 동작
    ```

- `주석(comment)` : 자바스크립트로 인해 어떠한 일이 벌어지고 있는지를 써주는 것
  - 한 줄짜리 주석 : **//** 을 쓰고 주석을 작성
  - 여러 줄의 주석 : **/* */**
  - 중첩 주석은 지원하지 않음

<br>

# 2.3 엄격 모드

<br>

```javascript
// 전체 스크립트 엄격 모드 동작 지시자
"use strict";
```

- 전체 스크립트가 아닌, 함수의 본문 앞에 와서 해당 함수만 엄격 모드로 실행시킬 수도 있음
- `use strict`의 위에는 주석만 사용할 수 있음
- 모던 자바스크립트는 `클래스` , `모듈` 을 사용하면 `use strict`가 자동으로 적용

<br>

# 2.4 변수와 상수

<br>

## 변수

- 데이터를 저장할 때 쓰이는 **이름이 붙은 저장소**
- 변수명은 간결하고 명확하게 작성, 무엇을 담고 있는지를 설명할 수 있어야 함

### let

- `let` 으로 변수를 생성
  
  > **변수 명명 제약 사항**
  >
  > - 문자와, 숫자, `$`, `_` 만 들어갈 수 있다
  > - 첫 글자는 숫자가 될 수 없다
  > - 카멜 표기법 사용 (첫 단어를 제외한 각 단어의 첫 글자를 대문자로 작성)
  > - 예약어 목록은 변수명으로 사용할 수 없음
  >   - let, class, return, function
  
  - 변수를 선언, 값 할당을 한 줄에 작성 가능
  - 한 줄에 여러 변수 선언도 가능 (권장하는 방법은 아님)
  - `var`도 `let`과 거의 동일하게 동작 하지만 오래된 방식
  
- 어떤 값이든지 넣을 수 있고, 변경 O, 한 변수의 데이터를 다른 변수에 복사 O

```javascript
// 생성
let message;
message = 'Hello';

// 변경
message = 'World';

// 복사
let Hello = 'Hello world!';
let message;
message = Hello; // 선언된 변수인 message에 Hello의 값을 넣어줌
// 즉, message는 'Hello world!'가 출력됨
```

- 변수는 두번 선언하면 X - 에러 발생
  - 선언한 변수를 참조할 때, let 없이 변수명만 사용해 참조해야함
  - 즉, message = "That"; 이런식으로 수정


```javascript
let message = "This";

let message = "That";
// SyntaxError : 'message' has already been declared
```

<br>

### const

- 변화하지 않는 변수 선언 시, `const` 사용

- 상수는 재할당 불가능, 상수를 변경하려 하면 에러가 발생

  ```javascript
  const MyBirthday = '10.31.1995';
  myBirthday = '01.01.2022';
  // error, cant' reassing the constant!
  ```

- **대문자 상수**는 `하드 코딩한` 값의 별칭을 만들 때 사용

  - 대문자와 밑줄로 구성된 이름으로 명명

  - 기억하기에 쉽고, 오타를 낼 확률이 줄어듦, 코드 가독성 증가

    ```javascript
    const pageLoadTime = /* 웹페이즈를 로드하는데 걸린 시간 */;
    
    /* 페이지가 로드 되고 나서는 최초 할당 이후 변경되지 않기에 상수이나,
    로드되기 전에는 정해지지 않기 때문에 일반적인 방식으로 변수명을 지음 */
    
    const COLOR_RED = "#F00";
    const COLOR_GREEN = "#0F0";
    ```

<br>

## 과제

### 1️⃣ 변수 가지고 놀기

<img src="../../../Library/Application Support/typora-user-images/스크린샷 2022-12-03 오후 7.29.52.png" alt="스크린샷 2022-12-03 오후 7.29.52" style="zoom: 33%;" />

```javascript

// 복사해야하므로 let 변수 선언
let admin;
let name;
name = "John";
admin = name;
alert(admin);

```

<br>

### 2️⃣ 올바른 이름 선택하기

```javascript
let ourPlanet = "Earth";
let activeUserName = "Dahlia";
```

<br>

### 3️⃣ 대문자 상수 올바로 사용하기

- **birthday**의 경우, 변하지 않는 상수이며 이미 정해져 있는 값이기에 대문자 상수로 바꾸기에 적합
- **age**의 생일과 다르게 변화하는 값으로 대문자 상수에 적합하지 아니함

<br>

# 2.5 자료형

<br>

### 숫자형

> 정수 및 부동소수점 숫자를 나타냄
>
> 일반적인 숫자 이외에 Infinity, -Infinity, NaN과 같은 특수 숫자 값이 포함

- `Infinity` : 무한대 
- `NaN` : 계산 중 에러가 발생했다는 것을 나타내주는 값
  - 문자열을 숫자로 나누는 경우 NaN, 추가 연산을 해도 NaN을 반환

<br>

### BigInt

- 암호 관련 작업 같이 아주 큰 숫자가 필요한 상황, 아주 높은 정밀도로 작업을 해야하는 경우 필요

- 정수 리터럴 끝에 n을 붙이면 만들 수 있음

  ```javascript
  const bigInt = 1234567890123456789012345678901234567890n;
  ```

<br>

### 문자형

- 따옴표로 묶어 표시(큰 따옴표, 작은따옴표는 차이가 없음)

- 역따옴표의 경우 변수나 표현식을 감싸고 `${..}`에 넣어주면, 변수나 표현식을 문자열 중간에 넣을 수 있음

  - 큰 따옴표, 작은 따옴표 안에는 불가능

  ```javascript
  let name = "John";
  alert (`Hello, ${name}!`)
  // Hello, John!
  ```

<br>

### 불린형

- `true` , `false` 두가지 값만 가지는 자료형
- 비교 결과 저장시에도 사용

<br>

### null값

- 자바스크립트에서는 null을 **존재하지 않는**, **비어있는**, **알수없는 값**을 나타내는 곳에만 사용

  ```javascript
  let age = null;
  // 나이를 알 수 없거나 그 값이 비어있음을 나타냄
  ```

<br>

### undefined 값

- **값이 할당되지 않은 상태**

  ```javascript
  let age;
  alert(age); // undefined 출력
  ```

- 명시적으로 undefined를 할당하는 것도 가능함 (권장하지는 않음)

<br>

### 객체와 심볼

- **객체**는 데이터 컬렉션이나 복잡한 개체를 표현할 수 있음
- **심볼**은 객체의 고유한 식별자를 만들 때 사용

<br>

### typeof 연산자

- 인수의 자료형을 반환, 자료형에 따라 처리방식을 다르게 하고 싶거나 변수의 자료형을 알아내고자 할 때 유용

  ```javascript
  typeof undefined // "undefined"
  typeof 0 // "number"
  typeof 10n // "bigint"
  typeof true // "boolean"
  typeof "foo" // "string"
  typeof Symbol("id") // "symbol"
  typeof Math // "object"  (1)
  typeof null // "object"  (2)
  typeof alert // "function"  (3)
  ```

  - Math는 수학연산을 제공하는 내장 객체로 object 출력
  - null의 경우 object로 출력되는 것은 하위 호환성을 유지하기 위한 언어자체의 오류
    - 즉, null은 object는 아님
  - 피연산자가 함수이면 function을 반환 함수형은 따로 존재치 않음, 함수는 객체에 속함
    - 이 역시도, 하위 호환성 유지를 위해 남겨진 상태

<br>

## 과제

<br>

### 1️⃣ 문자열 따옴표

```javascript
let name = "Ilya";
alert( `hello ${1}` ); // hello 1
alert( `hello ${"name"}` ); // hello name
alert( `hello ${name}` ); // hello Ilya
```

<br>

# 2.6 alert, prompt, confirm을 이용한 상호작용

<br>

### alert

- 메시지를 보여주는 모달 창을 띄워줌, 확인 버튼을 눌러야지 창이 종료 됨

  ```javascript
  alert("Hello");

<br>

### prompt

- 텍스트 메시지와, 입력 필드(input field), 확인 및 취소 버튼이 있는 모달 창을 띄워 준다

- `title`  : 사용자에게 보여줄 문자열

- `default` : 입력 필드의 초깃값(선택값)

- 사용자가 입력을 취소한 경우 null이 반환

  ```javascript
  let age = prompt('나이를 입력해주세요.', 100);
  
  alert(`당신의 나이는 ${age}살 입니다.`)
  ```

- 즉, 위의 예시에서 취소를 누르게 되면 **당신의 나이는 null살 입니다**가 뜨게 되고

- input 값에 28을 넣게되면 **당신의 나이는 28살 입니다**가 뜨게 된다

<br>

### confirm

- 매개 변수로 받은 question(질문)과 확인 취소 버튼이 있는 모달 창을 보여줌

- 사용자가 **확인**을 누르면 `true` 반환, 그 외의 경우 `false`를 반환

  ```javascript
  let isBoss = confirm("당신이 주인인가요?");
  alert(isBoss);
  ```

<br>

# 2.7 형 변환

<br>

### 문자형으로 변환

```javascript
let value = true; // 불린형으로 변수 생성
alert(typeof value); // 모달 창에 자료형 출력 - boolean

value = String(value); // 변수 value에 문자열 "true"가 저장됨
alert(typeof value); // 자료형 출력 - string
```

<br>

### 숫자형으로 변환

- 숫자형이 아닌 값에 연산을 적용할 경우

```javascript
alert("6"/"2");
// 3이 모달창에 뜨게 됨
// 문자열이 숫자형으로 자동변환 된 후 연산이 수행 됨
```

- Number(value) 함수를 사용
  - 문자 기반 폼을 통해 입력받는 경우 명시적 형변환 필수

```javascript
let str = "123";
alert(typeof str); // string
let num = Number(str); // 문자열 123이 숫자 123으로 변환
alert(typeof num); // number
```

- 숫자 이외의 글자가 들어가 있는 문자열을 숫자형으로 변환할 경우 결과는 `NaN`

![스크린샷 2022-12-03 오후 8.52.17](../../../Library/Application Support/typora-user-images/스크린샷 2022-12-03 오후 8.52.17.png)<br>

### 불린형으로 변환

- Boolean(value) 하는 경우 명시적으로 불리언으로 형 변환 수행할 수 있음

- 숫자 0, 빈 문자열, null, undefined, NaN과 같이 직관적으로 비어있다 느껴지는 값들은
  - `false`
- **주의** : 문자열 0은 true, 비어 있지 않은 문자열은 언제나 true임을 명심

<br>

# 2.8 기본 연산자와 수학

<br>

- `피연산자(인수)` : 연산자가 연산을 수행하는 대상
  - `5 * 2 ` : 왼쪽 피연산자 5, 오른쪽 피연산자 2 => 총 2개의 피연산자가 존재

### 수학

- 자바스크립트에서 지원하는 수학 연산자는 `+`, `-`, `*`, `/`, `%`, `**`

<br>

### 이항 연산자 '+'와 문자열 연결

```javascript
let s = "my" + "string"; // mystring
'1' + 2 // 12
2 + 2 + '1' // 41
6 - '2' // 4 '2'를 숫자로 바꾼 후 연산 진행
'6' / '2' // 3 두 피연산자가 숫자로 바뀌고 연산 진행
```

<br>

### 단항 연산자 +와 숫자형으로의 변환

```javascript
// 숫자에는 아무 영향 미치지 못함
let x = 1;
+x // 1 

let y = -2;
-y // -2

// 숫자형 아닌 피연산자는 숫자형으로 변화
+true // 1
+"" // 0

let apples = "2";
let oranges = "3";
// 문자열 더하고 싶다면
alert ( +apples + +oranges ); // 5
// Number(...)로도 형변환을 하여 진행할 수 있다
```

<br>

### 연산자 우선 순위

[참고 사이트](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)

- 단항 연산자는 이항 연산자보다 우선순위가 높음

<br>

### 할당 연산자

```javascript
let x = 2 * 2 + 1;
alert( x ); // 5
// 이 경우 오른쪽의 연산이 이루어지고 = 이 실행되어 x에 할당이 되는것
// 할당 연산자가 우선순위가 낮음

let a = 1;
let b = 2;
let c = 3 - (a = b + 1);
// 우선 b에 2가 들어가서 a에 3이 할당되고 그이후 c에 3 - 3 즉 0이 할당되게 된다

let a, b, c;
a = b = c = 2 + 2;
// a, b, c에 각각 4가 할당이 된다 (권장하지는 않음)
c = 2 + 2 ;
b = c;
a = c; 
// 이렇게 사용하는 것을 권장
```

<br>

### 증가/감소 연산자

- `++`, `-- ` : 1씩 증가, 1씩 감소

- 변수 앞과 뒤에 올 수 있음

  ```javascript
  let counter = 1;
  let a = ++counter;
  // 2
  
  let counter = 1;
  let a = counter++;
  // 1 counter을 증가시키는 하나 기존 값을 반환하므로 1을 출력
  ```

- 값을 증가시키고 증가시킨 값을 바로 사용하려면 전위형 증가 연산자 사용

- 증가시키지만 증가전의 기존값을 바로 사용하려면 후위형 증가 연산자 사용

<br>

### 비트 연산자

- `&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`

<br>

### 쉼표 연산자

- 표현식이 평가가 되기는 하나 마지막 표현식의 평가 결과만 반환이 된다

<br>

## 과제

<br>

### 1️⃣ 전위형과 후위형

```javascript
let a = 1, b = 1;

let c = ++a; // 2
let d = b++; // 1
```

<br>

### 2️⃣ 할당 후 결과 예측하기

```javascript
let a = 2;

let x = 1 + (a *= 2);
// a = 4
// x = 5
```

<br>

### 3️⃣ 형 변환

```javascript
"" + 1 + 0 // "1" + 0 10
"" - 1 + 0 // -1
true + false // 1
6 / "3" // 2
"2" * "3" // 6
4 + 5 + "px" // "9px"
"$" + 4 + 5 // "$45"
"4" - 2 // 2
"4px" - 2 // NaN
7 / 0 // Infinity
"  -9  " + 5 //  -9 5
"  -9  " - 5 // -14 뺄셈 연산자는 공백이 일반적인 공백으로 구성
null + 1 // 1
undefined + 1 // NaN
" \t \n" - 2 // 숫자형으로 변환 시 길이가 0인 문자열로 취급되어 -2라는 결과 나옴
```

<br>

### 4️⃣ 덧셈 고치기

```javascript
let a = prompt("덧셈할 첫 번째 숫자를 입력해주세요.", 1);
let b = prompt("덧셈할 두 번째 숫자를 입력해주세요.", 2);

alert(a + b); // 12

// 코드 수정
alert(+a + +b);
alert(Number(a) + Number(b));
```

<br>

# 2.9 비교 연산자

<br>

### 불린형 반환

```javascript
let result = 5 > 4; // 비교 결과 변수에할당 5는 4보다 크므로 true가 할당
alert( result ); // true
```

<br>

### 문자열 비교

- 자바스크립트 `사전(유니코드)` 순으로 문자열 비교

  - 단어를 비교할 경우, 첫 글자가 같다면 두번째 글자로 넘어가서 큰지 작은지를 비교

  - 대문자 A와 소문자 a에서 소문자 a가 더 큼, 소문자가 더 큰 인덱스를 가지기 때문

  - 글자 간 비교가 전부다 같게 끝나고 문자열의 길이도 같다면 두 문자열이 동일하다고 결론

  - 두 문자열의 길이가 다르면 길이가 긴 문자열이 더 크다고 결론

    ```javascript
    alert( 'Z' > 'A' ); // true
    alert( 'Glow' > 'Glee' ); // true o보다 e가 크므로 여기서 비교 종료 
    alert( 'Bee' > 'Be' ); 
    // true Be까지는 같지 문자열의 길이가 Bee로 더 길기에 왼쪽이 더 큼
    ```

<br>

### 다른 형을 가진 값 간의 비교

- 비교하려는 값의 자료형이 다르다면 이 값들을 숫자형으로 전환
  - 불린값의 경우 true는 1, false는 0으로 변환된 후 비교
- **null == undefined : null은 오직 undefined와 같다**

```javascript
let a = 0;
alert( Boolean(a) ); // false 0은 false다
let b = "0";
alert( Boolean(b) ); // true 비어있지 않은 문자열은 true이다

alert(a == b); // true 동등 비교시 숫자형으로 변환하게 되는데 이경우 a = 0 b는 문자열 0에서 숫자열 0으로 변환
// 그리하여 0 == 0의 비교가되고 이는 true이다.
```

<br>

### 일치 연산자

- `==`을 사용하게 되면 숫자형으로 변환하기에 0과 false를 구분하지 못함 = 같은 값이라고 생각해 **true를 반환**
- 엄격한 비교를 위해서는 일치연산자 `===`를 사용해야함 이 경우 자료형의 동등 여부를 비교하여 **false를 반환**하게 됨
- `null === undefined` 역시 자료형이 다르기에 **false를 반환**
- 일치 연산자를 제외한 비교 연산자의 피연산자에 undefined나 null이 오지 않도록 할 것
- undefined나 null이 될 가능성 있는 변수가 <, >, <=, >=의 피연산자가 되지 않게끔 할 것

<br>

## 과제

```javascript
// 1
5 > 4 // true
// 2
"apple" > "pineapple" // false
// 3
"2" > "12" // true
// 4
undefined == null // true
// 5
undefined === null // false
// 6
null == "\n0\n" // false
// 7
null === +"\n0\n" // false
```

<br>
