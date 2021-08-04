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