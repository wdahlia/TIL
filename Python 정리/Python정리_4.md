# **π** Python μ λ¦¬ - (4)

[μ°Έκ³  λ§ν¬](#μ°Έκ³ -λ§ν¬)

## λ°μ΄ν° κ΅¬μ‘°

- `νμ. + λ©μλ()`

```
- νμ = λκ°

- () = input 

- νμ.λ©μλ() = output
```

<br>

### μνμ€ - μμκ° μλ λ°μ΄ν° κ΅¬μ‘°

#### π λ¬Έμμ΄

- λ¬Έμλ€μ λμ΄
  - λͺ¨λ  λ¬Έμλ str νμ

| μμ νμΈνλ €λ©΄ ν΄λ¦­βοΈ                  |                                                              |
| :------------------------------------- | ------------------------------------------------------------ |
| **`λ¬Έμμ΄ νμ`**                      |                                                              |
| [.find(x)](#1λ²)                       | xμ μ²« λ²μ§Έ μμΉλ₯Ό λ°ν. μμΌλ©΄, -1μ λ°ν                   |
| [.index(x)](#2λ²)                      | xμ μ²« λ²μ§Έ μμΉλ₯Ό λ°ν. μμΌλ©΄, μ€λ₯ λ°μ                   |
| [.isdecimal()](#3λ²)                   | λ¬Έμμ΄ κ΄λ ¨ κ²μ¦ - μ£Όμ΄μ§ λ¬Έμμ΄μ΄ intλ‘ λ°ν κ°λ₯νκ° μ¬λΆ κ²μ¬ |
| **`λ¬Έμμ΄ λ³κ²½`**                      | λ¬Έμμ΄λ μ€μ€λ‘ λ°λλ κ²½μ° X (immutable ) , λͺ¨λ λ°λ κ²°κ³Όλ₯Ό λ°ννλ€ |
| [.replace(old, new[,count])](#4λ²)     | ππ» λ°κΏ λμ κΈμλ₯Ό μλ‘μ΄ κΈμλ‘ λ°κΏμ λ°ν<br>ππ» countλ₯Ό μ§μ νλ©΄, ν΄λΉ κ°μλ§νΌλ§ μν |
| [.strip([chars])](#5λ²)                | ππ» νΉμ ν λ¬Έμλ₯Ό μ§μ νλ©΄,<br>ππ» μμͺ½μ μ κ±°νκ±°λ(strip), μΌμͺ½μ μ κ±°νκ±°λ(lstrip), μ€λ₯Έμͺ½μ μ κ±°(strip)<br>ππ» λ¬Έμμ΄μ μ§μ νμ§ μμΌλ©΄ **κ³΅λ°±(space, '\n')μ μ κ±°ν¨** βΆοΈ μ μΌ λ§μ΄ μ¬μ© |
| [.split(sep=None, maxsplit=-1))](#6λ²) | ππ» λ¬Έμμ΄μ νΉμ ν λ¨μλ‘ λλ  λ¦¬μ€νΈλ‘ λ°ν                 |
| ['seperator'.join([iterable])](#7λ²)   | ππ» λ°λ³΅κ°λ₯ν μ»¨νμ΄λ μμλ€μ seperator(κ΅¬λΆμ)λ‘ ν©μ³ λ¬Έμμ΄ λ°ν<br>ππ» () μμ λ¬Έμμ΄μ΄ μλ κ°μ΄ μμΌλ©΄ TypeError λ°μ |
| [κΈ°ν λ¬Έμμ΄ λ³κ²½ μμ](#8λ²)          |                                                              |

<br>

#### π λ¦¬μ€νΈ

- λ³κ²½ κ°λ₯ν(mutable) κ°λ€μ λμ΄λ μλ£ν, λ°λ³΅ κ°λ₯ν¨(iterable)

  ``` python
  # λ¦¬μ€νΈλ mutable(λ³κ²½ κ°λ₯ν κ°)
  a = [1,2,3]
  a[0] = 100
  print(a)
  # [100, 2, 3]
  
  # λ¬Έμμ΄μ immutable
  a = 'hi'
  a[0] = 'c'
  print(a)
  # Traceback (most recent call last):
  #   File "C:\Users\hphk\Desktop\TIL\python\4μΌμ°¨\04_mutable.py", line 8, in <module>
  # 		a[0] = 'c'
  # TypeError: 'str' object does not support item assignment
  ```

- μμλ₯Ό κ°μ§λ©°, μλ‘ λ€λ₯Έ νμμ μμλ₯Ό κ°μ§ μ μμ

<br>

| μμ νμΈνλ €λ©΄ ν΄λ¦­βοΈ      |                                                              |
| :------------------------- | ------------------------------------------------------------ |
| π©π»βπ» **`κ° μΆκ° λ° μ­μ `**  |                                                              |
| [.append(x)](#9λ²)         | λ¦¬μ€νΈ λ§μ§λ§μ ν­λͺ© xλ₯Ό μΆκ°                                |
| [.expend(iterable)](#10λ²) | ππ» ()μμ ν­λͺ©μ μΆκ°<br>ππ» μ¬λ¬κ° μΆκ°νλ €λ©΄ κΌ­ λ¦¬μ€νΈλ‘ λ¬Άμ΄μ λ£μ΄μ€μΌν¨<br>ππ» λ¬Έμμ΄ 'banana'λ§ λ£κ²λλ©΄ 'b', 'a', 'n', 'a', 'n', 'a' μ΄λ κ² μΆκ°λ¨ |
| [.insert(i, x)](#11λ²)     | μ ν΄μ§ μμΉ iμ κ°μ μΆκ°ν¨. λ¦¬μ€νΈ μΈλ±μ€ iμ ν­λͺ© xλ₯Ό μ½μ |
| [.remove(x)](#12λ²)        | ππ» λ¦¬μ€νΈμμ κ°μ΄ xμΈ κ² μ­μ <br>ππ» μ΄λ―Έ λ¦¬μ€νΈμ μλλ° μ€ννλ€λ©΄ ValueError λΈ |
| [.pop(i)](#13λ²)           | ππ» μ ν΄μ§ μμΉ iμ μλ κ°μ μ­μ , κ·Έ ν­λͺ©μ λ°ν<br>ππ» iκ° μ§μ λμ§ μμΌλ©΄, λ§μ§λ§ ν­λͺ©μ μ­μ νκ³  λ°νν¨ |
| [.clear()](#14λ²)          | λͺ¨λ  ν­λͺ©μ μ­μ                                              |
| π©π»βπ» **`νμ λ° μ λ ¬`**     |                                                              |
| [.index(x)](#15λ²)         | xκ°μ μ°Ύμ ν΄λΉ index κ°μ λ°ν                              |
| [.count(x)](#16λ²)         | μνλ κ°μ κ°μλ₯Ό λ°νν¨                                    |
| [.sort()](#17λ²)           | ππ» μλ³Έ λ¦¬μ€νΈλ₯Ό μ λ ¬ν¨. None λ°ν<br>ππ» sorted ν¨μμ λΉκ΅ν  κ² |
| [.reverse()](#18λ²)        | μμλ₯Ό λ°λλ‘ λ€μ§μ(μ λ ¬νλ κ²μ΄ μλ). None λ°ν          |

<br>

### μ»¬λ μ - μμκ° μλ λ°μ΄ν° κ΅¬μ‘°

#### π μΈνΈ

- μ μΌν κ°λ€μ λͺ¨μ(collection)
- μμκ° μκ³  μ€λ³΅λ κ°μ΄ μμ
  - μνμμμ μ§ν©κ³Ό λμΌν κ΅¬μ‘°, μ§ν© μ°μ°λ κ°λ₯
- λ³κ²½ κ°λ₯, λ°λ³΅ κ°λ₯
  - λ¨, μΈνΈλ μμκ° μμ΄ λ°λ³΅μ κ²°κ³Όκ° μ μν μμμ λ€λ₯Ό μ μμ

| μμ νμΈνλ €λ©΄ ν΄λ¦­βοΈ |                                                              |
| :-------------------- | ------------------------------------------------------------ |
| .copy()               | μΈνΈμ μμ λ³΅μ¬λ³Έμ λ°ν                                    |
| .add(x)               | ν­λͺ© xκ° μΈνΈ sμ μλ€λ©΄ μΆκ°                                |
| .pop()                | μΈνΈ λ©μλ                                                  |
| .remove(s)            | ππ» μΈνΈsμμ λλ€νκ² ν­λͺ©μ λ°ννκ³ <br>ππ» ν΄λΉ ν­λͺ©μ μ κ±° μΈνΈκ° λΉμ΄ μμ κ²½μ°, KeyError |
| .discard(x)           | ππ» ν­λͺ© xλ₯Ό μΈνΈ sμμ μ­μ <br>ππ» ν­λͺ©μ΄ μ‘΄μ¬νμ§ μμ κ²½μ°, KeyError |
| .update(t)            | ν­λͺ© xκ° μΈνΈ sμ μλ κ²½μ°, ν­λͺ© xλ₯Ό μΈνΈsμμ μ­μ          |
| .clear()              | μΈνΈ tμ μλ λͺ¨λ  ν­λͺ© μ€ μΈνΈ sμ μλ ν­λͺ©μ μΆκ°         |
| .isdisjoint(t)        | λͺ¨λ  ν­λͺ©μ μ κ±°                                             |
| .issubset(t)          | μΈνΈ sκ° μΈνΈ tμ μλ‘ κ°μ ν­λͺ©μ νλλΌλ κ°κ³  μμ§ μμ κ²½μ°, Trueλ°ν |
| .issuperset(t)        | μΈνΈ sκ° μΈνΈ tμ νμ μΈνΈμΈ κ²½μ°, Trueλ°ν                 |

<br>

#### π λμλλ¦¬

- Key - Value μμΌλ‘ μ΄λ£¨μ΄μ§ λͺ¨μ
  - key 
    - λΆλ³ μλ£νλ§ κ°λ₯ (λ¦¬μ€νΈ, λμλλ¦¬ λΆκ°)
  - values
    - μ΄λ ν ννλ  κ°λ₯
- λ³κ²½ κ°λ₯, λ°λ³΅ κ°λ₯
  - λμλλ¦¬λ λ°λ³΅νλ©΄ ν€κ° λ°ν

| μμ νμΈνλ €λ©΄ ν΄λ¦­βοΈ        |                                                              |
| :--------------------------- | ------------------------------------------------------------ |
| **`μ‘°ν`**                   |                                                              |
| [.get(key[,default])](#19λ²) | ππ» keyλ₯Ό ν΅ν΄ valueλ₯Ό κ°μ Έμ΄<br>ππ» KeyErrorκ° λ°μνμ§ μμΌλ©°, default κ°μ μ€μ ν  μ μμ(κΈ°λ³Έ : None) |
| **`μΆκ° λ° μ­μ `**           |                                                              |
| [.pop(key[,default])](#20λ²) | ππ» keyκ° λμλλ¦¬μ μμΌλ©΄ μ κ±°νκ³  ν΄λΉ κ°μ λ°ν<br>ππ» κ·Έλ μ§ μμΌλ©΄ defaultλ₯Ό λ°ν, defaultκ°μ΄ μμΌλ©΄ KeyError |
| [.update([other])](#21λ²)    | κ°μ μ κ³΅νλ key, valueλ‘ λ?μ΄μμλλ€.                     |
| [.keys()](#22λ²)             | λμλλ¦¬ dμ λͺ¨λ  ν€λ₯Ό λ΄μ λ·°λ₯Ό λ°ν                        |
| [.values()](#23λ²)           | λμλλ¦¬ dμ λͺ¨λ  κ°μ λ΄μ λ·°λ₯Ό λ°ν                        |
| [.items()](#24λ²)            | λμλλ¦¬ dμ λͺ¨λ  ν€-κ°μ μμ λ΄μ λ·°λ₯Ό λ°ν                |

<br>

<br>

<br>

<br>

<br>

## μμ

###### 1λ²

> .find(x)

```python
 print('apple'.find('p')) 
 #1 
 print('apple'.find('k')) 
 # -1
```

###### 2λ²

>.index(x)

```python
print('apple'.index('pβ))              
#1
                   
'apple'.index('k')
# ------------------------------------------- 
# ValueError Traceback (most recent call last) 
# ----> 1 'apple'.index('k')
# ValueError: substring not found
```

###### 3λ²

>.isdecimal()

``` python
a = '3Β²'
print(a.isdecimal())
# False
```

###### 4λ²

>.replace(old, new[,count])

```python
 print('coone'.replace('o', 'aβ))
# caane oμ μλ¦¬μ aλ₯Ό λ£λλ€
print('wooooowoo'.replace('o', '!', 2)) 
# w!!ooowoo
# count 2 μ§μ  μ¦ λκ° λ³κ²½ !!
```

###### 5λ²

>.strip([chars])

```python
print(' μμ°!\n'.strip()) # μμͺ½ κ³΅λ°± μ κ±°
# 'μμ°!'
print(' μμ°!\n'.lstrip()) # μΌμͺ½ κ³΅λ°± μ κ±°
# 'μμ°!\n'
print(' μμ°!\n'.rstrip()) # μ€λ₯Έμͺ½ μ κ±°
#' μμ°!' 
print('μλνμΈμ????'.rstrip('?β)) 
# μ€λ₯Έμͺ½ λ¬Όμν μ κ±°
# 'μλνμΈμ'
```

###### 6λ²

>.split(sep=None, maxsplit=-1)

```python
print('a,b,c'.split('_β)) 
# _ μ κΈ°μ€μΌλ‘ λλλλ° _ κ° μλ ,λ‘ λλμ΄μ Έ μμ
# ['a,b,c']
print('a b c'.split())
# ['a', 'b', 'c']
                    
test = 'Hello world : ν¬λ‘ μλ'
print(test)
print(test.split())
print(test.split(sep=':'))
print(test.split(maxsplit=1))
print(test.split(maxsplit=2))
print(test.split(maxsplit=3))

-- μΆλ ₯κ°
Hello world : ν¬λ‘ μλ
['Hello', 'world', ':', 'ν¬λ‘', 'μλ']	# κΈ°λ³Έκ°μΌλ‘ λΆν 
['Hello world ', ' ν¬λ‘ μλ']	# ':'κΈ°μ€ λΆν 
['Hello', 'world : ν¬λ‘ μλ']	# κ³΅λ°±κΈ°μ€, 1λ² λΆν 
['Hello', 'world', ': ν¬λ‘ μλ']	# κ³΅λ°±κΈ°μ€, 2λ² λΆν 
['Hello', 'world', ':', 'ν¬λ‘ μλ']	# κ³΅λ°±κΈ°μ€, 3λ² λΆν 
```

###### 7λ²

> 'separator'.join([iterable])

```python
print(''.join(['3', '5β]))
# 35 # ('')κ³΅λ°±μμ΄ '3' '5'λ₯Ό ν©μ³ μΆλ ₯
```

###### 8λ²

>κΈ°ν λ¬Έμμ΄ λ³κ²½ μμ

```python
 msg = 'hI! Everyone.' 

print(msg) 
print(msg.capitalize()) 
print(msg.title()) 
print(msg.upper()) 
print(msg.lower()) 
print(msg.swapcase())

# hI! Everyone. κ·Έλλ‘ μΆλ ₯
# Hi! everyone. λ§¨ μ²«κΈμλ§ λλ¬Έμλ‘ λ³ν
# Hi! Everyone. μλ¨μ΄λ€μ μ²« κΈμλ₯Ό λͺ¨λ λλ¬Έμλ‘
# HI! EVERYONE. λͺ¨λ  μνλ²³μ λλ¬Έμλ‘ λ³ν
# hi! everyone. λͺ¨λ  μνλ²³μ μλ¬Έμλ‘ λ³ν
# Hi! eVERYONE. μλ¬Έμ > λλ¬Έμ, λλ¬Έμ > μλ¬Έμ
```

###### 9λ²

>.append(x)

```python
cafe = ['starbucks', 'tomntoms', 'hollysβ] 
print(cafe)
# ['starbucks', 'tomntoms', 'hollys'] 
cafe.append('banapressoβ)
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', 'banapresso']
```

###### 10λ²

>.extend(iterable)

```python
cafe = ['starbucks', 'tomntoms', 'hollysβ]
print(cafe)
# ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['cafe', 'testβ])
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', 'cafe', 'test]
```

###### 11λ²

>.insert(i, x)

```python
cafe = ['starbucks', 'tomntomsβ] 
print(cafe)
# ['starbucks', 'tomntoms']
cafe.insert(0, 'startβ)
print(cafe)
# ['start', 'starbucks', 'tomntoms']
# index 0μ μμΉμ 'start'λ₯Ό μ½μ
            
cafe = ['starbucks', 'tomntomsβ] 
print(cafe)
# ['starbucks', 'tomntoms']
cafe.insert(10000, 'startβ)
print(cafe)
# ['start', 'starbucks', 'tomntoms']
# λ¦¬μ€νΈ κΈΈμ΄λ³΄λ€ ν° κ²½μ° λ§¨ λ€
```

###### 12λ²

>.remove(x)

```python
numbers = [1, 2, 3, 'hiβ] 
print(numbers)
# [1, 2, 3, 'hi'] 
numbers.remove('hiβ) 
print(numbers)
# [1, 2, 3]
               
               
# λ¦¬μ€νΈμ μλ κ²½μ° ValueError
numbers.remove('hi')
# ----------------
# ValueError Traceback (most recent call last) # ----> 1 numbers.remove('hi')
# ValueError: list.remove(x): x not in list
```

###### 13λ²

>.pop(i)

```python
numbers = ['hi', 1, 2, 3] 
# ['hi', 1, 2, 3] 
pop_number = numbers.pop() 
print(pop_number)
#3
print(numbers)
# ['hi', 1, 2]
# iκ° μ§μ λμ§ μμΌλ©΄ λ§μ§λ§ ν­λͺ©μ μ­μ νκ³  λ°ν μ¦, 3μ λ°ν

numbers = ['hi', 1, 2, 3] 
# ['hi', 1, 2, 3] 
pop_number = numbers.pop(0) 
print(pop_number)
# 'hi'
print(numbers)
# [1, 2, 3]
```

###### 14λ²

>.clear()

```python
numbers = [1, 2, 3] 
print(numbers)
# [1, 2, 3] print(numbers.clear()) 
# []
```

###### 15λ²

> .index(x)

```python
numbers = [1, 2, 3, 4] 
print(numbers)
# [1, 2, 3, 4] 
print(numbers.index(3)) 
# 2
# 3μ μ°Ύμ κ·Έ indexκ°μΈ 2λ₯Ό λ°ν

print(numbers.index(100)) 
# ---------------------
# ValueError Traceback (most recent call last)
#       2 print(numbers)
# 3 print(numbers.index(3)) 
# ----> 4 print(numbers.index(100))
# ValueError: 100 is not in list
# μλ κ²½μ° ValueError
```

###### 16λ²

> .count(x)

```python
numbers = [1, 2, 3, 1, 1] 
print(numbers.count(1)) 
#3 
print(numbers.count(100)) 
#0
```

###### 17λ²

> .sort()

```python
numbers = [3, 2, 5, 1] 
result = numbers.sort() 
print(numbers, result) 
# [1, 2, 3, 5] None - μλ³Έ λ³κ²½μ΄λ―λ‘ μλ³Έ κ·Έ μμ²΄λ₯Ό λ³κ²½ None λ°ν

# sorted ν¨μμ λΉκ΅
numbers = [3, 2, 5, 1] 
result = sorted(numbers) 
print(numbers, result)
# [3, 2, 5, 1] [1, 2, 3, 5] - μ λ ¬λ λ¦¬μ€νΈλ₯Ό λ°ν, μλ³Έμ λ³κ²½ x
```

###### 18λ²

> .reverse()

``````python
numbers = [3, 2, 5, 1] 
result = numbers.reverse() 
print(numbers, result)
# [1, 5, 2, 3] None - μλ³Έμ κ·Έ μμ²΄λ₯Ό λ³κ²½ None λ°ν
``````

###### 19λ²

> .get(key[,default])

```python
my_dict = {'apple': 'μ¬κ³Ό', 'banana': 'λ°λλ'}
my_dict['pineapple']
# ------------------------------
# KeyError Traceback (most recent call last) 
# 1 my_dict = {'apple': 'μ¬κ³Ό', 'banana': 'λ°λλ'}
# ----> 2 my_dict['pineappleβ]
# KeyError: 'pineapple'

my_dict = {'apple': 'μ¬κ³Ό', 'banana': 'λ°λλ'} print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# μ¬κ³Ό 
print(my_dict.get('pineapple', 0)) 
#0 - defaultκ° μ€μ  0μΌλ‘ νμΌλ―λ‘ 0λ°ν. dictμ μλ€κ³  ν΄μ errorλ¨λ κ² X
```

###### 20λ²

> .pop(key[,default])

```python
my_dict = {'apple': 'μ¬κ³Ό', 'banana': 'λ°λλ'} 
data = my_dict.pop('apple')
print(data, my_dict)
# μ¬κ³Ό {'banana': 'λ°λλ'}

my_dict = {'apple': 'μ¬κ³Ό', 'banana': 'λ°λλ'} 
data = my_dict.pop('pineapple')
print(data, my_dict)
# ----------------
# KeyError Traceback (most recent call last)
# 1 my_dict = {'apple': 'μ¬κ³Ό', 'banana': 'λ°λλ'} 
# ----> 2 data = my_dict.pop('pineapple')
# 3 print(data, my_dict)
# KeyError: 'pineapple'
```

###### 21λ²

> .update([other])

```python
my_dict = {'apple': 'μ¬', 'banana': 'λ°λλ'} 
my_dict.update(apple='μ¬κ³Ό')
print(my_dict)
# {βappleβ: βμ¬κ³Όβ, 'banana': 'λ°λλ'}
```

###### 22λ²

> .keys()

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
dict_keys(['name', 'phone', 'birth'])
```

###### 23λ²

> .values()

```python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.values()
dict_values(['pey', '0119993323', '1118'])
```

###### 24λ²

> .items()

``` python
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
# ννλ‘ λ¬Άμ κ°μ λλ €μ€
```

<br>

<br>

<br>

### μ°Έκ³  λ§ν¬

- <https://wikidocs.net/16>

<br>
