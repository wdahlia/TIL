# Web DAY1

<br>

🔒 **학습 목차**

`Web`

- [Web DAY1](#web-day1)
  - [Web 개요](#web-개요)
      - [💡 웹사이트 구성요소](#-웹사이트-구성요소)
      - [💡 웹 표준](#-웹-표준)
  - [HTML](#html)
      - [💡 HTML](#-html)
      - [💡 요소(element)](#-요소element)
        - [📓 블록/인라인 요소](#-블록인라인-요소)
        - [📓 텍스트 요소](#-텍스트-요소)
        - [📓 그룹 컨텐츠](#-그룹-컨텐츠)
      - [💡 속성(attribute)](#-속성attribute)
      - [💡 기본 구조](#-기본-구조)
        - [📓 `<head>` 예시](#-head-예시)
  - [CSS](#css)
      - [💡 CSS](#-css)
      - [💡 CSS 적용](#-css-적용)
      - [💡 ID / CLASS / Tag](#-id--class--tag)
        - [📓 적용 우선 순위](#-적용-우선-순위)

<br>

[브라우저 동작](https://d2.naver.com/helloworld/59361)

## Web 개요

#### 💡 웹사이트 구성요소

<p align="center"><img width="600" alt="html" src=https://user-images.githubusercontent.com/108653518/187237143-eb02b612-fe61-4a30-a69f-fc57ad180c98.jpeg /></p>

<br>

#### 💡 웹 표준

- 브라우저마다 동작이 달라 문제가 생기는 경우가 많은데, 이것을 해결하기 위해 등장

- **웹에서 표준적으로 사용되는 기술 규칙**
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(`크로스 브라우징`)

<br>

[참고 - HTML/CSS/JS](http://html-css-js.com)

## HTML

#### 💡 HTML

> 웹 페이지를 작성(구조화)하기 위한 언어

<p align = "center"><img width="379" alt="html" src="https://user-images.githubusercontent.com/108653518/187236357-027f4e34-6302-4b79-b883-df77959a41c6.png"></p>

- `Hyper Text` : **참조(하이퍼링크)를 통해** 사용자가 한 문서에서 다른 문서로 **즉시 접근**할 수 있는 텍스트

  - 위키백과 안의 글자에 하이퍼링크 걸려있어 다른 문서로 넘어가는 것 생각하면 됨

- `Markup Language` : 태그 등을 이용하여 **문서나 데이터의 구조를 명시**하는 언어

  - `example` : 

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Hello, HTML</title>
    </head>
    <body>
    </body>
    </html>
    ```

  - *참고* : `<meta charset="utf-8">` 

    - utf-8 문자 집합에는 주류 기록언어에 있는 대부분의 문자가 포함
    - html파일의 인코딩을 알려주는 태그
    - 브라우저에게 text를 어떻게 그려달라는지 말해주는 것
    - 태그가 없다면 한글, 특수문자가 깨져서 나올 수 있음
    - [참고 사이트](https://antstudy.tistory.com/29)

<br>

#### 💡 요소(element)

<p align="center"><img width="279" alt="element" src="https://user-images.githubusercontent.com/108653518/187237751-40763bc5-ff79-4cac-81a7-06fc7eb6c14d.png"></p>

- 요소는 **태그**(`열린(시작)태그/닫는(종료)태그`), **내용**으로 구성
- 정보의 성격, 의미를 정의
- 빈 요소도 존재(내용이 X) - **닫는 태그 X**
  - `br` - 개행 , `hr` - 수평선 , `img` - 이미지, `input` - 입력필드, `link`,  `meta` 
- 요소는 중첩 될 수 있음
  - 여는 태그, 닫는 태그의 쌍 확인 잘해야 함

<br>

##### 📓 블록/인라인 요소

- [참고 블로그](https://memostack.tistory.com/275)

<br>

##### 📓 텍스트 요소

|                  태그                  | 설명                                                         |
| :------------------------------------: | ------------------------------------------------------------ |
|              `<a>` `</a>`              | href 속성을 활용 다른 URL로 연결하는 하이퍼링크 생성<br>- `방문하지 않은 링크` : 밑줄, 파란색<br>- `방문했던 링크` : 밑줄, 보라색<br>- `현재 마우스가 클릭하고 있는 링크` : 밑줄, 빨간색 |
| `<b>` `</b>`<br>`<strong>` `</strong>` | **단순히 굵게 표현되는 텍스트 정의, 텍스트 자체에 주의를 끌기 위함**<br>**강조하고자 하는 중요한 요소** |
|     `<i>` `</i>`<br>`<em>` `</em>`     | *보통 전문용어, 다른 언어의 관용구, 문어체등에 사용*<br>*강조하고자 하는 중요한 요소* |
|                 `<br>`                 | 텍스트 내 줄 바꿈                                            |
|                `<img>`                 | **src 속성**을 활용하여 **이미지 표현**, **alt 속성** 활용 대체 텍스트<br>`alt` : 이미지가 깨졌을 때, 이미지가 무엇을 나타내는지 알려주는 대체 텍스트 |
|           `<span>` `</span>`           | 의미 없는 인라인 컨테이너<br>인라인 요소들을 그룹화 하는데 사용<br>`div` 요소와 매우 비슷하게 사용되나, `div`는 블록 타입 요소 /`span`은 인라인 타입 요소 |

<br>

##### 📓 그룹 컨텐츠

|               태그               | 내용                                                         |
| :------------------------------: | ------------------------------------------------------------ |
|           `<p>` `</p>`           | 문단을 정의                                                  |
|              `<hr>`              | 수평적 가로선을 의미하나 HTML5에서 부터는 주제의 흐름 변경 용도로 사용 |
| `<ol>` `</ol>`<br>`<ul>` `</ul>` | 순서가 있는 리스트<br>순서가 없는 리스트                     |
|         `<pre>` `</pre>`         | 시스템에서 미리 지정된 고정폭 글꼴 사하여 표현<br>텍스트에 사용된 **여백과 줄바꿈**이 모두 그대로 브라우저 화면에 나타남 |
|  `<blockquote>` `</blockquote>`  | 다른 출처로부터 인용된 블록 정의<br>짧은 길이의 인용구 정의 시 `<q>` 사용이 바람직<br>주로 들여쓰기 한 것으로 표현됨 |
|         `<div>` `</div>`         | 의미 없는 블록 레벨 컨테이너<br>CSS로 스타일을 변경, JS로 특정 작업을 수행하기 위한 일종의 컨테이너로 사용, 레이아웃을 설정 |

<br>

#### 💡 속성(attribute)

<p align="center"><img width="617" alt="attribute" src="https://user-images.githubusercontent.com/108653518/187237431-f5f54647-ea70-4356-9636-22bae05e61db.png"></p>

- 속성을 통해 태그의 부가적인 정보를 설정 가능
- 요소는 속성 가질 수 있고, 경로나 크기와 같은 추가적인 정보를 제공

<br>

#### 💡 기본 구조

<p align="center"><img width="344" alt="html1" src="https://user-images.githubusercontent.com/108653518/187237778-7a7fbd02-2f73-47f1-a724-5b9169e96bad.png"></p>

- `<!DOCTYPE html>`
  - 모든 것이 올바르게 동작하기 위하여 포함되어야 할 것 정도로만 생각해도 무방!
- `<html>`
  - 페이지 전체의 컨텐츠를 감싸는 것. 루트(root)요소라고도 함
- `<head>`
  - 문서 **메타데이터** 요소
    - `메타데이터` : 데이터를 위한 데이터 즉, *페이지를 조회하는 사람들에게는 보이지 않는 컨텐츠*
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩등
- `<body>`
  - 실제 화면 구성과 관련된 내용
  - 텍스트, 이미지, 비디오, 게임 어떤 것이든 가능

<br>

##### 📓 `<head>` 예시

<p align="center"><img width="479" alt="html2" src="https://user-images.githubusercontent.com/108653518/187237791-bdf8e32f-61ce-442a-84e0-5a8d6ecef11e.png"></p>

- `<title>`
  - 브라우저 제목 표시줄, 페이지 탭에 보이는 문서 제목을 정의
  - 여는 태그, 닫는 태그 모두 존재
- `<meta>`
  - `name` , `http-equiv`, `charset` 
  - 문서 레벨 메타데이터 요소
  - 빈 요소이므로 여는 태그는 존재 닫는 태그는 존재 X
  - [참고](https://blog.munilive.com/posts/meta-tag-property-and-use-method.html)
- `<link>`
  - **CSS파일, favicon 등**
  - 현재 html과 외부의 .css파일을 연결
  - `href` : 속성 링크된 외부 리소스의 URL 명시
  - `rel` : 현재 문서와 외부 리소스 사이의 연관 관계
    - 사용자에게 더 정확한 결과를 주는데 사용, 검색엔진 최적화(SEO)에 영향 미침
    - [참고](http://www.tcpschool.com/html-tag-attrs/link-rel)
  - 빈 요소이므로 여는 태그는 존재 닫는 태그는 존재 X
- `<script>`
  - **JavaScript 파일/코드**
  - 매 페이지마다 동일한 스크립트 코드를 반복하여 추가하는 것보다 `<script>` 의 `src` 속성을 사용
    - html 파일안에 js코드를 그대로 쓰게 될 경우 정보와 제어가 섞여있어 정보로서의 가치가 떨어짐
    - js코드의 재활용성을 높이고, 정보와 제어를 분리하여 준다는 장점 존재
    - 단, 이때 외부 스크립트 파일의 내용에는 `<script>` 요소 포함되면 안됨
  - `src` :  외부 스크립트 파일의 URL 명시, 문서 내에 스크립트를 직접 삽입하는 것 대신 사용할 수 O
  - 여는 태그, 닫는 태그 모두 존재
- `<style>`
  - 문서나 문서 일부에 대한 스타일 정보를 표시 (여러개 포함 가능)
  - 여는 태그, 닫는 태그 모두 존재

<br>

[참고 - open graph 프로토콜](https://velog.io/@jiseong/open-graph-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C)

## CSS

#### 💡 CSS

> 스타일을 지정하기 위한 언어

<p align="center"><img width="315" alt="css" src="https://user-images.githubusercontent.com/108653518/187237440-10f01726-e131-4d37-91bc-7c5596c8e90a.png"></p>

- HTML만으로 웹 페이지를 제작할 경우, 세부 스타일을 일일히 지정해주어야함
  - 작업에 많은 시간 소요, 완성 후에도 스타일의 변경 및 유지 보수가 어려움
- 웹 페이지의 스타일을 별도의 파일에 저장
  - 스타일을 일관성 있게 유지할 수 있게 도와주며, 유지 보수 또한 쉬움

<br>

<p align="center"><img width="404" alt="css1" src="https://user-images.githubusercontent.com/108653518/187237457-dbaef422-db7f-427d-95fa-62aebd131a8b.png"></p>

- 중괄호 안에서 `속성`과 `값` 하나의 쌍으로 이루어진 선언 진행
- `속성` : 어떤 스타일 기능을 변경할지 결정
- `값` : 어떻게 스타일 기능을 변경할지 결정

<br>

#### 💡 CSS 적용

[참고](http://www.tcpschool.com/css/css_intro_apply)

- `인라인 스타일 (Inline Style) `

  <p align="center"><img width="655" alt="인라인" src="https://user-images.githubusercontent.com/108653518/187243634-5a9bb549-cab9-4cd4-856d-7911772fc4c2.png"></p>

  - HTML 요소 내부에 style 속성을 사용하여 CSS 스타일을 적용
  - 해당 요소에만 스타일을 적용 가능
  - 이 방식은 한 번 설정된 스타일을 변경하기가 매우 어려움 - 시간 많이 소요, 수정하려면 전부 다 고쳐야함

- `내부 참조`

  <p align="center"><img width="655" alt="내부참조" src="https://user-images.githubusercontent.com/108653518/187243641-f9fadd96-9bb6-44a2-8f72-35c1a3bc6aaa.png">
  </p>

  - `<head>` 태그에 `<style>` 태그 사용하여 CSS 스타일을 적용
  - 해당 HTML 문서에만 스타일을 적용 가능

- `외부 참조`

  <p align="center"><img width="651" alt="외부참조" src="https://user-images.githubusercontent.com/108653518/187243755-bfd61011-0221-4683-a7a2-1a544c42a55b.png">
  </p>
  
  <p align="center"><img width="658" alt="외부참조1" src="https://user-images.githubusercontent.com/108653518/187243744-c548a983-6994-4648-a5ff-f6eb2171c44f.png"></p>
  
  - `<head>` 태그에 `<link>` 태그를 사용하여 외부 스타일 시트를 포함해야만 스타일이 적용
  - 웹 사이트 전체의 스타일을 하나의 파일에서 변경 가능 - 수정 용이, 유지 보수 쉬움



#### 💡 ID / CLASS / Tag

[참고](https://heinafantasy.com/155)

- `ID ` : `#` + 아이디 값

  - CSS 적용할 대상으로 특정 요소를 선택할 때 사용

  - 여러 요소 중에서 특정 아이디 이름을 가지는 요소만을 선택해 준다

  - ```html
    <style>
      #heading { color : red; text-decoration: line-through; }
    </style>
    ...
    <h2 id="heading"></h2>
    ```

  - `<h2 id="heading">` 에서 시작해서`</h2>`가 나오기 전까지의 부분에 스타일을 적용

  - 보통 ID는 JS로 개발할 때 활용

  - 문서에서 반드시 한번만 사용, 여러번 사용도 가능하지만 단일 ID 사용 권장

<hr>

- `CLASS` : `.` + 클래스명

  - 특정 집단의 여러 요소를 한 번에 선택할 때 사용

  - ```html
    <style>
      .headings { color: blue; text-decoration: overline; }
    </style>
    ...
    <h2 class="headings"></h2>
    <h3 class="headings"></h3>
    ```

  - `<h2 class="headings">` , `<h3 class="headings">` 에서 시작해서 `</h2>`, `</h3>` 가 나오기 전까지의 부분에 스타일 적용

  - 여러번 사용 가능

  - 일반적으로 CSS 스타일링은 클래스로

<hr>
- `!important` : 속성 : 값 `!important`;
  - 같은 속성을 여러번 정의 했을 때, 나중에 설정한 값이 적용되는데 이를 적용하지 않으려면 속성 값 뒤에 붙여주면 됨
  - 변경하고 싶다면 똑같이 속성에 `!important` 속성을 삽입
  - 큰 프로그램의 경우 어디 CSS에서 꼬였는지 찾기 힘든 경우가 있는데 이 경우 일일히 찾아서 수정하기 쉽지 않으므로 사용하는 경우가 있음

<br>

##### 📓 적용 우선 순위

1. 서로 다른 레벨 : `ID` > `CLASS` > `TAG`

2. 서로 같은 레벨 : 나중에 **선언**된 것이 적용. 즉, 위에서부터 아래로

<br>