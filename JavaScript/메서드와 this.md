# 메서드와 this

- 객체의 프로퍼티에 함수 부여하여 객체에 행동할 수 있는 능력 부여

```javascript

let user = {
	name : 'John',
	age : 30,
};

user.sayHi = function() {
	alert('안녕하세요!');
};

user.sayHi(); // 함수 호출 // 안녕하세요 alert 창에 출력

console.log(user);
// {name: 'John', age: 30, sayHi: ƒ}

```

- 객체 프로퍼티에 할당된 함수를 메서드(method)라고 부름
- 직접 변수에 함수 할당하는 방법도 존재하나, 이미 정의된 함수 이용해서 할당하는 방법도 존재

- 메서드 내부에서 this 키워드 사용시 객체에 접근 가능
	- 내부에서 **this** 사용 시 메서드를 호출할 때 사용된 객체를 나타냄
	- 즉 `let user = { ... }` 내부의 프로퍼티 메서드 내부에 `this.name` 이런식으로 접근을 한다면
		- **this**는 **user**를 나타냄
	- **this**를 사용하지 않고 `user.name`으로도 접근이 가능한데 이 경우 유의할 점 존재

```javascript

let user = {
	name : 'John',
	age : 30,
	sayHi() {
		alert( user.name );
	}
};

let admin = user; // user 객체를 admin에 복사
user = null; // user 전체를 null로 덮어씀

// 이 경우
console.log(user); // null
console.log(admin); 
// { name : 'John', age : 30, sayHi() { alert( user.name ) } };

admin.sayHi();
// VM9270:6 Uncaught TypeError: Cannot read properties of null (reading 'name') at Object.sayHi

// 이런식으로 null값을 참조 this.name을 인수로 받았다면 에러가 발생하지 않음

```

- 외부에 함수를 생성하고, 그 값을 객체의 프로퍼티에 할당해서 호출할 경우
	- **this**가 참조하는 값이 달라짐

```javascript

let user = { name : 'John' };
let admin = { name : 'Dahlia' };

function sayHi() {
	alert( this.name );
}

user.f = sayHi;
admin.f = sayHi;

// this는 .앞의 객체를 참조

user.f(); // John
admin.f(); // Dahlia

// 대괄호 표기법도 동일하게 동작 user['f']();

```

- 엄격 모드에서 실행한다면 **this**에는 `undefined` 할당
- 엄격 모드가 아닐 경우에는 **this**가 전역 객체를 참조 `window`
- 화살표 함수에서 this를 참조할 경우, 외부 함수에서 this값을 가짐

```javascript

let user = {
	firstName: "보라", 
	sayHi() { 
		function arrow() {
			alert(this.firstName); 
		}
		// 여기서는 this가 object Window
		// 참조되는 this.firstName이 없기 때문에 undefined 출력
		arrow(); 
	} 
}; 

user.sayHi(); // undefined


let user = { 
	firstName: "보라", 
	sayHi() { 
		let arrow = () => alert(this.firstName); 
		// console.log(this)를 할 경우
		// {firstName: '보라', sayHi: ƒ}
		// this.firstName에 접근 가능
		arrow(); 
	}
}; 

user.sayHi(); // 보라

```

<br>

### 과제

### 객체 리터럴에서 'this' 사용하기

```javascript

function makeUser() { 
	return { 
		name: "John", 
		ref: this 
	}; 
}; 
	
let user = makeUser(); 
alert( user.ref.name ); 
// 결과가 어떻게 될까요?

// error 발생
// makeUser() 내의 this는 메서드로 호출 된게 아니고 함수로서 호출
// 즉 this의 값은 전체 함수가 됨
// John이 나오게 만들려면

function makeUser() { 
	return { 
		name: "John", 
		ref() {
			return this;
		}
	}; 
}; 

let user = makeUser(); 
alert( user.ref().name ); // user.ref() 메서드가 되고 앞의 객체가 되기 때문에 에러 발생안하고 John 출력

```

<br>

### 계산기 만들기

```javascript

let calculator = {
	num1 : 0,
	num2 : 0,
	read() {
		const input = prompt('더할 값 공백을 기준으로 두 개 입력하세요.');
		let numbers = input.split(' ');
		this.num1 = Number(numbers[0]);
		this.num2 = Number(numbers[1]);
	},
	sum() {
		return (this.num1 + this.num2);
	},
	mul() {
		return (this.num1 * this.num2);
	},
}

calculator.read(); 
// 더할 값 두개 받고 프로퍼티에 저장
alert( calculator.sum() );
alert( calculator.mul() );

```
<br>


### 체이닝

```javascript

let ladder = { 
	step: 0, 
	up() { 
		this.step++; 
		return this;
	}, 
	down() { 
		this.step--;
		return this;
	}, 
	showStep: function() { 
	// 사다리에서 몇 번째 단에 올라와 있는지 보여줌 
		alert( this.step ); 
		return this;
	} 
};

ladder.up().up().down().showStep();

// 메서드 호출 체이닝이 가능토록 만들 것

```

<br>
