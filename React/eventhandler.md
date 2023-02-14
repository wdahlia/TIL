# event handler
Event handler 함수는
- `handle`로 시작 하는 경우가 많음
- 컴포넌트 안에 정의가 되고 방식은 inline으로 작성할 수도 있고 따로 함수를 정의해줄 수도 있다

- **함수 정의**
```jsx

export default function Button() {
	function handleClick() {
		alert('You clicked me!');
	}

	return (
		<button onClick={handleClick}>
			Click me
		</button>
	);
}

```

- **inline 방식**
```jsx

// inline에 함수 정의
export default function Button() {
	return (
		<button onClick={function handleClick() {
			alert('You clicked me!');
		}}>
			Click me
		</button>
	);


// inline에 화살표 함수

export default function Button() { 
	return (
		<button onClick={() => {
			alert('You clicked me!');
		}}>
			Click me
		</button>
	)
}

```

- 동일한 실행결과 출력
![[스크린샷 2023-02-14 오후 6.50.04.png]]

### 참고
- event handler 함수는 passing a function 이어야 하지 calling a function 이면 안된다
```jsx
	<button onClick={handleClick}></button>  // O
	<button onClcick={handleClick()}></button> // X
```

- `handleClick`의 경우는 유저로 인해 onclick 이라는 이벤트가 실행되기 전에는 handleClick이라는 함수를 pass 한다.
- 반면, `handleClick()`은 렌더링이 이루어 질때마다 함수를 실행, 즉 클릭 이벤트와 같은 것이 실행되지 않더라도 함수가 실행된다는 것

```jsx

// inline일 때
<button onClick={alert('You clicked me')}></buttton>
// render될 때마다 실행됨, 이벤트 없이도!
<button onClick={() => alert('You clicked me')}></button>

```

- `button`, `div`와 같이 built-in 된 컴포넌트는 onClick과 같은 browser event name을 사용해주어야하지만,
- 내가 직접 만든 컴포넌트의 경우, on-으로 시작하고 따라 붙는 단어의 시작이 대문자인 event handler props를 만들 수 있다.

```jsx

	function Button({ onSmash, children }) {
	  return (
	    <button onClick={onSmash}>
	      {children}
	    </button>
	  );
	}
	
	export default function App() {
	  return (
	    <div>
	      <Button onSmash={() => alert('Playing!')}>
	        Play Movie
	      </Button>
	      <Button onSmash={() => alert('Uploading!')}>
	        Upload Image
	      </Button>
	    </div>
	  );
	}

```

- `e.stopPropagation()`은 같은 이벤트들이 모든 element에 먹혀있을 때, 버블링과 캡쳐링을 막아줌, 즉 부모요소로 버블링이 되거나 자식요소로 캡쳐링 되는 것을 막고 예를 들면 내가 누른 버튼 요소 하나만 실행되게끔 만들어주는 것
- browser event 중에는 default behavior를 가진 것들이 있음 form 안의 submit 이벤트가 그러함. 버튼을 클릭하게 되면 window가 reload 됨
- 그때, `e.preventDefault()`를 사용

-  [`e.stopPropagation()`](https://developer.mozilla.org/docs/Web/API/Event/stopPropagation) stops the event handlers attached to the tags above from firing.
-   [`e.preventDefault()`](https://developer.mozilla.org/docs/Web/API/Event/preventDefault) prevents the default browser behavior for the few events that have it.