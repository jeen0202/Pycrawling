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

기존에는 ```<script type="text/javascrpit">```라고 작성하였으나
html5에서는 ```<script>```라고만 작성하면 된다.
