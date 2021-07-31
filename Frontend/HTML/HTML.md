# HTML의 이해
기본 html 문법 : html5

## DOCTYPE
```html
<!doctype html>
```
해당문서가 HTML 문서임을 알려주는 태그

## HTML
```html
<html lang='ko'>
```
실제 HTML 문서 범위 설텅 태그
- lang : 문서 언서 설정 (ko,en ...)

## HEAD와 BODY
```html
<head>
</head>
<body>
</body>
```
html 문서는 ```<head>``` 와 ```<body>``` 태그로 이루어짐

* head 태그 내부는 html문서 전체를 대표하거나, html문서 전체에서 필요한 데이터를 넣는다.
    - 주요태그
        - title : html문서의 제목, 웹 브라우저 상단에 표기
        - meta : html 문서 전체를 대표하는 정보
* body 태그안에는 html문서에 표시되는 내용을 넣는다.

## META
```html
<meta>
```
문서 전반에 걸친 정보를 표시하기 위한 설정

* charset : 문자 인코딩 설정 (utf-8,euc-kr)
* name : 메타 정보 이름 (author : 저자이름, description : 문서 설명...)

## 주요 meta name 값
### 호환성 관련 태그
```html
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```
IE에서 최신 표준 모드로 렌더링 되도록 하는 설정
IE의 호환성 이슈를 해결하기 위해 HTML문서에 포함되는 것이 좋음

### 반응형 웹 관련 태그
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
**viewport**
화면에 보여지고 있는 직사각형 영역, 웹브라우저 상의 문서를 볼수있는 전체화면
**meta viewport 설정**

- width : 초기 너비 (device-width또는 양의 정수)
- user-scalable : 웹페이지 확대 허용 여부 

## LINK
```html
<link rel='stylesheet' href='style.css'>
<link rel='icon' href='favicon.png'>
```
html 문서에 필요한 외부 데이터를 가져오기 위해 사용
주로 css파일과 icon파일을 가져오기 위해 사용
* rel : html와 외부 데이터와의 관계(stylesheet, icon ...)
* href : 외부 데이터파일의 위치 지정(파일의 상대경로, 절대경로)

## STYLE
```html
<style>
```
css 코드를 html문서 내에서 작성할 때 사용

## SCRIPT

JS코드를 html문서 내부에서 작성할 때 사용

JS코드는 파일 형태로 link태그를 사용해 가져오거나, script 태그를 사용해 직접 문서에 삽입하는 방식으로 적용 가능

<<<<<<< HEAD
기존에는 ```<script type="text/javascrpit">```라고 작성하였으나<br>
html5에서는 ```<script>```라고만 작성하면 된다.

## Body내부의 주요 태그
**```<h1>~<h6>```**<br>

제목 태그로 제목 폰트 사이즈 차이가 존재한다.<br>

> ```현업에서는 웹브라우저 호환성을 위해, 태그의 표현서식을 모두 삭제하고 css를 별도로 적용한다.```

**```<p>```**

문단을 표시하는 태그

**```<a>```**

하이퍼링크를 표시하는 태그<br>

* ```href```속성을 통해 링크 연결
* ```target```속성을 사용하여 URL이동방법 지정
    - _self : 현재 브라우저에서 이동
    - _blank : 새창으로 이동<br>

**```<ol>,<ul>,<li>```**<br>

리스트 관련 태그로 모던웹에서 많이 사용

* ```<ol>``` : 순서가 있는 리스트
* ```<ul>``` : 순서가 없는 리스트
* ```<li>``` : 리스트 아이템<br>

**```<img>```**<br>

이미지 삽입 태그<br>

주요 속성

* src : 이미지 파일의 위치
* alt : 이미지 대체 텍스트

> ```alt는 웹접근성을 높이는 필수 속성으로 다루는것을 권장함```
 
 **```<div>```**

 division의 약자로 html 문서의 특정 부분을 지정하는데 사용<br>
 모던 웹에서 css또는 JS로 html의 특정 부분을 제어할 때 사용

 **```<table>```**

 테이블을 작성하기 위해 사용되는 태그
 * ```<thead>``` : 제목으로 구성된 열들을 가진 행을 표시
 * ```<th>``` : 제목으로 구성된 각 열을 표시
 * ```<tbody>``` : 표의 내용을 나타내는 행들을 표시
 * ```<tr>``` : 표의 내용들을 나타내는 각 행들을 표시
 * ```<td>``` : 표의 내용을 나타내는 각 열들을 표시
 * ```<tfoot>``` : 표의 마지막 행을 표시
 > ```thead``` ```tfoot```태그는 표에서 한번도 안나오거나 한번만 나와야 함
 > ```tfoot```은 ```thead``` 보다 뒤에 위치해야 함
 속성
 * colspan : td 태그에 사용하여 열을 확장
 * rowspan : tr 태그에 사용하여 행을 확장
=======
기존에는 ```<script type="text/javascrpit">```라고 작성하였으나
html5에서는 ```<script>```라고만 작성하면 된다.
>>>>>>> c888d6655da690a90164db0c5d400ef82108408f
