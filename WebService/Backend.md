Flask Backend Support
-----
+ nginx reverse proxy 구성
+ Frontend Support를 위한 내부 nginx server 구성
+ Wordpress 지원을 위한 Wordpress server(/blog) 구성
+ Flask Backend Support 및 성능 개선을 위한 gunicorn 프로그램을 활용항 server(/util) 구성

# Web Server와 WSGI의 이해

## Web server와 WAS Framework
+ Web server는 static한 Webpage를 반환.
  + request에 따른 static data 반환
  + 주요한 Web server로는 Apache, nginx가 있음
+ Data의 Dynamic한 반환을 위해서는 WAS(Web Applicatino Service) FrameWork필요 
  + 주요 WAS FrameWork 
    + flask(Python)
    + django(Python)
    + rails(Ruby)
    + node.js(JavaScript)
## WAS Framework
+ Web server 위에서 동작하는 Server 응용 프로그램
+ Framework를 사용하여 WAS 개발이 가능하다.

## WSGI
+ Web Server Gateway Interface
+ Python Script(응용 프로그램)이 웹 서버와 통신할 수 있도록 하는 프로토콜
  + WSGI for Python
+ 주요 기능
  + Web server의 환경 정보와 Callback 함수를 파이썬 스크립트에 전달해주는 기능
  + Request 처리결과를 Callback을 통해 Web server로 전달해주는 역할

## Middleware
+ WSGI의 동작을 지원하는 프로그램
+ 주요 기능
  + 응용 프로그램 실행 (응용 프로그램 Container)
  + Web Server의 환경 정보 변경시 이에 상응하는 요청 경로 변경
  + 동일 프로세스 상에서 여러 응용 프로그램 실행 지원
  + XSLT stylesheet 적용등의 전처리 지원
+ 주요 middleware
  +  mod_wsgi : apache의 플러그인으로 구현된 WSGI Middleware
  +  uwsgi : C언어로 작성된 WSGI Middleware
  +  gunicorn : python 언어로 작성된 WSGI Middleware

## 정리
+ 파이썬 응용 프로그램을 Web server 상단에서 실행시킬 수 있도록 하기위해, WGSI라는 프로토콜을 만들고, 여기에 편의성을 더한 기능을 추가한 WSGI Middleware가 존재한다.
+ Web server와 WSGI 동작 방식
  1. Web server에서 설정에 따라 특정 port를 listen
  2. Request 발생시 Web server가 Thread를 생성하여 해당 request 처리
     1. 해당 Thread는 WSGI Middleware를 통해 파이썬 응용 프로그램에 요청 전달
     2. Python 응용 프로그램이 요청을 처리해서 다시 WSGI Middleware에 전달
  3. WSGI Middleware가 Web server Thread에 해당 요청 처리 결과 전달
> nginx proxy(Web server), gunicore(WSGI Middleware)사용하여 요청을 처리하도록 구성<br>
>기존에는 uwsgi를 많이 사용하였지만, uwsgi가 무겁고, resource 사용량이 많아<br> 
>이를 고려하여 gunicorn을 사용