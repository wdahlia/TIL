# new 연산자와 생성자 함수

- 유사한 객체를 여러개 만들고자 할때 **new** 연산자와 생성자 함수를 사용한다면 가능

```javascript

function User(name) {
	// this = {} 빈 객체가 암시적으로 만들어짐
	// 새로운 프로퍼티를 this에 추가함
	this.name = name;
	this.isAdmin = false;

	// return this; this가 암시적으로 반환됨
}

let user = new User('Dahlia');
let user = {
	name : 'Dahlia',
	isAdmin : false,
};

console.log(user);

```

- `new User('John')`, `new User('Soo')` 이런식으로 여러 사용자 객체를 생성 가능
- 재사용할 수 있는 객체 생성 코드 구현 가능
- 첫글자가 대문자인 함수는 **new**를 붙여 실행해야 한다
- 재사용할 필요가 없는 복잡한 객체는 `new function() { ... }`
	- 한 번만 호출할 목적, 재사용 막으면서 코드를 캡슐화
- 생성자 함수에는 return문 존재하지 X
	- 반환해야 할 것은 모두 **this**에 저장되고, **this**는 자동 반환 되기 때문에 명시할 필요성 존재 X
		- retrun 객체를 반환하면 해당 객체를 반환, 이 외의 경우에는 this 반환
- 생성자 내부에 메서드 추가도 가능

<br>

## 과제

### 함수 두 개로 동일한 객체 만들기
```javascript

// return 값으로 객체를 반환하게 하면 가능

const obj = {};

function A() { return obj }
function B() { return obj }

let a = new A;
let b = new B;

alert( a == b ); // true 반환

```
<br>

### 계산기 만들기

```javascript

function Calculator() {
	this.read = function() {
		let input = prompt('숫자 2개 공백을 기준으로 입력 받기');
		input = input.split(' ');
		this.num1 = Number(input[0]);
		this.num2 = Number(input[1]);
	},
	this.sum = function() {
		return (this.num1 + this.num2);
	},
	this.mul = function() {
		return (this.num1 * this.num2);
	}
}
let calculator = new Calculator();
calculator.read();

alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );

```
<br>

### 누산기 만들기

```javascript

function Accumulator(value) { 
	this.value = value;
	this.read = function() {
		this.value += Number(prompt('더할 숫자를 입력하세요'));
	}
}

let accumulator = new Accumulator(1); // 최초값: 1 
accumulator.read(); // 사용자가 입력한 값을 더해줌 
accumulator.read(); // 사용자가 입력한 값을 더해줌 
alert(accumulator.value); // 최초값과 사용자가 입력한 모든 값을 더해 출력함

```
<br>
