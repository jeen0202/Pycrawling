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
* rowspan : tr 태그에 사용하여 행을 확장<br>

**```<form>```**

input, sumit과 같은 태그들과 같이 사용되며, 사용자의 입력을 받는 태그

주요 속성
* action : 입력 받은 데이터를 처리할 URL
* method : HTTP Method (post, get)
* target : 링크된 URL 이동방법 (_self : 현재창, _blank : 새창)

**```<input>```**

사용자의 데이터를 입력받는 주요 태그<br>
속성
* type : 입력 받는 인터페이스 설정 (button,checkbox,email,radio ...)
* maxlength : 입력 문자열 최대 길이
* minlength : 입력 문자열 최소 길이
* autofocus : 페이지 로드시 해당 태그에 커서가 자동으로 놓이도록
* autocomplete : 자동완성 기능 설정

## Semantic Web
웹 페이지 각요소에 의미를 부해서, 의미와 관련성을 기반으로 진보된 검색, 서비스를 가능토록 하는 시도<br>

관련 태그
* header, nav, aside, section, article, footer
* 하나하나의 태그는 의미가 없지만 CSS를 적용하여 분리 가능

### 참고 사항
* 웹 표준 : WWW(World Wide Web)의 측면을 정의, 서술하는 공식 기술 규격
    * W3C(World Wide Web Consortium) 권고안에 따라 정의된 웹 표준
    * HTML 버전에 따라 deprecated(추후 미지원) 되는 태그 및 속성이 존재
* 웹 접근성
    * 이미지 태그에 대체 택스트, 영상 자막, 키보드로 접근 가능 등등 환경적 제한이 있는 사용자를 고려하여 웹 페이지를 작성하는 기법
    * 인증마크도 있으나, 현실적으로 구현은 어려움
* 크로스 브라우징 : 다양한 웹 브라우저상에서 동일한 사용자 경험을 위한 기술
    * MS사의 IE가 문제의 소지가 가장 많으므로, 해당 브라우저만 간단히 고려

## 이미지
Bitmap, Vector Image로 구분

* Bitmap : 픽셀단위로 색 정보를 가진 데이터(.jpeg .jpg, .png, .gif)
    * 정교하고 다양한 색상 적용 가능
    * 확대, 축소시 이미지가 깨짐
* Vector : 수학 정보로 모양 정보를 가진 데이터 (.svg)
    * 확대, 축소시에도 이미지가 깨지지 않음

### JPEG(JPG)
: 높은 압축률

* 24bit, 고해상도 이미지 가능
* 이미지 품질과 용량 조정 가능
* 손실 압축(원본 이미지와 다른 정보)
### GIF
: 동영상, 짧은영상과 같은 이미지 가능

* 8Bit 색상만 지원
* 비손실 압축(원본 이지미와 동일 정보)

### PNG
: 투명도 지원이 되는 GIF 대체 포맷

* W3C 권장 이미지 포맷
* 동영상등은 지원되지 않음
* 24Bit, 고해상도 이미지 가능
* 비손실 압축(원본 이미지와 동일 정보), 상대적으로 파일 사이즈가 큼

### WEBP
: 동영상, 투명도 지원이 모두 되는 대체 포맷

* Google에서 개발
* 일부 브라우저 미지원
* 손실/비손실 압축 모두 지원