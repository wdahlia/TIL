📓`목차`
- [2.10 if와 '?'를 사용한 조건 처리](#210-if와-를-사용한-조건-처리)
- [2.11 논리 연산자](#211-논리-연산자)
- [2.12 nullish 병합 연산자 '??'](#212-nullish-병합-연산자-)
- [2.13 while문과 for 반복문](#213-while문과-for-반복문)
- [2.14 switch문](#214-switch문)
- [2.15 함수](#215-함수)
- [2.16 함수 표현식](#216-함수-표현식)
- [2.17 화살표 함수 기본](#217-화살표-함수-기본)
- [2.18 기본 문법 요약](#218-기본-문법-요약)

<br>


# 2.10 if와 '?'를 사용한 조건 처리

<br>

### if문

- 괄호 안의 조건 평가, 결과가 `true`이면 코드 블록을 실행시킴
- 조건이 `true` 일 때,  구문이 한 줄이던지 복수의 문인지에 상관 없이 중괄호로 코드 블록을 감싸준다
  - 코드의 가독성 증가

#### 불린형으로의 변환

- 형 변환 규칙에서 false가 되는 값들로는 코드 블록이 절대 실행되지 아니함
  - `0`, 빈 문자열`""`, `null`, `undefined`, `NaN`

```javascript
let cond = (year == 2015); // 비교를 통해 true/false 여부를 결정하여

// 그 결과값 true or false를 if문에 전달, true이면 코드 블록 실행, 아닐 시 false실행
if (cond) {
  ...
}
```

#### else, else if

- `else` 절은 조건이 거짓일 때 실행되는 코드 블록
- `else if`절은 조건 여러개를 처리 할 때 사용함
  - else if로만 조건을 끝낼 수 있음, else는 선택 사항

<br>

### '?'

- 여러 분기를 만들어 처리할 때는 if를 사용하는 것이 좋음

```javascript
let result = condition ? value1 : value2;
```

- condition이 true라면 value1이 그렇지 않으면 value2가 반환되어 result에 할당

```javascript
let accessAllowed = (age > 18) ? true : false;
// let accessAllowed = age > 18 ? true : false;
// let accessAllowed = age > 18;
```

- `? 연산자`는 우선순위가 낮으므로 비교연산자 >가 실행되고 난 뒤에 실행되므로, 괄호를 제거해도 무방함
  - 하지만 가독성을 위해 괄호 사용하기를 권장

```javascript
let age = prompt('나이를 입력해주세요.', 18);

let message = (age < 3) ? '아기야 안녕?' :
  (age < 18) ? '안녕!' :
  (age < 100) ? '환영합니다!' :
  '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';

/* if (age < 3) {
	message = '아기야 안녕?';
} else if (age < 18) {
	message = '안녕!';
} else if (age < 100) {
	message = '환영합니다!';
} else {
	message = '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!'
} */

alert( message );
```

- 다중 `? 연산자` 
  - 조건 첫 번째인 age < 3 이면, **아기야 안녕?**을 message에 할당
  - 아니라면, age < 18 조건을 검사해서 참이면, **안녕!**을 message에 할당
  - 그것 역시 아니라면 age < 100 조건 검사 참일 경우, **환영합니다!**를 할당
  - 그 외의 경우는 **나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!**를 message에 할당하여 alert창으로 띄움 

<br>

## 과제

### 1️⃣ if와 문자열 0

```javascript
if ("0") {
  alert( 'Hello' );
}
```

- alert은 실행 된다, "0"인 경우 비어있지 않은 문자열이므로 true를 반환 alert이 실행된다.

<br>

### 2️⃣ 자바스크립트의 공식 이름

```javascript
let answer = prompt('자바스크립트의 "공식"이름은 무엇일까요?', '');

if (answer == 'ECMAScript'){
  alert('정답입니다!');
} else {
  alert('모르셨나요? 정답은 ECMAScript입니다!');
}
```

<br>

### 3️⃣ 입력받은 숫자의 부호 표시하기

```javascript
let value = prompt('숫자를 입력해주세요', '');

if (value > 0) {
  alert('1');
} else if ( value < 0 ) {
  alert('-1');
} else {
  alert('0');
}
```

<br>

### 4️⃣ if를 ?로 교체하기

```javascript
let result;

if (a + b < 4) {
  result = '미만';
} else {
  result = '이상';
}
```

```javascript
let result = (a + b < 4) ? '미만' : '이상';
```

<br>

### 5️⃣ if..else를 ?로 교체하기

```javascript
let message;

if (login == '직원') {
  message = '안녕하세요.';
} else if (login == '임원') {
  message = '환영합니다.';
} else if (login == '') {
  message = '로그인이 필요합니다.';
} else {
  message = '';
}
```

```javascript
let message = (login == '직원') ? '안녕하세요' :
(login == '임원') ? '환영합니다' :
(login == '') ? '로그인이 필요합니다.' :
'';
```



<br>

# 2.11 논리 연산자

<br>

### || 

- **OR**
- 불린값을 조작하는데 사용
- 피연산자가 모두 false인 경우를 제외하면 연산 결과는 항상 true
- 피연산자가 불린형이 아니라면 평가를 위해 불린형으로 변환됨
- if문에서 자주 사용됨

```javascript
alert( 1 || 0 ); // 1
// 1이 true이므로 연산을 멈추고 true인 값의 원래값인 1을 반환

alert( null || 1 ); 
// null은 false, 1이 true이므로 연산을 멈추고 true인 값의 원래값인 1을 반환

alert( null || 0 || 1 );
// null은 false, 0도 false, 1이 true이므로 연산을 멈추고 true인 값의 원래값인 1을 반환

alert( undefined || null || 0 );
// undefined은 false, null 역시 false, 0역시 false이므로 모두 false이기에 마지막 false값인 0을 반환
```

- true인 값이 있다면 실제 값이 들어있는 변수를 반환

  ```javascript
  let firstName = "";
  let lastName = "";
  let nickName = "바이올렛";
  
  alert( firstName || lastName || nickName || "익명"); 
  
  // firstName, lastName 모두 비어있는 문자열로 false값이나 nickName은 비어있지 않은 문자열이기에 true
  // 원래의 값인 바이올렛이 출력되게 됨
  // 만약 nickName도 빈문자열이게 되면 유일하게 비어있지않은 문자열인 익명을 반환 
  ```

- 단락 평가

  ```javascript
  true || alert("not printed");
  false || alert("printed");
  
  // 왼쪽에서 오른쪽으로 평가를 진행, true를 만나면 나머지값은 건드리지 않음 = 단락 평가
  // 즉 첫번째는 true가 먼저 평가 진행되기에 alert이 뜨지않게되고
  // 두번째 코드는 왼쪽 false가 먼저 평가 된 후 alert이 true가 되게되므로 alert창 출력
  ```

<br>

### &&

- AND

- 모두 참일때 true, 나머지는 false

- 변환 후 값이 false이면 평가를 멈추고 변환 전 원래의 값을 반환

- 모두 true이면 마지막 피연산자가 반환

- || 보다 연산 우선순위가 높음

  ```javascript
  alert( 1 && 0 );
  // 1은 true, 0은 false이므로 0 반환
  alert( 1 && 5 );
  // 1도 true, 5도 true로 전부 true이기에 마지막 값 5 반환
  alert( null && 5 );
  // null false 이므로 null 반환
  alert( 0 && "아무거나 와도 상관없습니다." );
  // 0이 false이므로 0반환 
  ```

<br>

### !

- NOT

- 불린형 true/false로 변환

  ```javascript
  alert( !true );
  // true의 반대는 false 즉 false 반환
  alert( !0 );
  // false의 반대는 true true 반환
  
  alert( !!"non-empty string" );
  // 비어있지않은 문자열이므로 true true의 !는 false 그 false의 !가 또붙으므로 true 출력
  alert( !!null );
  // false에 ! true, true에 ! false false반환
  ```

- !을 두번 사용하면 원래 값을 불린형으로 전환

  - Boolean()을 사용할수도 있음
  - `Boolean("non-empty string");`
  - `Boolean(null)`

<br>

## 과제

### 1️⃣  다음 OR 연산의 결과는 무엇일까요?

```javascript
alert( null || 2 || undefined );
```

- null은 false 여서 통과 2는 true이므로 2에서 연산 종료후 **2 반환**

<br>

### 2️⃣ OR 연산자의 피연산자가 alert 라면?

```javascript
alert( alert(1) || 2 || alert(3) );
```

- 1이 true 값이므로 alert창이 뜨면서 1이나오게 되나 alert은 undefined를 반환하여 false가 되므로, 다음 연산자를 평가하게됨 2는 true가 되므로 alert창에 2가 뜨고 연산 종료
- **alert에 1, 2가 차례대로 출력**되는 결과

<br>

### 3️⃣ 다음 AND 연산의 결과는 무엇일까요?

```javascript
alert( 1 && null && 2 );
```

- 1은 true이므로 통과 null은 false이므로 연산이 종료되고 **null이 반환**

<br>

### 4️⃣ AND 연산자의 피연산자가 alert 라면?

```javascript
alert( alert(1) && alert(2) );
```

- alert에 1이 뜨기는 하나, alert자체는 undefined로 false이므로 연산이 종료되고 false값인 undefined를 출력
- **1과 undefined가 alert창에 출력됨**

<br>

### 5️⃣ OR AND OR 연산자로 구성된 표현식

```javascript
alert( null || 2 && 3 || 4 );
```

- `2&&3` &&연산자가 우선순위가 ||보다 높기에 연산이 먼저이루어짐 true, true이므로 마지막 값인 3

  ```javascript
  alert( null || 3 || 4);
  ```

- 이러한 식이 되고 null은 false이므로 다음값으로 넘어가게 되고 3은 true이므로 **3을 출력**

<br>

### 6️⃣ 사이 범위 확인하기

```javascript
let age;

if (age >= 14 && age <= 90) {
  alert('14세 이상 90세 이하입니다.');
}
```

<br>

### 7️⃣ 바깥 범위 확인하기

```javascript
let age;

if (age < 14 || age > 90) {
  alert('14세 이상 90세 이하가 아닙니다.');
}

if (!(age >= 14 && age <= 90)) {
  alert('14세 이상 90세 이하가 아닙니다.');
}
```

<br>

### 8️⃣ "if"에 관한 고찰

```javascript
if (-1 || 0) alert( 'first' );
if (-1 && 0) alert( 'second' );
if (null || -1 && 1) alert( 'third' );
```

- 첫 번째의 경우 -1가 true이므로 **alert 실행** first 보여짐
- 두 번째의 경우 false이므로 **alert 실행 안됨**
- 세 번째의 경우 (null || 1) 이므로 1이 true이기에 **alert이 실행**되고 third가 보여지게 됨

<br>

### 9️⃣ 로그인 구현하기

```javascript
let id = prompt('누구신가요.', '');

if (id == "Admin") {
  let password = prompt('비밀번호를 입력하세요.', '');
  if (password == "TheMaster") {
    alert('환영합니다.');
  } else if (password == "" || password == null) {
    alert('취소되었습니다.');
  } else {
    alert('인증에 실패하였습니다.');
  }
} else if (id == "" || id == null) {
  alert('취소되었습니다.');
} else {
  aler('알 수 없는 사용자입니다.');
}
```

<br>

# 2.12 nullish 병합 연산자 '??'

<br>

- 피연산자 중 그 값이 **확정되어있는** 변수를 찾을 수 있음

- null이나 undefined가 아닌 경우의 값을 찾아줌

  ```javascript
  x = (a !== null && a !== undefined) ? a : b;
  // a가 null이 아니고 undefined가 아니면 a를 x에 할당
  x = a ?? b
  // 이렇게 줄일 수 있음
  ```

  ```javascript
  let firstName = null;
  let lastName = null;
  let nickName = "바이올렛";
  
  alert(firstName ?? lastName ?? nickName ?? "익명의 사용자");
  // 값이 확정되어있는 nickName을 반환 바이올렛 반환됨
  ```

- `||` 과 `??`의 차이점

  - `||`는 첫번째 true값을 반환

  - `??`는 정의된 값을 반환 

    ```javascript
    let height = 0;
    
    alert(height || 100);
    // height이 0이 되면 false로 변환 함 그래서 그 다음 true값인 100을 반환
    alert(height ?? 100);
    // 이 경우 정의된 값을 반환하므로 0을 출력
    ```

- 연산자의 우선순위는 5로 낮은편이므로, **값을 하나 선택하게 될때는 괄호를 추가**하는 것이 좋음
- 또한, &&와 ||와 함께 사용하지 못함 - 안전성 문제
  - 제약을 피하려면 괄호를 사용

<br>

# 2.13 while문과 for 반복문

<br>

### while

- while 반복문의 조건이 true이면 반복문의 코드가 실행

  ```javascript
  while (condition) {
    // 코드
  }
  ```

- 본문이 한줄이라면 대괄호 사용하지 않아도 됨

- `do...while` : 조건이 true인지 아닌지 상관없이 **최소 한번 실행**하고 싶을 때 사용

  - 본문 먼저 실행 후, do 대괄호안이 먼저 실행되고 while의 조건 점검하여 만족되면 계속 실행

  ```javascript
  let i = 0;
  do {
    alert(i);
    i++;
  } while (i < 3); 
  ```

<br>

### for

- **for문의 구성요소**

  ```javascript
  for (begin; condition; step) {
    // body
  }
  ```

  - `begin` : 반복문에 진입 할 때, 단 한번 실행

  - `condition` : 반복문마다 해당 조건을 확인, false면 반복문 실행을 중지

  - `body` : condition true일 동안 계속 실행

  - `step` : body가 실행된 이후 실행

- for문의 구성요소는 필요에 따라 생략하는 것도 가능

- 모든 구성요소를 생략할 때는 무한 반복문이 만들어지는데, 이 경우에도 `for(;;)` 로 표시해주어야함

- 반복문을 빠져나오려면 `break`를 다음 반복으로 넘어가려면 `continue`

- 삼항 연산자 `?` 는 break나 continue가 올 수 없습니다

- **레이블을 사용** : 

  - 예를 들어, break outer는 outer라는 레이블이 붙은 반복문을 찾고, 해당 반복문을 빠져나오게 됨

    ```javascript
    outer: for (let i = 0; i < 3; i++) {
    
      for (let j = 0; j < 3; j++) {
    
        let input = prompt(`(${i},${j})의 값`, '');
    
        // 사용자가 아무것도 입력하지 않거나 Cancel 버튼을 누르면 두 반복문 을 빠져나옵니다.
        if (!input) break outer; // outer라는 위쪽의 레이블을 찾아 이중 포문을 빠져나옴
      }
    }
    alert('완료!');
    ```

<br>

## 과제

### 1️⃣ 반복문의 마지막 값

```javascript
let i = 3;

while (i) {
  alert( i-- );
}

// 1이 출력
// 0이 되면 false가 되기때문에 종료되어서 마지막으로 뜨는 값은 1이 된다
```

<br>

### 2️⃣ while 반복문의 출력값 예상하기

```javascript
let i = 0;
while (++i < 5) alert( i );

// 1부터 4가 나오게 됨
```

```javascript
let i = 0;
while (i++ < 5) alert( i );

// 1부터 5가 나오게 됨
```

<br>

### 3️⃣ for 반복문의 출력값 예상하기

```javascript
for (let i = 0; i < 5; i++) alert( i );

// 0부터 4까지 나오게 됨
```

```javascript
for (let i = 0; i < 5; ++i) alert( i );

// 0부터 4까지 나오게 됨
```

- 전위형 증가 연산자, 후위형 증가 연산자에 차이가 존재하지 않는다.

<br>

### 4️⃣ for 반복문을 이용하여 짝수 출력하기

```javascript
for (let i=2; i <= 10; i++) {
  if (i % 2 == 0) {
    alert(i);
  }
}
```

<br>

### 5️⃣ for 반복문을 while 반복문으로 바꾸기

```javascript
for (let i = 0; i < 3; i++) {
  alert( `number ${i}!` );
}

let i = 0;
while (i < 3) {
  alert(`number ${i}!`);
  i++;
}
```

<br>

### 6️⃣ 사용자가 유효한 값을 입력할 때까지 프롬프트 창 띄우기 

```javascript
let number;

do {
  number = prompt('100보다 큰 숫자를 입력하세요', '');
} while (number <= 100 && number);
```

<br>

### 7️⃣ 소수 출력하기

```javascript
let n = 10;

for (let i=2; i<=n; i++) {
  for (let j=2; j < i; j++) { 
  	if (i % j == 0) continue;
  }
  alert(i);
}
```



<br>

# 2.14 switch문

<br>

- 복수의 if문은 switch문으로 변환 가능

- 하나 이상의 `case`문으로 구성

  ```javascript
  let a = 2 + 2;
  
  switch (a) {
    case 3:
      alert( '비교하려는 값보다 작습니다.' );
      break;
    case 4:
      alert( '비교하려는 값과 일치합니다.' );
      break;
    case 5:
      alert( '비교하려는 값보다 큽니다.' );
      break;
    default:
      alert( "어떤 값인지 파악이 되지 않습니다." );
  }
  ```

  - a의 값은 4로 할당 되었음

  - 첫번째 case는 값이 3이므로 다음 case문으로 넘어감

  - 두번째 case와는 값이 일치하므로 비교하려는 값과 일치합니다라는 코드 실행이됨

  - 이 때, break문이 없다면 다음 case를 실행하게되고

  - case4, case5, default의 alert이 모두 실행

- case문을 묶는 것 가능

  - 묶는 것은 가능하나 break문을 표시하지 않으면 코드가 계속 실행될 수 있음

- 자료형이 중요

  - case문의 값의 형과 값이 같아야지만 case문이 실행됨

    ```javascript
    let arg = prompt("값을 입력해주세요.");
    switch (arg) {
      case '0':
      case '1':
        alert( '0이나 1을 입력하셨습니다.' );
        break;
    
      case '2':
        alert( '2를 입력하셨습니다.' );
        break;
    
      case 3:
        alert( '이 코드는 절대 실행되지 않습니다!' );
        break;
      default:
        alert( '알 수 없는 값을 입력하셨습니다.' );
    }
    ```

  - prompt 함수의 경우 숫자를 입력해도 문자열로 반환하기 때문에, 3을 입력해도 case 3은 실행될 수 없음

    - default문이 실행되게 됨

<br>

## 과제

### 1️⃣ switch문을 if문으로 변환

```javascript
switch (browser) {
  case 'Edge':
    alert( "Edge를 사용하고 계시네요!" );
    break;

  case 'Chrome':
  case 'Firefox':
  case 'Safari':
  case 'Opera':
    alert( '저희 서비스가 지원하는 브라우저를 사용하고 계시네요.' );
    break;

  default:
    alert( '현재 페이지가 괜찮아 보이길 바랍니다!' );
}
```

```javascript
if (browser == 'Edge') {
  alert("Edge를 사용하고 계시네요!");
} else if (browser == 'Chrome' 
           || browser == "Firefox" 
           || browser == "Safari" 
           || browser == "Opera") {
  alert("저희 서비스가 지원하는 브라우저를 사용하고 계시네요.");
} else {
  alert("현재 페이지가 괜찮아 보이길 바랍니다!");
}
```

<br>

### 2️⃣ if문을 switch문으로 변환

```javascript
let a = +prompt('a?', '');

if (a == 0) {
  alert( 0 );
}
if (a == 1) {
  alert( 1 );
}

if (a == 2 || a == 3) {
  alert( '2,3' );
}

```

```javascript
let a = +prompt('a?', '');

switch(a) {
  case 0:
    alert(0);
    break;
    
  case 1:
    alert(1);
    break;
    
  case 2:
  case 3:
    alert('2,3');
    break;
}
```

<br>

# 2.15 함수

<br>

- 함수 선언

  ```javascript
  function showMessage() {
    alert('안녕하세요!');
  }
  
  showMessage();
  ```

  - `function 키워드` + `함수 이름` + `괄호로 둘러싼 매개변수`
    - 매개변수가 여러개라면 콤마로 구분
    - 함수 이름 옆에 괄호를 붙여 호출 가능
  - 매개변수와 인수의 차이점
    - *매개변수*는 함수 선언 시 괄호 안에 있는 변수
    - *인수*는 함수를 호출 할 때, 매개변수에 전달되는 값

<br>

### 지역 변수

- 함수 안에서만 접근 가능

  ```javascript
  function showMessage() {
    let message = "안녕하세요!"; 
  
    alert( message );
  }
  
  showMessage();
  // 함수를 호출하게 되면 alert창으로 message 안녕하세요!를 출력
  
  alert( message ); 
  // ReferenceError: message is not defined
  // message는 함수 안에서 정의가 된 것이므로 외부에서는 불러올 수 없다
  ```

<br>

### 외부 변수

```javascript
let userName = 'John';

function showMessage() {
  userName = "Bob";
  // 외부변수인 userName을 Bob으로 수정
  let message = 'Hello, ' + userName;
  // message에 Hello, Bob이 할당
  alert(message);
}

alert( userName ); 
// 함수를 호출하지 않았으므로 John이 뜨게 됨

showMessage(); // Hello, Bob이라는 alert창이 뜨게됨

alert( userName ); 
// 함수에 따라 userName = "Bob"으로 변했으므로 Bob이 출력
```

```javascript
let userName = 'John';

function showMessage() {
  let userName = "Bob"; 
  let message = 'Hello, ' + userName;
  alert(message);
}

showMessage(); // Hello, Bob

alert( userName ); 
// userName이 showMessage() 안에서 다시 한 번 할당된 것 즉, 지금 현재 외부변수에만 접근 가능
// John이 출력
```

<br>

- 만약, 매개변수가 두개이고 인수는 한개밖에 호출하지 않았을 경우에는 호출하지 않은 인수는 **undefined**가 됨
- default값을 설정할 수도 있음

```javascript
function showMessage(from, text = anotherFunction()) {
}

// anotherFunction은 text값이 존재하지 않을때만 호출됨

function showMessage(text) {
  if (text == undefined) {
    text = '빈 문자열';
  }
  or
  text = text || '빈 문자열';
}

// 이런식으로 함수 선언 후에 매개변수 기본값을 설정하는 것이 적절한 경우도 존재
```

- 반환 값 즉, `return`의 경우 여러개의 return문을 사용할 수도 있으며 return만 명시하는 것도 가능(이 경우 함수 즉시 종료)

  - 여러줄의 긴 표현식을 return하려는 경우 같은 줄에 작성해야 함 개행하고 쓰면 안된다.

    - 띄워쓰고 싶은 경우 - 여는 괄호를 return 옆에 쓴 다음 개행

      ```javascript
      return (
        some + long + expression
        + or +
        whatever * f(a) + f(b)
        )
      ```

- 함수를 분리하여 작성하면, 테스트와 디버깅이 쉬워짐 또한 중복을 없애려는 용도로도 사용

<br>

## 과제

### 1️⃣ else는 정말 필요한가요?

- 변화 없이 동일하게 작동합니다.

<br>

### 2️⃣ ?나 ||를 사용하여 함수 다시 작성하기

```javascript
function checkAge(age) {
  return (age > 18) ? true : confirm('보호자의 동의를 받으셨나요?');
}
```

```javascript
function checkAge(age) {
  return (age > 18) || confirm('보호자의 동의를 받으셨나요?');
}
```

<br>

### 3️⃣  min(a, b) 함수 만들기

```javascript
function min(a, b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
} 
```

<br>

### 4️⃣ pow(x, n) 함수 만들기

```javascript

let x = prompt("x", "");
let n = prompt("n", "");

if (n < 1) {
  alert('자연수를 입력해주세요');
} else {
  alert(pow(x, n));
}

function pow(x, n) {
  let result = x;
  
  for (let i=1; i < n; i++) {
    result *= x;
  }
  
  return result;
}
```

<br>

# 2.16 함수 표현식

<br>

```javascript
function sayHi() { 
	alert('Hi');
}

// 함수 선언식

let sayHi = function() {
  alert('Hi');
}

// 함수 표현식
```

- 함수를 변수에 할당하는 방식
- 함수를 복사해서 실행 가능, 원래 함수도 실행 가능 (무조건 변수옆에 괄호를 붙여주어야함)
- 함수 표현식의 경우는 변수할당이기에 대괄호 뒤에 세미콜론을 붙여주는 것이 좋다

<br>

### 함수 표현식 vs 함수 선언문

- 함수 선언문은 **정의 되기 전에도 호출이 가능**

- 함수 표현식은 **실행이 되고 나서 호출이 가능**

  ```javascript
  sayHi("John"); // Hello, John
  
  function sayHi(name) {
    alert(`Hello, ${name}`);
  }
  
  // 함수선언문의 경우 함수가 정의 되기 전임에도 오류를 반환하는 것이 아닌 호출이 된다
  
  sayHi("John"); // error!
  
  let sayHi = function(name) { 
    alert( `Hello, ${name}` );
  };
  
  // 함수 표현식의 경우 error 반환
  ```

- 하지만 함수 선언문은  if 문 밖에서 호출이 불가능, 함수 표현식은 let welcome; 이런식으로 바깥에 정의를 하기때문에 if 문 밖에서도 동작
- 함수 선언식이 조금 더 효과적이기는 하나, 함수 표현식을 사용해야하는 상황 역시 존재

<br>

# 2.17 화살표 함수 기본

<br>

```javascript
let func = (arg1, arg2, ...argN) => expression
// arg1, arg2, ..argN의 인자를 받는 함수 func이 만들어지고 이 함수는 표현식 expression을 평가하고 평가 결과 반환

let func = function(arg1, arg2, ...argN) {
  return expression;
};
```

- 함수 표현식보다 간결한 문법으로 함수를 만들 수 있음

- 인수가 하나밖에 없다면 인수를 감싸는 괄호를 생략 가능

  ```javascript
  let double = n => n * 2;
  
  let double = function(n) { return n * 2; }
  ```

- 인수가 없을 때는 괄호를 비워놓는다, 생략은 불가능

  ```javascript
  let sayHi = () => alert("안녕하세요!");
  
  sayHi()
  ```

- 평가해야할 표현식, 구문이 여러개일 경우 `return` 지시자를 사용해 명시적으로 결과값을 반환해주어야함

<br>

## 과제

### 1️⃣ 화살표 함수로 변경하기

```javascript
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

ask(
  "동의하십니까?",
  function() { alert("동의하셨습니다."); },
  function() { alert("취소 버튼을 누르셨습니다."); }
);
```

```javascript
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

ask(
	"동의하십니까?",
  () => alert("동의하셨습니다."),
  () => alert("취소 버튼을 누르셨습니다.");
);
```

<br>

# 2.18 기본 문법 요약

<br>

### 코드 구조

- 여러개의 구문을 구분하는 방법

  - 코드의 마지막에 **세미콜론**(`;`)을 붙여 구분

  - **줄 바꿈**으로 구분 (세미콜론 자동 삽입 방식)

    - 동작하지 않을 경우가 존재 - 세미콜론을 붙이는 것을 권장

    - 코드 블록 `{...}` 이나 반복문 끝에는 세미콜론을 붙이지 않아도 됨

      - 세미콜론을 만약 붙이게 되더라도 무시됨

      ```javascript
      // 함수 선언문
      function f() {
        
      }
      
      // 반복문
      for () {
        
      } // for문 끝에는 세미콜론 필요 없음
      ```

<br>

### 엄격 모드

- `use strict`를 스크립트 최상단, 함수 본문 최상단에 적어줘야 모던 자바스크립트에서 지원하는 모든 기능 활성화 가능

<br>

### 변수

- `let`
- `const` - 한 번 값을 할당하면 더는 값을 바꿀 수 없는 **상수**를 정의
- `var`

- **변수 이름 규칙**

  - 숫자, 문자 사용 가능 하나 **숫자는 첫 글자에 올 수 없음**
  - 특수기호는 `$`와 `_`만
  - 비 라틴계 언어의 문자나 상형문자도 사용은 가능하나 잘 쓰이지 않음

- **기본 자료형**

  - `숫자형` : 정수와 부동 소수점 저장
  - `BigInt` : 매우 큰 숫자를 저장 숫자 끝에**n**을 붙임
  - `문자형` : 문자열 저장
  - `불린형` : 논리값 true/false 저장
  - `null` : 비어있음, 존재하지 않음을 나타내는 null값만을 위한 독립 자료형
  - `undefined` : 값이 할당되지 않은 상태 나타냄
  - `객체형` : 복잡한 자료구조를 저장
  - `심볼형` : 고유한 식별자를 만들 때 사용

  - **typeof**는 자료형을 반환해주는데, 두 가지 예외사항 존재
    - `null`의 자료형을 object로 반환하는 것은 언어 자체의 오류
    - `function`의 자료형을 function으로 반환

<br>

### 상호작용

- 아래의 함수는 모달 창을 띄워주게 되고, 모달 창이 닫히기 전까지는 이 외의 페이지와 상호작용 불가

- `prompt` : 매개변수로 받은 question을 넣어 사용자에게 보여줌, 확인을 누르면 사용자가 입력한 값 반환, 취소는 null 반환
- `confirm` : 확인을 누를 시  true, 그 외 false를 반환 
- `alert` : 메시지가 담긴 alert창을 보여줌

<br>
