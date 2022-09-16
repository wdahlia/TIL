# JavaScript

🔒 **학습 목차**

`JavaScript`





## JavaScript

> 브라우저를 조작하기 위한 언어

- 브라우저 화면을 `동적`으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어
- `동적`이란?
  - 페이지 내용이 주기적으로 갱신되거나,
  - 사용자와의 상호작용이 가능
  - 애니메이션이 적용된 2D/3D 그래픽 보는 것이 가능
- **JS의 탄생**
  - 제1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨
  - 서로 다른 자바스크립트(파편화)로 인해 크로스 브라우징 이슈가 발생, 웹 표준의 필요성 제기
  - `크로스 브라우징(Cross Browsing)`
    - W3C에서 채택 된 표준 웹 기술을 이용
    - 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되 어느 한쪽에 치우치지 않도록 웹 페이지 제작 (동일성이 아닌 동등성)
    - 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문
  - 현재는 JavaScript ES6+로 표준 대부분이 넘어오게 되었음

- (참고) MAC에서 console 여는 법
  - `command` + `option` + `J`
- (참고) MAC에서 console 깨끗하게 만드는법
  - `clear()` 입력 or `cmd` + `K`
- **내부 JavaScript**
  - HTML 코드에 `<script>`,  `</script>` 이용하여 코드를 넣는 방법
- **외부 JavaScript**
  - 파일명.js 파일 생성 후 `<script src="파일명.js" defer></script>` 로 HTML에 코드를 대체
  - 파일명.js 안에 코드 입력

<br>

## 👩🏻‍💻 JavaScript 기초

### Variables (변수)

#### 💡 let

- ```javascript
  let name = jinsook;
  // name 을 입력하면 jinsook을 출력하게 됨
  ```

- 변수이름을 지정하는 방법 `let` + 변수이름 = 값

  ```javascript
  let numapples = 5;
  let numgrapes = 3;
  // numapples + numgrapes을 하게 되면 8을 출력
  ```

- 순간을 스냅샷으로 찍은 것과 같다고 생각할 것. 서로 연결되어 있지 않음

  ```javascript
  // 예를 들어,
  let numapples = 5;
  let numgrapes = 3;
  let numfruits = numapples + numgrapes;
  // 이 경우 numfruits를 입력하면 8이 나오게 된다
  numapples = 3;
  // numapples를 5에서 3으로 업데이트하고 numfruits를 출력한다면 어떤 결과가 나올까?
  // 8이 나오게 된다. 즉, 연결 되어있어 자동으로 변경되지 않는다는 뜻
  numfruits = numapples + numgrapes;
  // 이렇게 다시 재할당을 해주어야지만 numapples의 변한값으로 더해져서 6이 출력된다.
  ```

- **변수 업데이트 방법**

  ```javascript
  // 이렇게 업데이트 해주면 됨
  numapples += 3;
  // 1씩 늘어나게 해주거나, 1씩 줄어들게 하는 법
  numapples--, numapples++
  ```

- **재선언 불가능**

  ```javascript
  let numapples = 5;
  let numapples = 3;
  // 이 경우 error 반환
  ```

<br>

#### 💡 const

> 상수의 줄임말

- ```javascript
  const luckyNum = 26;
  // 이렇게 하고 luckyNum을 업데이트 해보면
  luckyNum += 1;
  // Uncaught TypeError를 반환한다. 상수값은 고정 값을 늘리거나 변경 불가능
  luckyNum = 1;
  // 이것 역시도 error 반환
  ```

- 불변의 값을 보통 const로 해서 상수값으로 지정

  - ex) 원주율, 마일, km와 같은 것들 
  - **근데 이것들을 위해서 const를 사용하는 경우는 매우 드문 경우**

- array나 object를 배우고 나면 좀더 명확하게 const가 유용한 이유에 대해 파악 가능

<br>

#### 💡 var

> let과 차이점은 있지만 비슷함

- 예전 자바스크립트에서 유일하게 변수를 만드는데 이용되었던 방법
- `var`로 선언한 변수는 **재선언 및 재할당 모두 가능**
- 현재도 유효함



##### 호이스팅 (hoisting)

<br>

### Data Type

### Primitive type (원시 타입)

> 객체(object)가 아닌 기본 타입

- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨

#### Number (숫자)

- 한 타입만 존재 - 즉, 양수, 음수, 정수, 소수 모두 포함 (어떤 언어에서는 숫자가 여러 타입들로 존재)

- 숫자는 메모리에서 특정한 양의 공간을 갖게 됨. 즉, 메모리 공간에 한계가 존재

- 내장된 기본 연산자가 존재 (`+`, `-`, `*`, `/`, `%`, `**`)

- `NaN` - **Not A Number**

  - `0/0` - 수학적으로는 의미 없는 연산 

  - 하지만,  JS에서는 값을 출력해줌 이때 출력되는 값이 NaN

  - ```javascript
    type of NaN
    //"number"을 출력해준다
    ```

  - 즉, 숫자가 아닌 값을 나타내는 NaN은 JS에서는 숫자 타입 또는 숫자 패밀리 중 하나로 간주된다

  - `NaN * NaN` 도 NaN이 나오게 된다

<br>

#### String (문자열)

> "", '' 로 감싸 주어야함

- `변수명/문자열.length` - 문자의 수
-  

<br>

#### Booleans (불리언)

> true / false

- 조건문 / 반복문에서 유용하게 사용

  - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true or false로 변환됨

    |  데이터 타입  |    거짓    |        참        |
    | :-----------: | :--------: | :--------------: |
    | **Undefined** | 항상 거짓  |        X         |
    |   **Null**    | 항상 거짓  |        X         |
    |  **Number**   | 0, -0, NaN | 나머지 모든 경우 |
    |  **String**   | 빈 문자열  | 나머지 모든 경우 |
    |  **Object**   |     X      |     항상 참      |

  - 직관적으로 보았을때 `Undefined`, `Null`, `0`, `NaN`, `빈 문자열` 처럼 비어있다고 느껴지는 것들은 모두 false

  - 단, '0' 즉, 문자열 0의 경우는 비어 있지 않으므로 true입니다

<br>

#### Undefined

<br>

#### null



 





### 브라우저 (browser)

> URL로 웹을 탐색하며 서버와 통신, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어

- 인터넷의 컨텐츠를 검색 및 열람하도록 함
- 주요 브라우저 : Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari



### DOM

> 문서 객체 모델

- HTML, XML과 같은 문서를 제어하기 위한 문서 프로그래밍 인터페이스

- 문서를 구조화, 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - `window` :  DOM을 표현하는 창, 가장  최상위 객체(작성 시 생략 가능)









1. \1. 숫자 값에 숫자가 아닌 값을 덧셈 연산하면 가능한 경우 숫자가 아닌 값을 숫자 값으로 변환합니다. 그렇지 않으면 둘 다 문자열로 변환됩니다. 2. 숫자가 아닌 값을 어떤 값에 덧셈 연산하면 그 전에 두 값을 문자열로 변환합니다.