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

### Data type 변환
1. Number() : Number 형으로 변환
```js
Number("1.2")
```
2. parseInt() : Number type 정수형으로 변환
```js
parseInt("1.2")
```
3. parseFloat() : Number type 실수형(부동소수점)으로 변환
```js
parseFloat("1.2")
```
4. String() : 문자형으로 변환
```js
String(1.2)
```
5. Boolean() : 논리자료형으로 변환
```js
Boolean(-1)
```

### 동등 연산자와 일치 연산자
동등연산자(==, !=) : 관대한 비교방식으로 값이 같은지 비교
일치연산자(===, !==) : 염격한 연산자로, 값과 자료형이 같은지 확인

### 논리 연산자
    ! : NOT
    && : AND
    || : OR

### 문자 연산자
: +를 사용하여 문자열을 합칠 수 있다.

### 조건문
코드 블록({}) 으로 내부 실행문을 구분
```js
if (조건) {
    실행부;
}
else{
    실행부;
}
```
```Javascript에서는 switch/case 문이 지원된다```

## 함수
기본문법
```js
function 함수이름(파라미터){
    실행코드
    return 반환값
}
```

### 화살표(Arrow, => ) 함수
: 함수 선언을 보다 간단하게 하기 위해 ES6에서 고안된 방법<br>
익명 함수로 사용되며, 이를 호출하기 위해 변수에 대입하는 경우가 많음
```js
let func = (parameter) => expression
```
위와 같은 일반 함수식
```js
let func = function(parameter){
    return expression;
}
```
화살표 함수를 사용한 단축 문법
* function 키워드 생략
* 파라미터가 하나일 경우 괄호() 생략
* 함수 코드가 단일 라인일 경우, 코드 블록{} 및 return 생략
```js
//예시
let func1 = () => "Hello Arrow!";
```

## 객체
: JS의 객체는 대게 Property와 Method로 이루어져 있다.
    javascript : Property와 Method 
    Python : Attribute와 Method
    CSS : Property와 Property 값
    HTML : Attribute와 Attribute 값

### Property와 Method
* Property는 Key-Value로 구성
* Key는 문자열 또는 Symbol 값으로 구성, Value는 해당 Key에 저장하고자 하는 데이터
* Method는 객체가 보유하고있는 함수
* JS 객체 생성 방법
    1. 객체 리터럴 방ㅅ힉
    2. new Object() 생성
    3. 생성자 함수로 생성

### 객체 리터럴 생성 방법
> JS는 프로토타입 기반 객체 지향 언어이기 때문에, 객체 생성방식이 클래스 기반 문법과 다르다.
> 이를 객체 리터럴이라고 부른다.
> ES6에 와서는 클래스 기반 객체 생성 문법도 지원하고 있다.

* 객체 생성 방법 : {} 안에 Key:Value 로 필요한 프로퍼티를 정의
    + JSON, Python의 dic 자료형과 유사한 측면이 있음
```js
const 객체명 = {
    Key1: Value1,
    Key2: Value2,
    ...
};
```
* const를 사용하여 선언
* const 선언시 객체이름은 다른 객체로 재할당 될 수 없음
    + 객체 내부의 Property, Method 는 변경 가능
* 객체 주소값이 변경 될 수 있다면 const 대신 let을 사용
* 빈 객체 선언후, Property와 Method 추가 가능

**객체리터럴사용시 주의사항**<br>
* this 키워드
    + this 키워드는 자신의 객체를 가르킨다.

**Getter 와 Setter**<br>
* 클래스 기반 문법에서는 내부 변수를 외부에서 어느 범위까지 접근할 수 있는지 지정 문법 제공
    + public, private, proteceted...
    + 정보 은닉 및 캡슐화를 위해 사용
* JS 객체 리터럴 에서는 getter와 setter를 제공
    + 접근자 Property라고 불리며 접근제어를 위해 사용한다.
* getter는 선언시 파라미터가 없어야하고, setter는 파라미터가 한개이상 있어야 한다.
```js
get prop() {
    ...
}
set prop(param) {
    ...
}
```
### new Object 생성 방법
> 객체 리터럴, 생성자를 권장하므로 자주 쓰이지는 않는다.

```js
const 객체명 = new Object();
```

### 생성자 함수로 생성하는 방법
```js
function 객체명(param1,param2){
    this.프로퍼티명 = value;
}

const 객체명 = new 객체명(param1,param2);
```

### 프로토타입
: 생성자 함수에 프로퍼티 또는 메서드 정의 가능
```객체이름.prototype.프로퍼티명=....```와 같이 사용 가능
```js
객체명.prototype.프로퍼티명 = 프로퍼티값;
객체명.prototype.메서드명 = function() {
    ....
}
```

## Javascript ES6와 Class
* ES6에서 객체 지향 문법과 유사한 class 키워드 기반 객체 생성 문법이 표준화 됨
### 클래스 정의
```js
class 클래스명 {

}
```
**constructor() : 생성자 함수**<br>
* 클래스 내부에서 작성
```js
    class 클래스명 {
        constructor() {

        }
    }
```
* 정의된 클래스는 new 클래스명()을 통해 객체로 생성될 수 있음
* 클래스 프로퍼티는 생성자 내부에서 this 키워드로 선언 될 수 있음
* 객체 생성시 인자 정의는 생성자에서 할 수 있음
* 일반 객체 지향 문법과 유사한 상속을 지원함
    + extends를 사용하여, 상속받을 클래스를 선언할 수 있음
    + 자식 클래스에서는 super() 키워드로 부모의 생성자를 호출
```js
class Super {
    constuctor (파라미터1) {
        
    }
}
class Sub {
    constructor(파라미터2){
        super(파라미터1)
    }
}
```
* 객체지향의 다형성도 지원된다.

**hasOwnProperty 사용법**<br>
* 클래스명.prototype.프로퍼티 = 프로퍼티 값 으로도 클래스 외부에서 프로퍼티 추가 가능
* 클래스 내부에 선언한 프로퍼티임을 확인하기위해 hasOwnProperty(프로퍼티명)을 사용

## javascript의 반복문
### for문
```js
for(초기값,조건,증분){

}
```
**for ...of 문**<br>
: for(배열에서 불러올 아이템 of 배열)로 작성
```js
for(let item of 배열)
{
    item으로 배열의 변수 순차 호출
}
```
**객체와 for문**
* for ... in 으로 객체의 키를 반복할때마다 가져올 수 있음
    + Object.entries(), Object.keys(), Object.values()를 사용하여, Key-value를 기반으로 사용하는 것과 유사한 기능을 사용할 수 있다.
    - Object.entries() : Key-Value로 이루어진 프로퍼티셋의 리스트를 반환
    - Object.keys() : 프로퍼티의 key 리스트 배열 번환
    - Object.values() : 프로퍼티의 value 리스트 배열 반환
### While 문
```js
while(조건){
    조건 만족시 반복
    break; // 반복문 종료
    continue; // 하위 실행문 생략
}
```

## Javascript 배열
### 생성
: 대괄호([])를 사용하고, 내부에서 콤마(,)로 구분한다.

* length를 사용해 길이 확인 가능
* 객체처럼 생성 가능

### 배열 호출 & 수정
: index가 0부터 시작하며 index 번호로 각 아이템 호출 가능

### 삭제
: 배열변수.splice(시작 index값, 삭제할 인덱스의 개수)

### 다양한 배열관련 기능 (함수)

**push**<br>
배열끝에 아이템 추가

**pop**<br>
배열 끝에있는 아이템 반환 후 해당 아이템 제거

**shift**<br>
배열의 첫번째 아이템을 제거하고, index 번호를 떙긴다.

**concat**<br>
두 배열 병합

**join**<br>
아이템 사이에 특정 문자열을 끼워넣어 하나의 문자열로

**reverse**<br>
현재 배열을 역순으로 배치

**slice**<br>
배열의 일부분 반환 

**forEach**<br>
for문을 대체하여, 간단하게 배열의 각 아이템을 호출

**map**<br>
배열의 각 아이템에 함수를 적용하여, 새로운 배열을 반환

**indexof**<br>
배열에서 지정한 위치의 데이터 위치값

**findIndex**<br>
배열 아이템이 객체일 경우, 객체에서 지정한 데이터 위치를 검색하는 방법


**find**<br>
지정한 데이터가 들어있는 객체를 반환

**filter**<br>
특정 조건을 만족하는 경우에 해당 아이템을 추출

## 자주 사용되는 JS 문법
### 1. 삼항 연산자
: 조건식을 처리하는 간결한 문법

* 문법
```js
condition ? exprIfTrue : exprIfFalse
```

### 2. 배열 분할 할당
: 배열의 각 아이템을 별도 변수에 할당
```js
let myArray = [ 1,2,3,4];
let [fisrt,second,third,fourth] = myArray;
```

### 구조 분해 할당 문법 활용

**변수값 swap**<br>
```js
let a = 1;
let b = 3;
[a,b] = [b,a]
```

**함수에서 복수의 데이터 반환**
```js
funciton getData(){
    return[10,20];
}
```

**문자열 split**<br>
* split()
: default값이 없으므로, 명시적으로 인자를 넣어주어야 한다.

## Rest 파라미터
: 함수 인자 선업 앞에 ...를 붙여 사용<br>
해당 함수에 전달된 인자 리스트를 하나의 배열로 변수에 대입<br>
rest 파라미터는 함수의 맨 마지막에 위치해야 한다.

## Spread 파라미터
: 변수에 ..를 붙여 사용하는 문법<br>
iterable 한 변수 앞에 붙여서, 해당 변수의 데이터를 분리

### concat
: 두 배열 병합

## Hoisting(호이스팅) 이슈
: JS에서는 함수 또는 변수의 선언부 상단에서 사용하여도 에러가 발생하지 않는다.

### var 키워드
: 변수선언을 위해 사용되며, let과는 달리 동일한 이름의 변수를 여러번 선언 할 수 있음


### Hosting 현상
```js
//아래의 코드가 에러없이 실행된다.
console.log(a);
a = 10;
console.log(a);
var a = 20;
```

### Hoisting 발생 이유
* JS는 함수와 변수 선언을 실행 영역의 맨 앞으로 이동시켜 실행.
* ES6 이전의 JS는 유효 범위가 Global Or Function 이였기 때문에 함수 외부에서 선언된 함수 또는 변수가 모두 전역변수가 되어버림.
* Hoisting이 일어날 변수의 경우 초기화 없이 선언되어 undefined값을 가지게 됨

### 해결 방안
1. 변수 선언시 var 키워드 대신 Hoisting 이슈가 해결된 let, const를 사용
2. 함수 선언은 함수 표현식으로 사용
    + 함수 표현식 : 함수를 변수(let,const)에 할당하는 문법

## Scope
: JS 변수 또는 함수 선언시, 해당 요소가 유효한 범위를 의미<br>

### JS의 3가지 Scope
1. Global : 코드 전체 범위
2. Function : 함수 내부
3. Block : {} 괄호로 이루어진 범위

**전역 scope**<br>
: 블록이나 함수 안에서 선언되지 않고, 외부에서 선언되어 모든 코드에 포함가능

**Block Scope**<br>
{ } 괄호 내부의 영역을 의미한다.<br>
Block내부에서 let, const 키워드로 선언된 변수는 Block Scope에 속한다.

**var키워드와 함수 scope**<br>
var 키워드는 함수 scope를 가진다.<br>
block 안에서 var키워드로 선언된 변수는 block 외부에서도 유효하며, 이를 block scope와 분리하여 함수 scope로 분리한다.


**전역변수와 지역변수**<br>

동일한 이름을 가진 전역변수와 지역변수가 있으면, 지역변수를 우선 사용

## 동기식 처리와 비동기식 처리
* Syncronous (동기) : 요청을 보낸후, 해당 요청의 응답을 받아야 다음 동작 실행
* Asyncronous (비동기) : 요청을 보낸후, 응답과 상관없이 다음 동작 실행

### 비동기식 처리의 이해
* 일반적인 프로그래밍 언어는 동시직 처리를 지향
* JS의 경우 실행이 오래 걸리는 동작을 기다릴 필요없이 비동기식 처리가 가능하도록 되어있음
* JS는 일반적으로 동기식 처리가 기본이지만, 일부 기능은 비동기적으로 처리가 가능하도록 관련 기능을 추가로 제공하고 있음

### 주요 비동기식 처리
* Rest API 요청
* File/DB 처리
* 타이머, 암호화/복호화

### setTimeout
: 타이머를 지정하여 함수 호출
```js
setTimeout(function, milliseconds)
```

### 비동기식 처리의 문제점
함수 호출의 결과값을 기반으로 영향을 받는 코드가 있을경우 문제가 생길 수 있음
> Vanilla JS 에서 Rest API 호출을 위해, axios를 사용하는 것이 추세임

### 문제점을 해결하기 위한 Callback함수
* JS의 함수는 first-class 함수
    - 함수 자체를 변수에 저장 가능
    - 함수의 인자에 다른 함수를 인자로 전달 가능
    - 함수의 반환값으로 함수를 전달 가능
* 비동기식으로 처리되는 함수에 영향을 받는 함수를 callback으로 넣어 문제 해결

**Callback 지옥**<br>
callback 함수가 너무 많이 반복될 경우 함수의 작성이 너무 복잡해 질수있다.<br>
이러한 문제의 해결을 위해 Promise, async/await등의 문법이 추가되었다.

## Promise
: 비동기식 처리를 위한 콜백함수의 단점을 극복하기 위해 ES6에서 공식적으로 추가된 문법<br>
단순화 하면 Promise객체를 생성하여 then으로 실행하는 방식.

    1. new로 Promise 객체 생성
    2. Promise 객체 내부에서 executor함수가 내부적으로 실행되고, resolve, 실패시 reject 를 비동기 식으로 실행

 ### Promise의 3가지 상태
    1. Pending(대기) : 비동기 처리가 아직 실행되지 않은 단계
    2. Fullfilled(이행): 비동기 처리가 성공적으로 완료된 상태
    3. Rejected(실패) : 비동기 처리가 실패한 상태

### then 메서드
: Promise객체에서 resolve, reject 를 정의하고, promise 코드를 실행해주는 메서드

### catch 메서드
: promise 실행중 예외사항 처리를 위한 메서드<br>
failureCallback가 정의되어있지 않을경우, reject시에 호출됨

**chaining**<br>  
* then과 catch 메서드도 함께 연결해서 실행 가능

### throw
* 사용자 정의 예외를 던질 떄 사용
    - catch block가 있으면 전달되고, 그렇지 않으면 프로그램 종료
```js
throw new Error('메시지');
```

**chaning과 catch**<br>
- 일반적으로 catch를 chaining 맨 마지막에 추가해서, 에러 케이스를 간결히 핸들링

### finally
: Promise의 마지막에 해당 함수를 실행

### Promise.all
* 동기화 처리할 Promise를 묶어서 한번에 실행
* 다중 함수가 모두 실행 완료된 후, then구문 실행

### Promise.race
* 여러 함수중 가장먼저 실행된 함수 종료 이후에 then 구문 실행

## DOM(Document Object Model)
* Document : 구조화된 데이터
* DOM : 구조화된 문서를 객체로 표현하는 방식


### 웹 브라우저의 동작 과정
    1. HTML파일 가져오기
    2. HTML파일 파싱하여 DOM tree 생성, CSS 정보를 파싱하여 CSSOM tree 생성
    3. DOM/CSSOM tree 기반 Render tree 생성
    4. Render tree 기반으로 Rendering

### 웹브라우저 동작과정과 javascript
* JS 코드를 head 태그 내의 script로 작성하면
    - HTMl 코드를 기반으로 DOM 트리를 구성하기전에 script 태그를 마나면, JS 엔진에 제어권 이전
    - JS 엔진이 해당 JS 코드 파일을 로드,실행
    - 이후 HTML로 전환하여 HTML 코드를 읽고, DOM 트리 구성부터 진행
* head 태그 내부의 JS
    - 화면로딩이 느려질 수 있음
    - DOM tree 구성 전에 JS가 실행되므로, DOM을 조작하는 JS는 에러유발
* 결론
    - JS코드는 body태그 종료 직전에 script 태그의 코드 파일 형태로 추가

### window 와 document

* window : 웹브라우저 객체(DOM, BOM, JS로 구성)
* document : DOM 객체

### windows와 BOM(Browser Object Model)
* window : 브라우저 환경 전체 객체
* BOM의 주요 객체
    - navigator 객체 : 브라우저와 운영체제 정보 제공
    - location 객체 : URL 관련 핸들링

### document
document 객체를 통해 HTML/CSS 수정 가능<br>
원하는 HTML을 읽는다는 의미는 원하는 HTML을 찾는다는 의미

#### 조작이 필요한 HTML 검색
    document.getElementById(id) : id로 검색
    document.getElementsByTagName(name) : 태그로 검색(반환값 : 배열)
    document.getElementsByClassName(name) : class 이르믕로 찾기(반환값 : 배열)
    document.querySelector(css selector) : CSS Selector로 첫번째 요소 검색
    ducument.querySelectorAll(css selector) : CSS Selector로 전체 검색

#### 검색된 HTML 요소 확인/수정
    element.innerText = new html content : 요소 내용 확인/수정(태그 미포함)
    element.innerHTML = new html content : 요소 내용 확인/수정(태그 포함)
    element.attribute = new value : 요소의 attribute값 수정
    element.style.property = new style : 요소의 CSS 프로퍼티 값 수정
    element.setAttribute(attribute,value) : 요소의 attribute 값 설정
* 메서드로 신규 attribute 설정 또는 기존 attribute 수정 가능

#### HTML요소 생성/추가하기
    document.createElement(tagName) : HTML 요소 생성
    document.appendChild(element) : HTML 요소 추가

#### HTML 요소 삭제/대체하기
    document.removeChild(element) : HTML 요소 삭제
    document.replaceChild(new,old) : HTML 요소 대체

#### HTML 요소 탐색
    element.parentNode : 부모 요소
    element.nextElementSibling : 현재 요소의 다음 형제 요소
    element.previousElementSibling : 현재 요소의 이전 형제 요소
    element.children : 자식 요소 (배열 형태)

## 이벤트
: 웹페이지에 발생하는 이벤트를 의미<br>

    이벤트 이름         설명
    load                로드 완료
    resize              윈도우 크기 변경
    keydown             키 입력
    keyup               키에서 손을 떼었을때
    change              변동이 있을떄
    click               클릭
    focus               포커스를 얻었을때
    mousedown           마우스 클릭
    mouseout            마우스가 객체 밖으로 나갔을경우
    mouseover           마우스가 객체 위로 올려졌을때
    mousemove           마우스가 움직였을때
    mouseup             마우스에서 손을 뗐을 때
    select              option 태그 등에서 선택을 했을 때

### 이벤트 등록 
* addEventListener()를 통해 이벤트 등록
> HTML과 JS의 역할을 분리하는 차원에서 onclick과 같이 태그의 속성으로 특정이벤트를 추가하는 방식을 지양한다.

```js
EventTarget.addEventListner(event type, function name)
```
### 이벤트를 통해 DOM 제어
* function에 dom제어함수를 정의하여 이벤트 발생시 DOM 제어 

### 이벤트 삭제
* removeEventListner()를 통해 이벤트 삭제
    - addEventListner와 동일한 양식 사용

#### JQuery
* Vanila JS 함수보다 손쉽게 사용이 가능
* 라이브러리 로드가 필요하고 사이즈가 방대하여 최근에는 사용하지 않는 추세
* $표시와 축약어를 통해 DOM 제어