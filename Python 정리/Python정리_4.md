# **📓** Python 정리 - (4)

[참고 링크](#참고-링크)

## 데이터 구조

- `타입. + 메서드()`

```
- 타입 = 누가

- () = input 

- 타입.메서드() = output
```

<br>

### 시퀀스 - 순서가 있는 데이터 구조

#### 📚 문자열

- 문자들의 나열
  - 모든 문자는 str 타입

| 예시 확인하려면 클릭✔️                  |                                                              |
| :------------------------------------- | ------------------------------------------------------------ |
| **`문자열 탐색`**                      |                                                              |
| [.find(x)](#1번)                       | x의 첫 번째 위치를 반환. 없으면, -1을 반환                   |
| [.index(x)](#2번)                      | x의 첫 번째 위치를 반환. 없으면, 오류 발생                   |
| [.isdecimal()](#3번)                   | 문자열 관련 검증 - 주어진 문자열이 int로 반환 가능한가 여부 검사 |
| **`문자열 변경`**                      | 문자열도 스스로 바뀌는 경우 X (immutable ) , 모두 바뀐 결과를 반환한다 |
| [.replace(old, new[,count])](#4번)     | 👉🏻 바꿀 대상 글자를 새로운 글자로 바꿔서 반환<br>👉🏻 count를 지정하면, 해당 개수만큼만 시행 |
| [.strip([chars])](#5번)                | 👉🏻 특정한 문자를 지정하면,<br>👉🏻 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(strip)<br>👉🏻 문자열을 지정하지 않으면 **공백(space, '\n')을 제거함** ▶️ 제일 많이 사용 |
| [.split(sep=None, maxsplit=-1))](#6번) | 👉🏻 문자열을 특정한 단위로 나눠 리스트로 반환                 |
| ['seperator'.join([iterable])](#7번)   | 👉🏻 반복가능한 컨테이너 요소들을 seperator(구분자)로 합쳐 문자열 반환<br>👉🏻 () 안에 문자열이 아닌 값이 있으면 TypeError 발생 |
| [기타 문자열 변경 예시](#8번)          |                                                              |

<br>

#### 📚 리스트

- 변경 가능한(mutable) 값들의 나열된 자료형, 반복 가능함(iterable)

  ``` python
  # 리스트는 mutable(변경 가능한 값)
  a = [1,2,3]
  a[0] = 100
  print(a)
  # [100, 2, 3]
  
  # 문자열은 immutable
  a = 'hi'
  a[0] = 'c'
  print(a)
  # Traceback (most recent call last):
  #   File "C:\Users\hphk\Desktop\TIL\python\4일차\04_mutable.py", line 8, in <module>
  # 		a[0] = 'c'
  # TypeError: 'str' object does not support item assignment
  ```

- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

<br>

| 예시 확인하려면 클릭✔️      |                                                              |
| :------------------------- | ------------------------------------------------------------ |
| 👩🏻‍💻 **`값 추가 및 삭제`**  |                                                              |
| [.append(x)](#9번)         | 리스트 마지막에 항목 x를 추가                                |
| [.expend(iterable)](#10번) | 👉🏻 ()안의 항목을 추가<br>👉🏻 여러개 추가하려면 꼭 리스트로 묶어서 넣어줘야함<br>👉🏻 문자열 'banana'만 넣게되면 'b', 'a', 'n', 'a', 'n', 'a' 이렇게 추가됨 |
| [.insert(i, x)](#11번)     | 정해진 위치 i에 값을 추가함. 리스트 인덱스 i에 항목 x를 삽입 |
| [.remove(x)](#12번)        | 👉🏻 리스트에서 값이 x인 것 삭제<br>👉🏻 이미 리스트에 없는데 실행한다면 ValueError 뜸 |
| [.pop(i)](#13번)           | 👉🏻 정해진 위치 i에 있는 값을 삭제, 그 항목을 반환<br>👉🏻 i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함 |
| [.clear()](#14번)          | 모든 항목을 삭제                                             |
| 👩🏻‍💻 **`탐색 및 정렬`**     |                                                              |
| [.index(x)](#15번)         | x값을 찾아 해당 index 값을 반환                              |
| [.count(x)](#16번)         | 원하는 값의 개수를 반환함                                    |
| [.sort()](#17번)           | 👉🏻 원본 리스트를 정렬함. None 반환<br>👉🏻 sorted 함수와 비교할 것 |
| [.reverse()](#18번)        | 순서를 반대로 뒤집음(정렬하는 것이 아님). None 반환          |

<br>

### 컬렉션 - 순서가 없는 데이터 구조

#### 📚 세트

- 유일한 값들의 모음(collection)
- 순서가 없고 중복된 값이 없음
  - 수학에서의 집합과 동일한 구조, 집합 연산도 가능
- 변경 가능, 반복 가능
  - 단, 세트는 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음

| 예시 확인하려면 클릭✔️ |                                                              |
| :-------------------- | ------------------------------------------------------------ |
| .copy()               | 세트의 얕은 복사본을 반환                                    |
| .add(x)               | 항목 x가 세트 s에 없다면 추가                                |
| .pop()                | 세트 메서드                                                  |
| .remove(s)            | 👉🏻 세트s에서 랜덤하게 항목을 반환하고<br>👉🏻 해당 항목을 제거 세트가 비어 있을 경우, KeyError |
| .discard(x)           | 👉🏻 항목 x를 세트 s에서 삭제<br>👉🏻 항목이 존재하지 않을 경우, KeyError |
| .update(t)            | 항목 x가 세트 s에 있는 경우, 항목 x를 세트s에서 삭제         |
| .clear()              | 세트 t에 있는 모든 항목 중 세트 s에 없는 항목을 추가         |
| .isdisjoint(t)        | 모든 항목을 제거                                             |
| .issubset(t)          | 세트 s가 세트 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환 |
| .issuperset(t)        | 세트 s가 세트 t의 하위 세트인 경우, True반환                 |

<br>

#### 📚 딕셔너리

- Key - Value 쌍으로 이루어진 모음
  - key 
    - 불변 자료형만 가능 (리스트, 딕셔너리 불가)
  - values
    - 어떠한 형태든 가능
- 변경 가능, 반복 가능
  - 딕셔너리는 반복하면 키가 반환

| 예시 확인하려면 클릭✔️        |                                                              |
| :--------------------------- | ------------------------------------------------------------ |
| **`조회`**                   |                                                              |
| [.get(key[,default])](#19번) | 👉🏻 key를 통해 value를 가져옴<br>👉🏻 KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본 : None) |
| **`추가 및 삭제`**           |                                                              |
| [.pop(key[,default])](#20번) | 👉🏻 key가 딕셔너리에 있으면 제거하고 해당 값을 반환<br>👉🏻 그렇지 않으면 default를 반환, default값이 없으면 KeyError |
| [.update([other])](#21번)    | 값을 제공하는 key, value로 덮어씌웁니다.                     |
| [.keys()](#22번)             | 딕셔너리 d의 모든 키를 담은 뷰를 반환                        |
| [.values()](#23번)           | 딕셔너리 d의 모든 값을 담은 뷰를 반환                        |
| [.items()](#24번)            | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환                |

<br>

<br>

<br>

<br>

<br>

## 예시

###### 1번

> .find(x)

```python
 print('apple'.find('p')) 
 #1 
 print('apple'.find('k')) 
 # -1
```

###### 2번

>.index(x)

```python
print('apple'.index('p’))              
#1
                   
'apple'.index('k')
# ------------------------------------------- 
# ValueError Traceback (most recent call last) 
# ----> 1 'apple'.index('k')
# ValueError: substring not found
```

###### 3번

>.isdecimal()

``` python
a = '3²'
print(a.isdecimal())
# False
```

###### 4번

>.replace(old, new[,count])

```python
 print('coone'.replace('o', 'a’))
# caane o의 자리에 a를 넣는다
print('wooooowoo'.replace('o', '!', 2)) 
# w!!ooowoo
# count 2 지정 즉 두개 변경 !!
```

###### 5번

>.strip([chars])

```python
print(' 와우!\n'.strip()) # 양쪽 공백 제거
# '와우!'
print(' 와우!\n'.lstrip()) # 왼쪽 공백 제거
# '와우!\n'
print(' 와우!\n'.rstrip()) # 오른쪽 제거
#' 와우!' 
print('안녕하세요????'.rstrip('?’)) 
# 오른쪽 물음표 제거
# '안녕하세요'
```

###### 6번

>.split(sep=None, maxsplit=-1)

```python
print('a,b,c'.split('_’)) 
# _ 을 기준으로 나누는데 _ 가 아닌 ,로 나뉘어져 있음
# ['a,b,c']
print('a b c'.split())
# ['a', 'b', 'c']
                    
test = 'Hello world : 헬로 월드'
print(test)
print(test.split())
print(test.split(sep=':'))
print(test.split(maxsplit=1))
print(test.split(maxsplit=2))
print(test.split(maxsplit=3))

-- 출력값
Hello world : 헬로 월드
['Hello', 'world', ':', '헬로', '월드']	# 기본값으로 분할
['Hello world ', ' 헬로 월드']	# ':'기준 분할
['Hello', 'world : 헬로 월드']	# 공백기준, 1번 분할
['Hello', 'world', ': 헬로 월드']	# 공백기준, 2번 분할
['Hello', 'world', ':', '헬로 월드']	# 공백기준, 3번 분할
```

###### 7번

> 'separator'.join([iterable])

```python
print(''.join(['3', '5’]))
# 35 # ('')공백없이 '3' '5'를 합쳐 출력
```

###### 8번

>기타 문자열 변경 예시

```python
 msg = 'hI! Everyone.' 

print(msg) 
print(msg.capitalize()) 
print(msg.title()) 
print(msg.upper()) 
print(msg.lower()) 
print(msg.swapcase())

# hI! Everyone. 그대로 출력
# Hi! everyone. 맨 첫글자만 대문자로 변환
# Hi! Everyone. 영단어들의 첫 글자를 모두 대문자로
# HI! EVERYONE. 모든 알파벳을 대문자로 변환
# hi! everyone. 모든 알파벳을 소문자로 변환
# Hi! eVERYONE. 소문자 > 대문자, 대문자 > 소문자
```

###### 9번

>.append(x)

```python
cafe = ['starbucks', 'tomntoms', 'hollys’] 
print(cafe)
# ['starbucks', 'tomntoms', 'hollys'] 
cafe.append('banapresso’)
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', 'banapresso']
```

###### 10번

>.extend(iterable)

```python
cafe = ['starbucks', 'tomntoms', 'hollys’]
print(cafe)
# ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['cafe', 'test’])
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', 'cafe', 'test]
```

###### 11번

>.insert(i, x)

```python
cafe = ['starbucks', 'tomntoms’] 
print(cafe)
# ['starbucks', 'tomntoms']
cafe.insert(0, 'start’)
print(cafe)
# ['start', 'starbucks', 'tomntoms']
# index 0의 위치에 'start'를 삽입
            
cafe = ['starbucks', 'tomntoms’] 
print(cafe)
# ['starbucks', 'tomntoms']
cafe.insert(10000, 'start’)
print(cafe)
# ['start', 'starbucks', 'tomntoms']
# 리스트 길이보다 큰 경우 맨 뒤
```

###### 12번

>.remove(x)

```python
numbers = [1, 2, 3, 'hi’] 
print(numbers)
# [1, 2, 3, 'hi'] 
numbers.remove('hi’) 
print(numbers)
# [1, 2, 3]
               
               
# 리스트에 없는 경우 ValueError
numbers.remove('hi')
# ----------------
# ValueError Traceback (most recent call last) # ----> 1 numbers.remove('hi')
# ValueError: list.remove(x): x not in list
```

###### 13번

>.pop(i)

```python
numbers = ['hi', 1, 2, 3] 
# ['hi', 1, 2, 3] 
pop_number = numbers.pop() 
print(pop_number)
#3
print(numbers)
# ['hi', 1, 2]
# i가 지정되지 않으면 마지막 항목을 삭제하고 반환 즉, 3을 반환

numbers = ['hi', 1, 2, 3] 
# ['hi', 1, 2, 3] 
pop_number = numbers.pop(0) 
print(pop_number)
# 'hi'
print(numbers)
# [1, 2, 3]
```

###### 14번

>.clear()

```python
numbers = [1, 2, 3] 
print(numbers)
# [1, 2, 3] print(numbers.clear()) 
# []
```

###### 15번

> .index(x)

```python
numbers = [1, 2, 3, 4] 
print(numbers)
# [1, 2, 3, 4] 
print(numbers.index(3)) 
# 2
# 3을 찾아 그 index값인 2를 반환

print(numbers.index(100)) 
# ---------------------
# ValueError Traceback (most recent call last)
#       2 print(numbers)
# 3 print(numbers.index(3)) 
# ----> 4 print(numbers.index(100))
# ValueError: 100 is not in list
# 없는 경우 ValueError
```

###### 16번

> .count(x)

```python
numbers = [1, 2, 3, 1, 1] 
print(numbers.count(1)) 
#3 
print(numbers.count(100)) 
#0
```

###### 17번

> .sort()

```python
numbers = [3, 2, 5, 1] 
result = numbers.sort() 
print(numbers, result) 
# [1, 2, 3, 5] None - 원본 변경이므로 원본 그 자체를 변경 None 반환

# sorted 함수와 비교
numbers = [3, 2, 5, 1] 
result = sorted(numbers) 
print(numbers, result)
# [3, 2, 5, 1] [1, 2, 3, 5] - 정렬된 리스트를 반환, 원본은 변경 x
```

###### 18번

> .reverse()

``````python
numbers = [3, 2, 5, 1] 
result = numbers.reverse() 
print(numbers, result)
# [1, 5, 2, 3] None - 원본을 그 자체를 변경 None 반환
``````

###### 19번

> .get(key[,default])

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['pineapple']
# ------------------------------
# KeyError Traceback (most recent call last) 
# 1 my_dict = {'apple': '사과', 'banana': '바나나'}
# ----> 2 my_dict['pineapple’]
# KeyError: 'pineapple'

my_dict = {'apple': '사과', 'banana': '바나나'} print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# 사과 
print(my_dict.get('pineapple', 0)) 
#0 - default값 설정 0으로 했으므로 0반환. dict에 없다고 해서 error뜨는 것 X
```

###### 20번

> .pop(key[,default])

```python
my_dict = {'apple': '사과', 'banana': '바나나'} 
data = my_dict.pop('apple')
print(data, my_dict)
# 사과 {'banana': '바나나'}

my_dict = {'apple': '사과', 'banana': '바나나'} 
data = my_dict.pop('pineapple')
print(data, my_dict)
# ----------------
# KeyError Traceback (most recent call last)
# 1 my_dict = {'apple': '사과', 'banana': '바나나'} 
# ----> 2 data = my_dict.pop('pineapple')
# 3 print(data, my_dict)
# KeyError: 'pineapple'
```

###### 21번

> .update([other])

```python
my_dict = {'apple': '사', 'banana': '바나나'} 
my_dict.update(apple='사과')
print(my_dict)
# {‘apple’: ‘사과’, 'banana': '바나나'}
```

###### 22번

> .keys()

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
dict_keys(['name', 'phone', 'birth'])
```

###### 23번

> .values()

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.values()
dict_values(['pey', '0119993323', '1118'])
```

###### 24번

> .items()

``` python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
# 튜플로 묶은 값을 돌려줌
```

<br>

<br>

<br>

### 참고 링크

- <https://wikidocs.net/16>

<br>
