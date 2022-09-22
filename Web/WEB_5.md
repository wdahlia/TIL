# HTML

HTML 문서 구조화

table의 각 영역을 명시하기 위함 <thead> <tbody> <tfoot> 필수 요소는 아니다

<tr>로 가로 줄 구성 후 header부분의 요소는 th 나머지는 td



form 정보(데이터)를 서버에 제출하기 위해 사용하는 태그



Form 기본 속성

action : form을 처리할 서버의 URL(데이터를 보낼 곳)



input label



value(값) name(이름)으로 매핑되어 서버에 전송 



layout- utilities



## Bootstrap v.5.2

### Breakpoints

반응형 레이아웃이 뷰포트 크기 또는 기기에서 어떻게 작동 할지 결정하는 사용자가 정의 가능한 넓이

- 레이아웃을 특정 뷰포트 크기 또는 기기에서 조정 제어
- 일반적으로는 min-width를 사용
- 모바일 우선, 반응형 디자인이 목표
- 가장 작은 breakpoint에서 레이아웃이 작동하도록 설정한 후 스타일에 계층을 적용하고 더 큰 기기에 해당 디자인이 맞게 조정되는 것이 목표이다

| Breakpoint        | Class infix | Dimensions  |
| ----------------- | ----------- | ----------- |
| X-Small           | None        | 576px 미만  |
| Small             | **sm**      | 576px 이상  |
| Medium            | **md**      | 768px 이상  |
| Large             | **lg**      | 992px 이상  |
| Extra large       | **xl**      | 1200px 이상 |
| Extra extra large | **xxl**     | 1400px 이상 |



### Reboot

#### 💡header and paragraphs

- `<h1>`, `<p>`는 **margin-top**이 제거 되게 재설정
- `<h$>`은 **margin-bottom**이 0.5rem(8px)
- `<p>`단락은 **margin-bottom**이 1rem(16px)

#### 💡 hr

- `<hr>` 은 border-top을 통해 스타일링 된 것
- 디폴트 값이 `opacity : .25`
- `<hr>` 색상의 경우에는 부모의 color 값을 상속받으며, 테마 색상에 구축 된 유틸리티 사용하여 테두리 색상을 변경
  - 참고 : [border-color](#color)






## Utilities

### Border

#### 💡 border를 추가

<img src="../../../WEB_5.assets/additive.png" alt="additive" style="zoom:50%;" />

<br>

#### 💡 order를 제거

<img src="../../../WEB_5.assets/subtractive.png" alt="subtractive" style="zoom:50%;" />

<br>

#### 💡 Color

<img src="../../../WEB_5.assets/builtoncolors.png" alt="builtoncolors" style="zoom:50%;" />

- 부트스트랩에 내장되어 있는 border color

<br>

#### 💡 Opacity 투명도

- `border-opacity-원하는 %` 를 쓰면 된다

  <img src="../../../WEB_5.assets/opacity.png" alt="opacity" style="zoom:50%;" />

<br>

#### 💡 Width



 

