## Python 정리 - (5)

<br>

## 🫥 에러/예외 처리

<br>

### 👾 디버깅

- **`branches`**
  - 모든 조건이 원하는대로 동작하는지

- **`For loops`**
  - 반복문에 진입하는지 , 원하는 횟수만큼 실행되는지

- **`while loops`**
  - for loops와 동일, 종료조건이 제대로 동작하는지

- **`function`**
  - 함수 호출 시, 함수 파라미터, 함수 결과

- **`print 함수 활용`**
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- **`개발 환경(text editor, IDE) 등에서 제공하는 기능 활용`**
  - breakpoint, 변수 조회 등
- **`Python tutor 활용 (단순 파이썬 코드인 경우)`**
- **`뇌컴파일 , 눈디버깅`**

<br>

### 😱 에러와 예외

<br>

#### 문법 에러(Syntax Error)

- SyntaxError가 발생하면 , 파이썬 프로그램은 실행이 되지 않는다

  ```python
  File "<ipython-input-1-f8a097d0a685>", line 1
  if else ^
  SyntaxError: invalid syntax
  ```

- 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿기호(^)를 표시

##### EOL (End Of Line)

```python
print('hello ====> 작은 따옴표로 문자열 안닫음
# File "<ipython-input-6-2a5f5c6b1414>", line 1
# print('hello
# ^
# SyntaxError: EOL while scanning string literal
```

##### EOF (End Of File)

```python
print( ====> )로 안닫아 줬음
# File "<ipython-input-4-424fbb3a34c5>", line 1
# print(
# ^
# SyntaxError: unexpected 
```

##### Invaild syntax - 파이썬 문법에 맞지 않는 경우

```python
while
# File "<ipython-input-7-ae84bbebe3ce>", line 1
# while
# ^
# SyntaxError: invalid syntax
```

##### assign to literal - 변수의 이름은 숫자로 시작될 수 없음

```python
5 = 3
# File "<ipython-input-28-9a762f2c796b>", line
1
# 5 = 3
# ^
# SyntaxError: cannot assign to literal
```

<br>

#### 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중 감지되는 에러들을 예외라고 부름
- 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력
  - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

##### ZeroDivisionError - 0으로 나눌 수 없다는 것

```python
10/0
# ---------------
# ZeroDivisionError Traceback (most recent call last)
# ----> 1 10/0
# ZeroDivisionError: division by zero
```

##### NameError : namespace 상에 이름이 없는 경우

- namespace란 변수명과 객체를 연결한 것 ex. ham = 'spam' , my_number = 7

```python
print(name_error)
# ---------------------------
# NameError Traceback (most recent call last)
# ----> 1 print(name_error)
# NameError: name 'name_error' is not defined
```

##### TypeError : 타입 불일치

```python
# example 1.
1 + '1'
# --------------
# TypeError Traceback (most recent call last)
# ----> 1 1 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# example 2.
round('3.5')
# ---------------
# TypeError Traceback (most recent call last)
# ----> 1 round('3.5')
# TypeError: type str doesn't define __round__ 
```

##### TypeError - arguments 부족

```python
# example 1.
divmod() ====> divmod는 2개의 argument를 필요로하는데 0개 입려됨
# ------------
# TypeError Traceback (most recent call last)
# ----> 1 divmod()
# TypeError: divmod expected 2 arguments, got 0

# example 2.
import random
random.sample()
# ---------
# TypeError Traceback (most recent call last)
# 1 import random
# ----> 2 random.sample()
# TypeError: sample() missing 2 required positional arguments:
'population' and 'k'
```

##### TypeError - argument 개수 초과

```python
# example 1.
divmod(1, 2, 3)
# ---------
# TypeError Traceback (most recent call last)
# ----> 1 divmod(1, 2, 3)
# TypeError: divmod expected 2 arguments, got 3

# example 2.
import random
random.sample(range(3), 1, 2)
# --------
# TypeError Traceback (most recent call last)
# 1 import random
# ----> 2 random.sample(range(3), 1, 2)
# TypeError: sample() takes 3 positional arguments but 4 were given
```

