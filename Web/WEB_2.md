# Web DAY2

<br>

🔒 **학습 목차**

`Web`

<br>

emmet 이라는 기능 - ultra fast coding 가능

ul>li*5 언리스트 태그안에 리스트를 다섯개 자동 생성해줘~



- `h2#kimbap+ul>li.blue*5` 

```html
<h2 id="kimbap">김밥목록</h2>
<ul>
  <li class="blue">참김</li>
  <li class="blue">돈김</li>
  <li class="blue">치김</li>
  <li class="blue">김밥</li>
  <li class="blue">야김</li>
</ul>
```



픽셀과 퍼센트의 차이

em, rem

vmin



css 원칙

모든 요소는 네모(박스모델)이고

위에서부터 아래로 왼쪽에서 오른쪽으로 쌓인다 - 좌측 상단에 배치



**BOX MODEL**

마진은 컨텐츠요소 아니라서 색깔 못넣음 여백임 - 컨텐츠 요소 밖

보더는 경계선 외곽선을 나타냄 블록의 컨텐츠 크기 

- border 역시 줄여서 작성할 수 있음, 속성값확인 참고 링크걸것

 패딩 - 컨텐츠 안에 들어가는 spacing

- padding top right left bottom (시계방향)



inline은 물건

Inline block은 블럭은 블럭인데 한줄에 정렬될 수 있는 상자

block은 블럭은 블럭인데 한줄에 하나씩



div는 width, height, margin 이런 식의 속성을 주면 표시되지만

- div도 한줄에 여러개를 보고 싶다면 display inline-block 설정
- inline만 넣으면, span과 같이 값을 입력해줘야지만 보이게 됨

span은 값을 `<span>` 이 안에 값을 넣어줘야지만 `</span>` 화면상에서 표시가 됨

- span역시 display를 block으로 설정한다면, 블록형태로 보이게 됨



CSS Display

Display에 따라 크기와 배치가 달라진다

display : block - 마진 요소가 붙어있음을 명심

- 줄 바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭을 차지한다
- 블록레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- 블록 정렬은 margin-center, margin-right, margin-left

align은 블록을 정렬시키지는 못하고 블록 안의 텍스트를 정렬시키는 것은 가능 





display position 

position은 기본적으로 static;

html 순서대로 브라우저상에 자연스럽게 보여지는 것을 말한다

position을 realative;로 하면 left top bottom right 내가 설정한 값으로 옮겨져감 - 상대적

absolute; 내 아이템과 가장 가까이에 있는 박스안에서 그니까 상위박스에서 부터 내가 지정한 top right left bottom 값으로 옮겨가는것

fixed; 상자안에서 완전히 벗어나서 웹페이지에서 움직이는 것

sticky; 원래있는 그자리에는 있는데 스크롤링되는동안 원래 그자리에 있는것!

- 약간, 그 웹페이지에 있는 고객센터 채팅 보낼수있는 창? 스크롤링해도 밑으로 내려오는 애들 같은건가..?



























