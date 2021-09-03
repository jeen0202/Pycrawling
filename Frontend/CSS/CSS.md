# CSS 기본 정리
## CSS란?
:Cascading Style Sheets

현재는 2005년에 정의된 CSS3 사용<br>
HTML로 구조화된 문서의 렌더링 표현 방법을 정의하기 위한 언어<br>

## CSS Sclector
* HTML 문서의 특정 부분에 대해 렌더링 방법을 정의하기 위해 특정 부분의 선택이 필요
* 이를위해 CSS Selector를 사용
* CSS Selector로 특정 부분을 정의한 구문을 Rule Set이라고 부르며 Rule Set의 집합을 Style Sheet라고 부른다.

* Property(속성)과 각 Property별 설정 가능한 Value(값)은 미리 정의되어있다.
> CSS는 속성-값의 형태이지만, 모던 웹을 위해서는 다양하고 깊은 CSS 문법을 이해하고 있어야 한다.<br>

## HTML과 CSS의 연동
1. 적용할 태그의 style 속성에 사용
2. Haead안에 style 태그로 적용
3. link를 사용하여 CSS 파일 적용

## Reset CSS
웹 브라우저마다 다른 default 스타일이 지정되어 있으므로 이를 초기화하야 다양한 웹브라우저에서도 동일한 스타일로 표시하도록 하는 설정<br>
> 공식 권장사항은 아니지만, 실무에서 필요에 의해 임의로 만든 설정
* 스타일을 초기화하는 다양한 기법이 있지만, 최근에는 normalize.css를 주로 사용
    + cdn을 통해 링크할수있음
    + default 스타일은 남기고, 브라우저별로 다를 수 있는 스타일만 초기화

```html
<link rel = 'stylesheet' 
href='https://cdnjs.cluudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css>
```


##  CSS 크기 단위
1. px : 픽셀 단위, 해상도에 따라 상대적인 크기
2. % : 백분율 단위의 상대 단위, 상대적인 비율의 크기
3. em : 배수 단위, 지정 사이즈를 기반으로 배수된 크기
    + 중첩된 자식 요소에 em을 지정하면 모든 자식 요소 사이즈에 영향을 줄 수 있음
4. rem : root em, 최상위 요소(html) 사이즈가 기준

## 반응형 Viewport 단위
* 반응형 지원을 위해 자동으로 크기가 변하도록 하는 기능

### Viewport 단위
1. vw : viewport 너비 1/100 (1%)
2. vh : viewport 높이 1/100 (1%)
3. vmin : 너비 또는 높이 중 작은 쪽 (1%)
4. vman: 너비 또는 높이 중 큰 쪽 (1%)
> 최대값이 100인 비율의 형태

## 색상 표현 단위

1. 색상 이름으로 표기 (red)
2. 16진수 표기 (#ffffff, 2자리마다 RGB의 정도 표현) 
3. RGB 표기  rgb(138,43,226)
4. RGBA(Red,Green,BLue,Alpha(투명도)) : rgba(138,43,226,0.5)
5. HSL,HSLA(Hue/색상,Saturation/채도,Lightness/명도,Alpha/투명도)

### 참고 : RGBA와 opacity의 차이점
+ opacity : 투명도 설정, 0.0이 투명, 1.0이 불투명
+ opacity 값은 모든 자식 요소에 투명도 값 상속
+ RGBA는 상속되지 않음

# CSS Selector
* HTML 문서의 특정 부분을 선택하기 위한 문법

(구) reset.css
* 최근에는 사용되지 않음
```html
<style>
    * {
        margin : 0;
        padding : 0;
        border : none;
    }
</style>
```

## 태그 Selector
```html
<style>
    h1 { color : red;}
</style>
```

## ID Selector
#아이디명으로 지정
```html
<style>
    #dave {color : blue;}
</style>
```
## class Selector
.클래스명으로 지정
```html
<style>
    .dave {color : yellow;}
</style>
```

## attribute(속성) selector
* [속성] : attr 속성을 가지는 모든 태그(요쇼)
* [속성=값] : 속성값이 일치하는 태그
* [속성~=값] : 속성값이 value를 단어로 포함하는 모든 태그(요소)
* [속성 |=값] : 속성값이 일치하거나 값으로 시작하면서 문자가 곧바로 따라오는 태그
* [속성 ^=값] : 태그의 속성값이 값으로 시작하는 모든 태그
* [속성 $=값] : 태그의 요소중 속성값이 값으로 끝나느 모든 태그
* [속성 *=값] : 태그의 속성값이 값을 포함하는 모든 태그
```html
<style> [attr] {color : red;}</style>
```

## 다양한 CSS Selector 조합
* 태그,id,class selector를 조합해서 복합적으로 사용 가능
* HTML 문서 특정 태그에 여러 클래스가 지정될 경우, 스페이스를 이용해서 여러 클래스 설정 가능
    + class = '클래스명1 클래스명2 클래스명3'
    + 이 경우 css selector는 .클래스명1.클래스명2.클래스명3과 같이 사용 가능
```html
<style>
    h1.dave.funcoding#lee {color:gray;}
</style>
</head>
<body>
    <h1 class='dave funcoding' id='lee'>Hello World</h1>
</body>
```
## 복합 selector (Combinator)

* 태그 안에 또다른 태그를 넣을 수 있으므로, 요소간에 부모/자식의 관계가 매겨짐
* 관계를 기반으로 HTML 문서 특정 부분을 선택 할 수 있는 문법
```html
<div>
    <h1>Sejing</h1>
    <p> 잔잔바리 코딩을 운영하고 있습니다. </p>
    <p><span>좋은 서비스를</span> 만드는일에 집중하고 있습니다.</p>
```
* 후손 셀렉터 : ``` ```로 표시
    + 부모 태그안에 있는 모든 하위 태그를 하위 요소라고 부름
    + 부모 태그(selector1)안에 있는 모든 태그중에 selctor2를 선택
    ```selector1 selector2```
* 자식 셀렉터 : ```>```로 표시
    + 부모 태그 안에 있는 바로 다음 레벨의 태그중에 selector2 선택
    ```selector1>selector2```
* 인접 형제 셀렉터 : ```+```로 표시
    + 태그와 동일한 레벨에 위치하고 바로 뒤에 위치한 selector를 선택
    ```selector+selector2```
* 일반 형제 셀럭터 : ```~```로 표시
    + 태그와 동일 레벨에 위치하고, selector1 뒤에 위치하는 selector를 선택
    ```selector1~selector2```

## 가상 클래스 셀렉터
* 요소에 특정 이벤트 발생시를 선택하는 문법
### 가상 클래스의 종류
* link : 방문하지 않은 링크가 적용된 요소
* visited : 한번이라도 방문한 링크가 적용된 요소
* hover : 특성 요소에 커서가 올라간 상태
* active : 링크 요소를 클릭한 상태
* focus : 특정 요소에 포커스가 있는 상태

## UI 요소 상태 셀렉터
: 특정 UI 요소 상태에 따른 셀렉터

* enabled : UI 셀렉터가 사용 가능
* disabled : UI 셀렉터가 사용 불가능
* checked : UI 셀렉터가 체크된 상태
* indeterminate : UI 셀렉터 상태가 결정되지 않은 상태

## 구조 가상 클래스 셀렉터

* first-child : 첫번쨰 자식인 요소 선택
* last-child : 마지막 자식 요소 선택
* nth-child : n 번째 자식 요소 선택
* nth-last-child : 마지막 자식 요소에서 n번째 자식요소 선택

* first-of-type : 셀렉터에 해당하는 요소의 부모 요소의 자식중 셀렉터중 첫번째 요소를 선택
* last-of-type : 셀렉터에 해당하는 요소의 부모 요소의 자식중 셀렉터중 마지막 요소를 선택

## 부정 셀렉터
* not(셀렉터) - 셀렉터에 해당하지 않은 모든 요소 선택

## 정합성 체크 셀렉터 
* valid(셀렉터) : 정합성이 검증된 input 또는 form 요소 선택
* invalid(셀렉터) : 정합성 검증이 실패한 input 또는 form 요소 선택

## input 태그 유효성 검사와 정합성 체크 셀렉터
>> 정합성 체크 셀렉터 이해와 활용을 위해, input 태그의 유효성 검사 관련 속성을 이해 해야한다.<br>
다양한 속성이 있지만, 크로스 브라우저를 위해, 호환성이 떨어지는 속성은 사용하지 않는 편이 좋기에, 호환성이 높은 속성만 정리

### required 속성
* input 태그로 생성된 입력창에 데이터를 무조건 넣어야 한다.()

### pattern 속성
* input 태그로 생성된 입력창에 넣은 데이터가 원하는 데이터 포맷에 맞으면 검증완료
* pattern 값은 정규표현식 

### 가상 요소 셀렉터
* 선택한 요소 안의 특정 부분을 선택
* first-letter : 요소의 첫 글자
* first-line : 요소의 첫 라인 선택
* atfer : 요소의 뒤에 위치하는 공간, content property와 함께 사용
* before : 요소의 앞에 위치하는 공간, content property와 함께 사용
* selection : 요소에서 드래그한 부분을 선택
> 가상요소 셀렉터는 ```::``` 을 사용한다.

# CSS BOX MODEL
block 또는 inline-block 특성을 가지는 요소 => Box 형태, 세부 사장을 수정할 수 있다.

## BOX MODEL PROPERTY

* content : 요소의 실제 내용이 위치하는 영역 (width,height)
* padding : border 안쪽의 내부 여백 여역, 패딩영역의 두께를 의미
* border : 테두리 영역, 속성값으로 두께 지정
* margin : border 바깥의 외부 여백 영역, 배경색 지정 불가

### 주요 속성

1. width/height
+ box-sizing : default값이 content-box,
    + width/height는 content  영역의 너비와 높이
+ box-sizing 속성이 border-box로 지정되어 있으면, content+ padding+ border영역의 너비와 높이가 된다.
+ width/height 포함, 모든 box model 속성은 상속되지 않는다.

> content 영역밖으로 컨텐츠가 넘치는 경우, overflow 속성을 hidden으로 설정하면, 이를 감출 수 있다.

#### 참고:max-width/max-height 속성
 요소 너비가 브라우저 너비보다 클 경우, 스크롤바가 만들어 질 수 있음<br>
 max-width를 사용하면 자동으로 요소 너비가 줄어듬

2. margin/padding
+ margin 또는 padding에 -top,-right,-bottom,-left 를 붙여 방향별 margin/paddin 설정 가능
+ 순서대로 작성하여 한번에 설정하는 단축 속성도 사용 가능
```html
margin : 10px 20px 30px 40px;
---아래와 동일---
margin-top : 10px;
margin-right : 20px;
margin-bottom : 30px;
margin-left : 40px;
```
3개의 속성값 설정시
```html
margin : 10px 20px 30px
---아래와 동일---
margin-top : 10px;
margin-right : 20px;
margin-left: 20px;
margin-bottom : 30px
```

2개의 속성값 설정시
```html
padding : 10px 20px;
---아래와 동일---
margin-top : 10px;
margin-bottom : 10px;
margin-right : 20px;
margin-left : 20px
```

#### 참고 : block 특성을 가진 요소에 대한 중앙 정렬(margin 활용)
```html
width : 10px /* 명시적으로 지정*/
margin-right : auto;
margin-left : auto;
---단축 설정 활용---
margin: 10px auto
```

3. border
    1. border-style : 선 스타일
    2. border-width : 선 굵기, 정수형이나, thin, medium의 키워드로도 설정가능
        + border-width는 border-style과 함께 설정되어야 한다.
    3. border-color : 선 색상 지정
    4. border-radius : 테두리 모서리 둥글게 표시
    + 단축 속성 : border-width, border-style, border-color 순으로 한번에 설정할 수 있는 단축 속성

## box-sizing
width : height 대상 영역 설정

* content-box : width,height 속성 값은 content영역 의미(default)
* border-box : width,height 속성 값은 content+padding+border를 의미

### 참고 : CSS 스타일링과 box-sizing
* CSS 적용시, 모든 block 요소는 box-sizing을 border-box로 하는것이 일반적
* box-sizing은 상속되지 않고, HTML 요소의 default box-sizing을 content-box 이므로, 전체 요소의 box-sizing을 border-box로 설정하기위해 다음과 같이 설정
```html
*,
*::before,
*::after {
    box-sizing : border-box;
}
```

# CSS background
> 메인 화면에서 background 이미지를 꼭 사용하게 되고, 신뢰감있는 사이트 구성을 위해 세부설정이 필요하다.

## background-image 속성
: CSS요소에 배경 이미지를 설정
```html
<style>
    div {
        background-image : url(주소);
    }
</style>
```

## background-repeat 속성
: 배경 이미지가 요소 사이즈보다 작을때의 채우기 설정

* repeat : 배경영역을 채울 때 까지 반복, 사이즈가 초과 될경우 잘림(default)
* space : 사이즈가 초과되지 않게 image간의 간격을 조정하며 반복,
    + image 크기가 요소 사이즈보다 클 경우 이미지가 잘릴수 있음
* round : 사이즈가 초과되지 않게 image의 사이즈 조정하며 반복
* no-repeat : 반복 없음

### 반복 세부 설정
* repeat-x : 가로만 반복
* repeat-y : 세로만 반복
* repeat repeat : 가로, 세로 동시 조정

### 복수의 이미지 설정 가능
: 먼저 설정된 image가 전면에(repeat 설정시, 먼저 설정된 이미지로 덮일 수도 있음)

## background-size 속성
: 배경 이미지의 사이즈 설정을 위한 속성

* auto : 이미지 크기 유지
* lengt : 두 개의 값을 입력받아 가로, 세로 크기를 조정
* cover : 요소를 채울 수 있도록 이미지 사이즈 조정
* contain : 요소 사이즈를 벗어나지 않는 최대 크기로 조정
* initial : 기본값으로 설정

## background attatchment 속성
: 브라우저의 스크롤시의 배경 이미지 설정

* fixed : 화면을 스크롤 하여도 background image는 고정
* scroll : 화면 스크롤시 내려감(default)

## background-position 속성
background-image는 좌측 상단에 위치(default) <br>
이를 background-position의 좌표(x,y) 형식으로 위치를 지정할 수 있음

### 주요 속성 값
: 기본적으로 두 값(x,y) 설정 가능, 한 속성만 설정할 경우 다른 값은 center<br>

    center : 정중앙
    left top : 좌상단
    left center : 좌중앙
    left bottom : 좌하단 ...
    x y : %,px,em 등으로 위치 지정 가능, 0% 0% 은 좌상단, 100% 100% 은 우하단

## background-color 속성
CSS 색상 단위로 배경색 설정 가능
    + transparent : 투명 (default)

## background 단축 속성
다음 순서대로 다양한 background 속성을 한번에 설정 가능<br>
    background : color image repeat attachment position

**예시**
```html    
<style>
    background : yellow url(주소) no-repeat fixed center;
</style>
```

# CSS Block 과 inline

## block과 inline
* 모든 HTML 태그는 각 태그마다 default로 block, inline 속성을 가진다.

## block 특성
* 항상 새로운 라인에 표시 => 한 line에 block 요소는 1개만 가능
* 화면 너비 전체를 차지 (width : 100%)
* width, height, margin, padding 속성 설정 가능
* block 내부에 inline 요소 포함 가능
* block 특성을 default로 가지는 주요 HTML 태그
    + div
    + h1~h6
    + p, ol, ul, li
    + hr, table, form

## Inline 특성
* 동일한 라인에 다른 요소와 함께 위치 가능
* content 너비만큼 width 차지
* width,height, margin, padding 속성 지정 불가
    + 상,하 여백은 line-height로 지정 가능
* inline 요소 뒤에 공백이 있을 경우 정의하지 않은 space가 자동 지정
    + 공백, 엔터, 스페이스 모두 임의 space(4px)로 변환
* block의 특성을 가지는 요소를 포함할 수 없음
* inline 특성을 default로 가지는 HTML 주요 태그
    + span, a, strong, img, br, input, select, textarea, button

### CSS display 속성
: 모든 HTML 태그의 default 특성을 display 속성을 통해 변경 가능하다.<br>

**display 속성**<br>

    block : block 특성
    inline : inline 특성
    inline-block : inline-block 특성
    none : 해당 요소 미표시(차지하는 공간 삭제)

### visibility 속성
요소를 보이게 할 것인지 아닌지를 설정

> ```display:none``` 과 ```visibility:hidden```의 차이점에 주의 할것 

    visible : 해당요소를 보이게 함
    hidden : 해당요소를 보이지 않게 함 (차지하던 공간은 그대로 남겨둠)
    collapse : 행이나 열을 보이지 않게(table)
    none : table의 row나 column을 보이지 않게 한다. Chrome에서 미동작

### inline-block 특성
block과 inline 특성 모두를 가짐

**inline 요소와 같이 한 라인에 표현되면서도, width,height,margin,padding 설정 가능**<br>

주요 특성

* 동일라인에 다른 요소들과 표시
* width, height, margin, padding 지정 가능
* content 너비만큼 width 차지
* 요소 뒤에 공백이 있을 경우 정의하지 않은 space(4px)가 자동 지정

# CSS font

## font-size 속성

**주요 값**
    medium : 웹브라우저에서 정한 기본 글자 크기
    xx-small,x-small,small,large,x-large,xx-large : medium에 대한 상대적 크기 설정
    smaller,larger : 부모 요소에 대한 상대적인 크기 설정
    length : px, %, em, rem 등의 CSS 단위로 크기 설정

## font-family 속성
> 일반적으로 font-family에 여러 폰트를 설정하는 경우가 많음

```html
    font-family : 첫번째 폰트, 두번째 폰트, ...
```

* 폰트는 웹 페이지를 보는 각 사용자 PC에 설치 되어있어야 하므로, 설정된 순서부터 설치되어있는 폰트를 설정
* 일반적으로 세개 정도 설정하고, 마지막 폰트는 어느 PC에나 있을법한 generic-family를 사용
> generic family에는 seift, monospace, cursive, fantasy 등이 있음

## 웹 폰트 사용법
* 폰트가 설치되어있어야 표시됨
* 웹폰트를 사용하여, 사용자 PC에 폰터가 없더라고, 웹 브라우저에서 폰트를 다운로드받아 표시되게 할 수 있음
> 웹폰트는 pc 설치 폰트보다 경량화 된 형태
> 다운로드 받아 표시하므로 설치되어있는 폰트 사용보다 느릴 수 있음

**적용 예시(Black Han Sans)**

1. link 태그 복사
```html
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap" rel="stylesheet">
```
2. font-family 설정에서 폰트 이름 확인
```html
    font-family : 'Black Han Sans' , sans-serif;
```
3. 작성할 html 페지의 head에 link 태그로 삽입


## font-style 속성
: 글자 모양 설정

* normal : default 모양
* italic : 기울임
* oblique : 기울임

## font-weight 속성
: 글자 굵기 설정

* number : 100,200,300,....900 (숫자로 굵기를 미세하고 조정가능)
* normal : 기본 속성(400)
* bold : 굵은 글씨(700)
* bolder : 상속된 값보다 굵게
* lighter : 상속된 값보다 얇게


## font-variant 속성
: 소문자를 소문자 크기의 대문자로 바꾸는 설정

* normal : 그대로
* small-caps : 소문자를 소문자 크기의 대문자로

## line-height 속성
: 라인 높이 설정

* normal : 기본값(보통 1.2)
* length : px, %, em, rem 등의 CSS 단위로 높이 설정
* number : 글자 크기의 배수로 높이 설정

## letter-spacing, word-space 속성
: 글자 사이 간격, 단어 사이 간격 설정
> 보통 CSS 단위를 사용하며, 키울수록 간격이 넓어지고, 음수도 가능

## text-align 속성
: 글자 수평 설정
    left, right, center : 좌, 우, 중앙 정렬
    justify : 양쪽 정렬

## text-decoration 속성
: 글자에 선을 넣는 속성
    none : 선 없음(default)
    line-through : 글자 중간에 선
    overline : 글자 위에 선
    underline : 글자 아래에 선

## white-space 속성
: 글자에 들어있는 스페이스, 탭, 줄바꿈, 자동 줄바꿈 설정
    normal : 스페이스와 탭 병합, 줄바꿈 병합, 자동 줄바꿈
    nowrap : 스페이스와 탭 병합, 줄바꿈 병합,
    pre : 스페이스와 탭 보존, 줄바꿈 보존
    pre-wrap : 스페이스와 탭 보존, 줄바꿈 보존, 자동 줄바꿈
    pre-line : 스페이스와 탭 병합, 줄바꿈 보존, 자동 줄바꿈

## text-overflow 속성
: 문자열이 넘칠 경우의 처리 설정

1. width 설정
2. white-space : nowrap
3. overflow 속성이 visible 이외의 값

**속성 값**
    clip : 텍스트를 잘라냄
    ellipsis : 말줄임표로 표시
> 이외의 값은 호환성이 떨어져 사용성이 낮음

# 위치 관련 속성

## position 속성
: HTML 요소 위치 결정 방식 설정

1. static position(정적 위치)
* 다른 태그와의 관계에 의해 자동 배치, 위치 임의 설정 불가능, 

2. relative position(상대 위치)
+ relative 미설정시 원래 위치를 기준으로 좌표 지정 가능
+ 문서의 일반적인 흐름에 포함
    - 문서의 일반적인 흐름에 포함 되므로 relative 미설정시 요소가 상대 위치로 이동
> 문서의 일반적인 흐름 : 요소를 어느 방향으로 나열할지 결정

3. absolute position(절대 위치)
+ 가장 가까운 위치의 relative인 부모 요소를 기준으로 left,right,top.bottom 값으로 위치 설정
+ relative인 부모 요소가 없으면, body 요소를 기준으로 위치
+ 문서의 일반적 흐름에서 포함되지 않고, 페이지 레이아웃 공간도 배정하지 않음
    - 다른 요소가 먼처 위치를 점유해도 덮어 씌워짐(이를 부유 객체라고 함)

4. fixed position(고정 위치)
+ viewport를 기준으로 특정 위치에 배치
+ 문서의 일반적 흐름에서 배제, 레이아웃 공간 미배정

## z-index, overflow 속성

### z-index 속성
: 큰 숫자값을 지정할 수록 화면 전면에 출력

### overflow 속성
: 자식 요소가 부모 요소의 영역을 벗어났을 때 처리 방법을 정의

    visible : 벗어난 부분 표시
    hidden : 벗어난 부분을 잘라냄
    scroll : 벗어난 부분이 없어도 스크롤 표시
    auto : 벗어난 부분이 있을때만 스크롤 표시

# CSS transition
: CSS 속성 변경시, 값 변화가 텀을 두고 일어나도록 해서, 일종의 애니메이션 효과를 주는 기능

## 주요 CSS transition 속성
    transition-property : 대상이 되는 CSS 속성 지정
    transition-duration : 트랜지션이 일어나는 시간을 지정
    transition-timing-function : 함수를 사용해 시간별 트랜지션 속도 지정
    transition-delay : 트랜지션 시작 시간 지정
    transition : 모든 속성을 한번에 지정하는 단축 속성

## transition-property와 duration
**transition-property** : 대상이 되는 CSS 속성명을 지정(default : all) <br/>
**transition-duration** : 트랜지션이 일어나는 일정 시간을 s, ms 단위로 지정(default : 0s)

## transition-timing-function
cubic-bezier() 함수에 대한 이해 필요<br>
>cubic-bezier()는 bezier curves(베지어 곡선) 을 정의하는 함수로 사용

### 주요 transition-timing-function 속성 값
* ease : 느리게 시작하여 빨라졌다가 다시 느려지며 종료
* linear : 동일한 속도로 진행
* ease-in : 느리게 시작하여 동일한 속도로 마무리
* ease-in-out : 일정 속도로 진행, 점점 느려지며 종료
* step-start : 바로 실행
* step-end : 일정 시간 후 종료
* steps : n 단계로 나누어서 변화
* cubic-bezier(n,n,n,n) : 베지어 곡선으로 진행(n값 : 0~1)

## transition-delay
: 언제 시작할지 지정

### transition 단축 속성
```html
    transition : property duration function delay
```
# CSS animation
transition 과 유사하게, CSS 스타일을 부드럽게 전환

## transition과 animation
transition : 변경되어야할 스타일만 지정<br>
animation : 중간에 변경되는 스타일을 세밀하게 지정<br>

animtaion은 CSS 스타일과, 중간 상태를 나타내는 키프레임으로 구성

> JS 기반 애니메이션보다, 렌더링 성능이 좋다.
> 가벼운 효과 => CSS 애니메이션
> 세밀한 제어 => JS 애니메이션

## 주요 CSS animation 속성

### Keyframes 문법

1. keyframes 이름 정하기
```html
@keyframes 이름 {

}
```
2. keyframes의 원하는 시점에 스타일 지정하기
0% , from : 시작 프레임<br>
100% , to : 마지막 프레임<br>
0~ 100% 사이 : 원하는 시점 프레임<br>
```html
    @keyframes ball {
        0%{

        }
        50%{

        }
        100%{

        }
    }
```
3. 애니메이션 요소 설정
    + animation-name에서 정희한 이름
    + animation-duration에 소요시간 지정
    + animation-iteration-count에 반복횟수 지정(infinite : 무한 반복)
```html
    name{
        animation-name : ball;
        animation-duration : 5s;
        animation-iteration-count : infinite;
    }
```

### animation-timing-function
transintion-timing-function과 동일하게 사용 가능<br>
default는 ease

### animation-duration, animiation-delay
동작 시간과, 지연시간 설정 (s,ms)

### animation-iteration-count
정수로 지정 가능, infinite는 무한 반복

### animation-direction
    속성        설명
    normal      0에서 100%까지 진행
    reverse     100%에서 0방향으로 진행
    alternate   홀수번째는 normal, 짝수 번째는 reverse로 진행
    alternate-reverse 홀수번쨰에는 reverse, 짝수 번째는 normal로 진행   

### animation-fill-mode
> 이해하기 복잡한 개념이므로 실습을 통해

    none : 초기상태 => 0% => 100% => 초기상태
    forward : 초기상태 => 0% => 100% => 100%
    backwards : 0% => 0%=> 100%=> 초기상태
    both : 0 => 0 => 100% => 100%

### animation-play-state
javascript와 사용해, 이벤트에 따라 해당 속성을 변경

    paused : 중지 상태
    running : 실행 상태

### animation 단축 속성
```html
    animation : name duration timing-function delay iteration-count direction fill-mode play-state
```

# CSS transform
: 요소의 회전, 크기 조절, 기울이기, 이동효과를 부여하는 함수 제공<br>

키프레임 기반 설정은 제공하지 않으므로, 이를 위해서는 CSS animation, transtion과 함께 사용해야 한다.

## CSS transform 사용법
```html
transform : tranform 함수;
```
CSS transform 함수로 요소 이동 및 변형시 x,y,z로 요소 변경을 설정 할 수 있다.

### 주요 transform 함수

    translate(x,y) : 위치를 x, y 이동
    translateX(x) : x 이동
    translateY(y) : y이동
    scale(x,y) : 크기를 가로 x,세로 y배
    scaleX(x) : 가로 x배
    scaleY(y) : 세로 y배
    skew(x-angle,y-angle) : 가로 x, 세로 y 만큼 기울임
    skewX(x-angle) : 가로 기울임
    skewY(y-angle) : 세로 기울임
    rotate(angle) : 주어진 각만큼 회전

## transform-origin 속성
: 요소의 기준점을 변경하는 속성<br>
scale(),rotate(),translate(),skew() 동작은, 기본적으로 해당 요소의 중심 기준으로 동작 <br>

사용법
```html
    tranform-origin : x축 | y축 | z축
```

# CSS float 속성
웹페이지에서 텍스트와 함께 이미지 배치를 위해 고안되었지만, 수평 정렬을 위해서도 사용

* 수평 정렬을 위해 float,flexbox,grid를 사용 할 수 있음
    + float는 본래 수평 정렬을 위한 속성이 아니고 복잡하고 특별한 룰셋을 가지고 있어, 기본 동작과 달라보이는 케이스가 나타날 수 있다.
    + flexbox와 grid는 호환성 이슈로 사용하기 어려웠지만, flexbox의 경우는 호환성이 해결된 수준
    + flexbox,grid는 수평 정렬/배치를 위해 고안되었다.

## float 속성

    none: 떠있지 않게 함
    right : 요소를 오른쪽으로 이동
    left : 요소를 왼쪽으로 이동

## clear 속성
:float을 해제하는 속성
    none : 양쪽 float를 사용 할 수 있음
    right : 왼쪽 float 사용 해제
    left : 오른쪽 float 사용 해제
    both : 양쪽 float 사용 해제

## 정렬과 float 속성

* 수평정렬할 요소들을 left로 설정시 왼쪽 정렬, right로 설정시 오른쪽 정렬
* 오른쪽 정렬의 경우, 먼저 설정한 요소가 오른쪽 끝에 놓여짐

## float 정렬의 기본 문제점
float의 부유성때문에 float 속성이 사용되지 않은 요소와 곂치는 문제가 있다.
### 문제해결을 위해 clearfix class안에 float 요소를 사용
```html
.clearfix:after{
    content: "";
    claer : both;
    display : block;
}
```

## float 속성의 특성
* float 속성으로 설정한 요소는 기본적으로 display 특성을 block 특성으로 변경
    + display 가 flex 등으로 설정되어 있는 경우 제외
* block 특성을 가진 요소는 기본 width가 100%인 반면 float 속성이 설정된 요소는 요소의 크기만큰 width가 설정된다.
* float 설정시, float가 적용된 요소에 content가 있을 경우, 해당 content의 width, height가 다음 요소의 content에 영향을 줌

# CSS 상속

## 상속과 CSS 우선순위
요소간에는 부모, 자식관계가 있고, 상속은 부모 요소의 속성을 자식요소가 물려받는 것을 의미


## 주요 속성 별 상속 여부
* 속성별로 상속유무가 다르다.(태그별 상속유무도 다름)
* 상속가능 : text-align, line-heignt, color, font, visibility, opacity
* 상속 불가능 : width, height, margin, padding, border, display, box-sizing, background, vertical-align, position, z-index, overflow, float

## 강제 상속 설정
부모의 속성중 상속되지 않는 속성을 상속하고 싶을떄는, 자식 요소의 해당 속성값을 inherit로 설정하면 된다.

## CSS 우선순위와 Cascadinxg

다양한 CSS 속성 적용과 상속으로 인해, 특정 요소에 어떤 속성값이 적용될지 결정해야함

### Cascading 기본 규칙

**중요도 : CSS를 어디에 선언했는지에 따라 우선순위가 달라진다.** 
1. ```head``` 태그 안의 style 요소
2. ```head``` 태그 안의 style 태그안의 @import 문
3. ```<link>```로 연결된 CSS 파일
4. ```<link>```로 연결된 CSS 파일 안의 @import 문

**명시도 : 대상을 명확하게 지정할 수록 높은 우선순위**
**선언순서 : HTML 문서상 뒤에 나오는 CSS가 높은 우선순쉬**

### CSS 우선순위 기본 규칙
> 중요도, 선언 순서보다는 명시도가 우선순위에 많은 영향을 미친다.

1. HTML 문서상 뒤에 나올수록 높은 우선순위
2. 기본 우선순위(높은 순으로 정렬)
    * 속성값뒤에 !important를 기대할 경우 (최우선)
    * 태그 안에 속성으로 기재한 style에 의해 설정된 속성 (1000점)
    * id로 선택한 CSS Selector 에서 적용된 속성 (100점)
    * class,html 속성, pseudo class 로 선택한 CSS Selector에서 적용된 속성(10점)
    * 태그 또는 가상 요소 셀렉터로 선택한 CSS Selector에서 적용된 속성(1점)
> !important > Inline Style > id > class > tag
> !important, 태그안의 style은 현업에서는 사용을 제한한다.(복잡도 문제)

# CSS media query와 responsive Layout

## Reactive Web
: 접속기기에 따라 자동으로 화면이 조정되는 Webpage

* 기존에는 bootstrap 기반으로 반응형 웹을 자동 구현하거나, 웹 퍼블리셔가 처리
* 풀스택이 되어, 그럴싸한 웹서비스를 구현하지 위해서 개발 단계에서 반응형 처리 필요 

## 적응형웹 과 반응형 웹
* 적응형 웹 : 사용자의 환경(mobile,pc)에 따라 다른 페이지를 보여줌
    + ex) naver.com 과 m.naver.com
* 반응형 웹 : 환경에 관계없이 동일한 페이지를 보여주지만, 화면 사이즈에 따라 조정


## Pixel 과 Viewport
* Pixel : Picture Element(화소). 컴퓨터 화면을 구성하는 최소 단위
* Viewport : 사용자 환경에 해상도가 달라져도 동일한 화면을 구성하기 위해 도입된 개념으로 화면상의 표시 영역을 의미. 
* meata viewport 설정 : viewport 에 입력한 width길이에 맞춰 웹 페이지표시 (default 980px)<br>
width에 device-width를 입력하여 기기의 너비값에 맞추어 화면 출력
### PPI(Pixels Per Inch) 
: 픽셀 밀도, 또는 화소 밀도라고 불리며 단위 면적당 화소수를 나타냄

### 주요 속성
    width : vieport 너비(px)
    height : viewport 높이(px)
    initial-scale : viewport 초기 배율(default:1.0)
    user-scale : 사용자의 웹페이지 확대-축소 가능여부(default:yes)
    maximum-scale : 최대 배율
    minimun-scale : 최소 배율

## 레이아웃 과 미디어 쿼리
Layout : 각 페이지 구성 요소를 페이지 내에 효과적으로 배열하는 작업

### 반응형 레이아웃
: HTML5에 정의된 Semantic tags 기반으로 일반 레이아웃 기반 반응형 레이아웃

### 미디어 쿼리
: 반응형 레이아웃 구현을 위해 사용되는 서로 다른 미디어 타입에 대응하기 위한 기능<br>
CSS3의 가장 큰 추가기능 중 하나
> @media를 사용하는 것이 핵심
### 미디어 쿼리 기본 문법
```html
    @media media-type and (media-feature-rule) {

    }
```
* media-type : all 또는 screen 사용
    + all : 전체
    + print : 프린트 화면
    + screen : 브라우저 화면
    + speech : 음성
* media-feature-rule : media 조건, 주로 min/max-width, orientation 정도 사용
    width/height : min-max 최소/최대 너비,높이
    device-width : 디바이스의 물리적 너비
    device-height : 디바이스의 물리적 높이
    orientation : 디바이스 방향(가로:landscape, 세로:portrait)
    aspect-ratio : viewport의 종횡비
* 논리 연산자(and,not,only)를 붙여 복잡한 조건을 만들 수 있음
    + only : 구형 브라우저 지원을 위해 only screen and 처럼 쓰면 좋음
    + comma(,) : 여러 미디어 조건 나열을 위해 사용

### 참고 해상도

* 320px~480px : 스마트폰
* 481px~768px : 태블릿
* 769ox~1024px : 저해상도 노트북
* 1025px~1200px : 데스크탑
* 1201px~ : 고해상도 데스크탑 및 TV

# CSS flexbox

## 수평 정렬 방법과 flexbox (Flexible Box)
* 기존에는 float 과 position 속성을 기반으로 Layout 작업을 실행
* CSS3에서는 레이아웃을 위해 flexbox 속성을 제공하였으나, 그동안은 IE가 지원을 하지않아 사용이 어려웠으나 현재는 많은 개선이 이루어져 flexbox까지 사용이 가능
* grid의 경우는 호환성 문제가 있어 조심해햐할 필요가 있음

### flexbox의 이해

**div.item을 수평으로 정렬하려면?**
1. item 클래스에 inline-block을 display 속성으로 지정. 이 경우 작성 방식에 영향을 미침(줄 바꿈, 탭)
2. float 사용. 이 경우 부모 요소 위에 존재하게 되므로, 형제 요소와 곂칠 수 있음 => (clearfix로 해결)
3. flexbox를 사용하면, 비공식적인 방법 없이 깔끔하게 요소들을 수평정렬 할 수 있음

## flexbox container 관련 속성
flexbox의 구성 요소 
* 상위 부모 요소인 flex container
* 하위 자식 요소인 flex item 
=> 수평 정렬할 요소 : flex item, 정렬할 요소를 감싸는 부모요소 : flex container

### flex container 에서 설정 가능한 속성
    display : flex container 정의
    flex-direction : flex item들의 주 축 방향 설정
    flex-wrap : flex item들을 1행 또는 복수의 행으로 배치하는 설정
    flex-flow : flex-direction과 flex-wrap을 한번에 설정하는 단축 설정
    justify-content : 주 축 기반 정렬 방법 설정
    align-content : 교차축 기반 정렬 방법 설정(2행 이상)
    align-items : 교차 축 기반 정렬 방법을 설정(행마다 적용)

### display
    + flex: flex container 정의 (container간 수직 정렬)<br>
    + inline-flex : inline 특성의 flex container 정의(container 간 수평 정렬)
###  flex-direction : 정렬 방법 설정
    + row : 왼쪽 수평 정렬
    + row-reverse : 오른쪽 수평 정렬
    + column : 수직 정렬
    + cloumn : 아래부터 수직 정렬
### flex-wrap : flex-item들의 행 배치
    + nowrap : flex item 들을 개행하지 않고, 항행에 배치(default)
    + wrap : flex item들의 너비 합이 flex container 너비보다 클 경우 개행
    + wrap-reverse : flex item들의 너비합이 container 너비보다 클 경우 역방향으로 개행하여 표시
### flex-flow : direction과 wrap 속성의 단축 프로퍼티
### justify-content : 주 축 기반 수평 병렬 방식 설정
    + flex-start : 왼쪽부터 수평정렬
    + flex-end : 오른쪽 수평 정렬
    + center : 가운데 수평 정렬
    + space-between : 좌우끝에 item 배치후 내부 item들은 균등 간격으로
    + space-around : container 내부에 균등간격으로 배치
### align-items 과 align-content
    + align-items : 교차축 기반 정렬 (각 행 마다 적용)
        - flex-start : 영역 시작점에 정렬
        - flex-end : 영역 끝점에 정렬
        - center : 각 행의 교차 축 가운데 정렬
        - baseline : 각 행의 문자 기준선 정렬
    + align-content : 교차 축 기반 정렬 (복수의 행을 하나의 그룹처럼 적용)
        - stretch : default 설정. 교차축을 채우기 위해 자동 조정
        - flex-start : 축 시작점에 정렬
        - flex-end : 축 끝점에 정렬
        - center : 전체 container의 가운데에 정렬
        - space-between : 좌우끝에 item 배치후 내부 item들은 균등 간격으로
        - space-around : container 내부에 균등간격으로 배치
## flexbox item 관련 속성
    order : item 배치 순서 설정
    flex-grow : item 너비 증가 비율 설정
    flex-shrink : 너비 축소 비율 설정
    flex-basis : 기본 너비 설정 (공간 분배 이전)
    flex : grow, shrink, basis의 단축 속성
    align-self : container의 설정보다 우선해서, 개별 item 수직 정렬 방법 설정

### order
: flex item 배치 순서 설ㅈ어

* default 값은 0
* order 값이 낮은 순서대로 배치

### flex-grow
: flex iem 너비 증가 비율 설정

동일한 flex-grow 값을 가진 item 들은 동일한 너비를 가지며, flex-grow 값이 다를경우<br>

```해당 flex item의 grow 값/ 전체 flex item의 grow 총합```

비율로 너비 조정(너비 조정 속성이 많이 때문에 정확하게 떨어지지는 않는다.)

### flex-shrink
: flex 너비 축소 비율 설정

* defalut 값은 0
* shrink 값이 동일하면, 동일한 비율로 container안에서 축소
* shrink 값이 다르면, item의 shrink 값/ shrink값의 전체 합 비율로 축소

### flex-basis
flex item 기본 너비 설정

### flex
: flex-grow, flex-shrink, flex-basis 속성의 단축 속성

### align-self
container 레벨의 수직 정렬 방법보다 우선하셔 flex item의 수직 정렬 방법을 설정<br>
align-content/align-items와 동일한 속성값으로 정렬 가능
```html
align-self : flex-start | flex-end | center | baseline | stretch
```

**참고 링크**
https://www.outpan.com/app/1b970b008f/flexbox-playground
https://flexboxfroggy.com/