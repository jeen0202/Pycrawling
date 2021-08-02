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