# Javascript

웹 페이지 상에서 동적으로 요소를 변경하고, 사용자 인터페이스를 지원하기 위해 고안된 스크립트 언어.<br>
넷프케이프 커뮤니케이션 사에서 개발. 원래 이름은 모카, 라이브스크립트 였어나, JAVA언어의 인기에 따라, 관련이 없음에도 Javascript라고 명명하게되었음.

## ECMAScript
* 넷스케이프의 Javascript에 대응하기 위해, MS에서 JS와 호환되게 개발안 언어
* 표준화된 언어의 공식 이름은 ECMAScript(에크마스크립트) 이며, 대외적으로 JS로 불림

## Javascript 엔진
* JS는 웹브라우저 상에서 동작하며, 각기 다른 JS엔진 구현 또는 채용 중
    + JS엔진 : JS코드를 이해하고, 실행하는 인터프리터
* 최근 사용되는 JS 엔진
    + V8 : 구글에서 개발하였으며, 크롬, electron, node.js에서 사용중
    + SpiderMonkey : fireFox 에서 사용 중
    + JavaScriptCore : 오픈소스로 Apple과 Safari 브라우저에서 사용

## 최근 javascript 동향
* 웹페이지의 동적요소를 변경하고, UI를 지원하기 위해 Frontend에서만 사용되었음
* Server Backend 기술인 Node.js가 JS기반으로 동작하게됨
* 최근에는 Electron을 사용한 데스크탑 프로그램, React-native, NativeScript등을 사용한 모바일 앱도 만들 수 있게 되었음
* 잘 설계된 언어가 아니라, 크로스 브라우징 문제로 인해 새로운 언어가 바로 채용되지는 못하는 실정
* 크로스 부라우징 문제를 해결하기위해 현재는 ES6기준으로 사용
    + ES6는 ECMAScrpit 6 로 알려진 2015년에 추가된 문법

> JS가 다양한 분야에 많이 사용되므로, Python 만큼 익혀둘 필요가 있다고 볼 수 있음
> JS는 엔진은 V8이 중심이고, 문법은 ES6까지를 잘 알고있어야 함.

## Javascript Naming Rule
* 변수, 함수등은 camelCase로 명명함
    + CamelCase : 두단어를 붙여 쓸 경우, 맨 앞단어 는 소문자, 뒤에 나오는 단어마다 첫글자를 대문자로 작성
* boolean 변수는 is, has, are과 같은 동사를 써서 나타내는 것을 권장
* class명은 PascalCase로 작성
    + 두단어를 붙여 사용할때, 단위단어의 앞글자를 대문자로 작성
* class의 멤버함수, 또는 외부의 함수등은 모두 camelCase로 작성
    + 함수/method는 동사로 시작하는 것을 추천

### 주석
```js
    // 주석
    /* 주석 */ 
```
## 변수
### 변수 선언
: 변수 선원 키워드(let)을 사용하여 선언, 재할당 불가능
```js
let 변수명;
let 변수명 = 변수값;
```

### 상수 선언
: 상수는 초기화 이후에 값 변경이 불가능
```js
const 상수명 = ;
```

## javaScript의 자료형
    1. Number
    2. String
    3. Boolean
    4. null
    5. undefined
    6. object
    7. Symbol 

1.  Number
* 정수/부동소숫점을 통쨰로 Number type으로  처리
    + 64bit 부동 소수점 사이의 값

### typeof
변수의 데이터 타입을 확인하기 위한 문법
```js
typeof 변수명
```
2. Boolean
* true와 false로 표현

3. null과 undefined
* null : 값이 존재하지 않음을 의미
* undefined : 값이 할당되지 않았음을 의미

4. object
* 객체 타입을 표현
* python과 마찬가지로 결국 모든 기능을 객체로 다룸

5. Symbol
* ES6에서 추가된 타입으로 unique한 값을 생성
```js
Symbol ((description));
```