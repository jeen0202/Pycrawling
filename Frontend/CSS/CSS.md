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