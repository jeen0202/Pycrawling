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

# Flask Backend Server와 Gunicorn 설정

## Flask server를 위한 Dockerfile 작성
``` docker
FROM python:3.9-alpine

WORKDIR usr/src/flask_app  
COPY requirements.txt . # 현재폴더에 requirements 파일 복사
RUN pip install -r requirements.txt # 파일에 작성되어있는 라이브러리 설치
COPY ./flask_app .
```
+ requirements.txt
```
flask
gunicorn
```
## docker-compose.yml에 Container 추가
``` yaml
  flask:
    build : ./flask_docker
    restart : always
    container_name : myflask
    command : gunicorn -w -2 -b 0.0.0.0:80 wsgi:server
```

## wsgi 실행을 위한 python 코드
1. wsgi.py
  + wsgi 프로그램 실행
  + 80번 포트 + 별고 고정ip없이 실행
  ``` python
  from app import server
  if __name__ =="__main__":
    server.run(host="0.0.0.0", port=80)
  ```
2. app.py
  + flask 객체를 server로 작성하고,
  + /seach 경로 요청시, 메시지 리턴
  ```python
  from flask import Flask

  server = Flask(__name__)

  @server.route('/search')
  def hello_world() :
    return 'hello Elasticsearch6'
  ```
## docker-compose.yml 수정
+ image 빌드를 위해, 경로명 작성
+ gunicorn 실행
  + wsgi.py에서 server안에 있는 flask 객체 선택
  + 주 옵션
    + -b IP_포트 : 바인딩ㅎ할 ip와 포트 설정
    + -w 숫자 : worker 프로세스 개수 지정
  ```yaml
    flask : 
      build : ./flask_docker
      restart: always
      container_name : myflask
      command: gunicorn -w 2 -b 0.0.0.0:80 wsgi:server
      # 테스트를 위해 certbot command 수정
      certbot : 
      ...
      ...
        command : --keep-until-expiring
  ```