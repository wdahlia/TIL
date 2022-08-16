# Python 정리 (2)

> **참고사이트 정리**

- [왕초보를 위한 python](https://wikidocs.net/book/2)
- [초보자를 위한 python 300제](https://wikidocs.net/book/922)
- [점프 투 파이썬](https://wikidocs.net/book/1)

<details>
<summary>🔓 Python 정리 (1) 목차 </summary>
</details>

> 빠르게 내가 원하는 것만 확인

- [조건문](#조건문)
  - [복수 조건문](#복수-조건문)
  - [중첩 조건문](#중첩-조건문)
- [반복문](#반복문)

## `제어문`

- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요
- 제어문은 순서도로 표현이 가능

### 조건문

- ㅁ참/거짓을 판단할 수 있는 조건식과 함께 사용

- **기본형식**

  - expression에는 참/거짓에 대한 조건식

    - 조건이 참인 경우 들여쓰기(Tab or Space 4번) 되어 있는 코드 블럭 실행
    - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행
      - else는 선택적으로 활용 가능

    ```python
    a = -4
    if a >= 0:
        print('양수')
    else:
        print('음수')
        
    # 프린트 결과는 음수
    ```

- ##### **복수 조건문**

  - elif를 활용하여 표현 (코드는 위에서 아래로 읽는다는 것 명심)
  
    - elif 사용해서 미세먼지 농도 사용 표현할때 x <= a < y 이런 식으로 코드 구성할 필요성 X
    - 코드는 위에서 아래로 읽는다
    - 만약, 80이라는 미세먼지 농도 관측 된다면 첫번째 if에서 150보다 크지않으므로 나머지 값들은 필터링 됨
    - 밑으로 내려와서 dust > 30 : print('보통') 의 조건에 만족 
    - 결과는 '보통', '미세먼지 확인완료' 가 출력 될 것
  
    ```python
    dust = 80
    
    if dust > 150:
      print('매우 나쁨')
    elif dust > 80:
      print('나쁨')
    elif dust > 30:
      print('보통')
    else:
      print('좋음')
      
    print('미세먼지 확인 완료')
    ```
  
- ##### **중첩 조건문** 

  - 조건문은 다른 조건문에 중첩되어 사용 가능
  
    - 들여쓰기 유의하여 작성
    - *만약, 미세먼지 농도(dust 값)이 300이 넘는 경우 '실외 활동을 자제하세요' 추가적으로 출력하고 싶다면?*
  
    ````python
    dust = 80
    
    if dust > 150:
      print('매우 나쁨')
    elif dust > 80:
      print('나쁨')
    elif dust > 30:
      print('보통')
    else:
      print('좋음')
      
    print('미세먼지 확인 완료')
    ````
  
  - 
  

### 조건표현식

elif이런 것들은 안됨 쓰는순간 코드가 어지러워짐

- 조건에 따라 값을 정할 때 활용

value = num if num >= 0 else -num - 변환하는법 그림으로 표현할 것

```python
num = int(input())
if num >= 0:
  value = num
else:
  value = -num
print(value)
```

### 반복문

[Python Tutor](https://pythontutor.com/)라는 사이트에서 실행해 볼 수 있음

- while문
  - 조건식이 참인 경우 반복적으로 코드 실행
  - **종료조건에 해당하는 코드**를 통해 반복문을 **종료**
- for문
  - 시퀀스(string, tuple, list, range) 를 포함한 순회가능한 객체요소를 모두 순회함
  - 반복가능한 객체를 모두 순회하면 종료 = **별도의 종료조건이 필요하지 않음**
    - 그냥 요소
    - range - 인덱스 접근
    - 딕셔너리 기본 key
- 반복 제어

#### while문



#### for문





#### 반복문 제어

- break
  - 반복문을 종료
- continue
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- for-else
  - 끝까지 반복문을 실행한 이후에 else문을 실행



