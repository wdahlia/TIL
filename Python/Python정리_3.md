# 📓 Python 정리 - (3)

- 참고사이트 :  [파이썬 자습서](https://docs.python.org/3/) , [파이썬 코딩 도장](https://dojang.io/course/view.php?id=7) , [Argument 참고](https://velog.io/@taeha7b/python-parameter-argument) , [LEGB 룰](https://velog.io/@maxkmh/Python-08-LEGB-%EA%B7%9C%EC%B9%99) , [map](https://jimmy-ai.tistory.com/50)

## 함수

- **`Decomposition`** - 기능을 분해, 재사용 가능

- **`Abstraction`** - 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음. 재사용성, 가독성, 생산성
  - print('happy!') 가 있을때 happy!를 출력하는 print라는 함수가 어떻게 happy!를 출력하는지 우리는 모름
  - 복잡한 내용을 숨기고는 있지만 print라는 것을 파이썬에서 사용한다면 happy!는 출력

- 특정한 기능을 하는 코드의 조각(묶음)

- 특정 명령을 수행하는 코드를 매번 작성하지 않고, 필요 시에만 호출하여 간편히 사용

> 함수를 사용해야 하는 이유 ?

- 코드 중복 방지

- 재사용 용이 
- 복잡한 내용을 간편하게 표현 가능

<br>

### 함수의 기본 구조

> 빠르게 확인 🔽

- [선언과 호출(define & call)](#선언과-호출)
- [입력(Input)](#입력)
- [범위(Scope)](#범위)
- [결과값(Output)]()
- [함수 응용](#함수-응용)

<br>

#### 선언과 호출

````
1. 함수의 선언은 def 키워드를 활용
2. 들여쓰기를 통해 Function body(실행될 코드 블록)을 작성함
3. 함수는 parameter(매개변수)를 넘겨줄 수 있음
4. 함수는 동작 후에 return을 통해 결과값을 전달함
````

- 함수는 함수명()으로 호출

  - parameter가 있는 경우, 함수명(값1, 값2, ...)로 호출

    ```python
    def add(x,y):
      return x + y
    
    # add(2,3)
    # return 5
    ```

> 즉, 함수는 호출되면 코드를 실행 return 값을 반환하며 종료

<br>

#### 입력

- **`Parameter`** 

  - 함수를 실행할 때, 함수 내부에서 사용되는 식

- **`Argument`** 

  - 함수 호출 시, 함수의 parameter를 통해 전달되는 값 (= 넣어주는 값)

  - Argument는 소괄호 안에 할당 func_name(argument)

    - 필수 Argument : 반드시 전달되어야 하는 Argument

    - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

      ```python
      def average(a,b,c):    # parameter : a,b,c
        s = a+b+c
      average(10,20,30)     # argument : 10,20,30
      ```

    - **Positional Arguments**

      - 위치에 맞게 argument들이 parameter값으로 들어간다는 것

        ```python
        def add (x, y, z):
          return x + y
        
        add(2, 4, 5)
        # 함수의 parameter에 input값으로 들어갈때 순서대로 들어감
        									2 > x
        									4 > y
        									5 > z	
        ```

      - 가변인수(**variable length arguments**)

        - 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용

        - argument들은 튜플로 묶여 처리, parameter에 *를 붙여 표현

          ```python
          # def 함수이름(*매개변수이름)
          # 가변 매개변수 사용 시 관습상 *args 사용
          ex1)
          def foo(*args):
            result =0
          
          for i in args:
            result += i
          return result
          
          ex = foo(1,2,3,4,5,6,7,8,9,10)
          print(ex)
          # 실행결과는 55
          
          ex2)
          def foo(*args):
            return args
          
          ex = foo('류진숙', '체다', 'soulmate')
          print(ex)
          # 실행결과 ('류진숙', '체다', 'soulmate')
          ```

    - **Keyword Arguments**

      - positional argument의 경우에는 순서가 중요 but, 키워드 인수의 경우에는 인수들의 순서가 중요치 X

      - *keyword argument 다음에 positional argument를 활용할 수 없음*

      - ```python
        add(x, y, z):
          return x + y + z
        # add(x=2, y=5, z=3)
        # add(2, y=5, z=3) 
        # 따로 값이 정해지지 않는다면 y=5가 기본값
        # add(x=2, 5, 3) (X)
        # 키워드 인수는 키워드에 맞게 들어가나, 위치인수는 자신이 매개변수 어디에 들어가야 할지 모르게 됨
        # error massage
        <SyntaxError: positional argument follows keyword argument>
        ```

      - 매개변수의 이름에 맞춰 값을 함수에 전달하기 때문에 값을 함수에 전달하기에 위치가 바뀌어도 괜찮고, 실수로 함수에 잘못 전달하는 실수를 사전에 예방할 수 있다.

      - 키워드를 사용하기에 어떤 값을 함수의 매개변수로 넘기는지 명확하게 알 수 있어 가독성이 높아짐

      - 가변 키워드 인수(**variable length keyword arguments**)

        - 임의의 개수 argument를 keyword argument로 호출 

        - argument들은 딕셔너리로 묶여 처리, parameter 앞에 **를 붙여 표현

          ```python
          def family(**kwargs):
              return(kwargs)
          
          my = family(father='John', mother='dahlia')
          print(my)
          # 답 {'father': 'John', 'mother': 'dahlia'} 출력
          ```

<br>

#### 범위

- 함수는 코드 내부에 local scope를 생성, 그 외의 공간인 global scope으로 구분

- **`LEGB RULE`**

  <p align="center"><img src="https://user-images.githubusercontent.com/108653518/178732579-b43b0549-be17-4add-a350-e6e8294e711f.png" alt="image-103"  />

  - **Local Scope**

    - 함수 안을 의미

  - **Enclosed Scope**

    - 함수를 내포하는 또다른 함수의 공간

  - **Global Scope**

    - 함수 밖의 변수, 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

  - **Built-in scope**

    - 파이썬 안에 내장되어 있는 함수 또는 속성, 파이썬이 실행된 이후부터 영원히 유지

  - 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

  - `Local 예시`

    ```python
    # child_func() 함수 안이 local 영역이고 여기서 변수를 찾음 a가 정의되어져 있음
    # 즉, 도출되는 값은 a = 20
    
    a = 30
    
    def child_func():
        a = 20
        return a
    
    print(child_func())
    
    ```

  - `Enclosed Scope 예시`

  - ```python
    # 첫번쨰 local 영역에 return a만 있고 a값이 할당되어져 있지 않기에
    # enclosed 영역으로 감
    # enclosed 영역 에는 a = 10 할당되어져 있음 
    # 정답은 10
    
    a = 30
    
    def parent_func():
        a = 10
        def child_func():
            return a
    
        return child_func()
    
    print(parent_func())
    
    ```

  - `Global 예시`

    ```python
    # 첫번째 로컬인 영역과 두번째 enclosed 영역에 모두 할당된 a가 없음 
    # global을 확인 a = 30 할당 되어져 있음
    # 정답은 30
    a = 30
    
    def parent_func():
        def child_func():
            return a
    
        return child_func()
    
    print(parent_func())
    
    ```

<br>

#### 결과값

- 함수는 반드시 값을 하나만 return 한다.
  - 명시적인 return이 없는 경우에도 None을 반환한다.
- 함수는 return과 동시에 실행이 종료
- `return`은 **함수 안에서 값을 반환하기 위해 사용되는 키워드** 
- `print`는 **출력을 위해 사용되는 함수**

> 아래 코드의 문제점은?

<p align="center"><img width="339" alt="스크린샷 2022-07-13 오후 9 46 02" src="https://user-images.githubusercontent.com/108653518/178736986-97aad606-4814-4d52-bc16-8bb9a299a563.png">	

- 절대 실행되지 않는 return

> return문을 한번만 사용하면서 두 개 이상의 값을 반환하는 방법 존재?

<p align = "center"><img width="340" alt="스크린샷 2022-07-13 오후 9 51 56" src="https://user-images.githubusercontent.com/108653518/178738070-a0eb8e69-f401-4716-95d4-e9f0a6f63fb5.png">

- 튜플 반환 

  ```python
  # 위의 함수에
  m = minus_and_product(5, 7)
  print (m, type(m))
  # 답은 (-2, 35) <class 'tuple'>
  ```

<br>

#### 함수 응용

- 파이썬 내장함수
  - <https://docs.python.org/ko/3/library/functions.html> 👈🏻 확인 가능

- **`map`**

  - **map(<span style="color:red">적용할 함수</span>, <span style="color:green">순회 가능한 객체</span>)**

    - 순회 가능한 객체의 각 원소에 지정한 함수를 각각 적용하여 결과를 반환하는 함수
    - map 사용 예시

    ```python
    map(int, ['1', '2', '3', 4.5, 5.9]) # map object at 0x10136ffa0 이런식의 결과값 나옴
    list(map(int, ['1', '2', '3', 4.5, 5.9]) # [1, 2, 3, 4, 5] list로 전환해서 봐줘야지 보임
    ```

    ```python
    def game_result(x):
        if x == '가위':
            return 'win'
        elif x == '보':
            return 'draw'
        else:
            return 'lose'
    
    game_list = ['가위', '바위', '보', '가위', '안냄']
    
    result = list(map(game_result, game_list)) # ['win', 'lose', 'draw', 'win', 'lose']
    ```

<br>