# Web Server
+ HTTP Request에 응답하기 위해 동작
+ 서버 프로그램을 Server에 설치하여, Request에 따라, 서비스를 제공해주는 방식으로 서비스 구현
+ 서버 프로그램으로 apache와 nginx가 많이 쓰이고있음

## Apache
+ 오픈 소스 원칙을 지키고있는 서버 프로그램
+ 전통적으로 많이 사용된 프로그램

### Apache 구동 방식
+ 2가지 방식 지원
    + Prefork Multi Process Module(MPM) 방식
        + Request가 올 때마다, process를 복제하여, 별도 process에서 Request 처리
    + Worker MPM 방식
        + 1개의 HTTP Request 연결후, 복제된 process내에서 Thread를 생성하여 요청 처리

## Nginx
+ 가벼움과 높은 성능을 목표로하는 서버 프로그램
+ Async Event 구조를 가진다.

### Nginx 구동 방식
+ Event Driven 방식
    + 1개의 Process가 동작하면서, HTTP Request를 Event로 비동기식(async)로 처리
        + 대부분이 IO 작업인 HTTP Response를 event에 포워딩하고, 요청작업이 끝난 순으로 처리
    + 매번 Request가 전달될때마다, Proecess/Thread의 생성이 필요없으므로, 자원 관리에 장점이 있음
    + 접속자가 많을 경우 Apache보다는 Nginx가 성능이 좋을 수 있음

> Web Server는 다양한 추가 기능과 함께 동작하기 때문에, 종합적인 성능에서는 큰 차이가 없다고 생각하는게 좋다.

### Nginx 기본 사용법
> 설정은 서버 프로그램 버전/리눅스 패키지 마다 그 방법이 매우 다르기 때문에 참고용으로만 사용
> (ubuntu 20.04, nginx 1.18.0 기준)
**ubuntu 20.04 버전의 container 생성 후 bash로 연결**
``` bash
docker run -dit -p 80:8080 --name myos ubuntu:20.04
docker exec -it myos /bin/bash
```
**Container의 bash에서 nginx와 vim에디터 설치**
``` bash
apt-get update
apt-get install nginx=1.18.0-0ubuntu1.2 # 6 asia 69 seoul
apt-get install vim
```


## nginx.conf
+ conf 파일 접근
``` bash
find -name nginx.conf
vim /etc/nginx/nginx.conf
```
+ nginx 웹 서버 기본 설정 파일
+ user, worker_processes, pid, events, http Block으로 구분된다.
+ Block 정보
    |Block이름|용도|
    |----|------|
    |user|사용자 이름/ID|
    |worker_processes|생성되는 Process 개수정보|
    |pid|system과의 연결설정|
    |include|포함할 설정파일|
    |events|async로 처리되는 event관련 부분|
    |http|웹서버 기본 설정|


**참고 사함**
> nginx의 설치 방법에 따라, 설정 파일의 위치가 다를 수 있다. 

### default에서의 Server 설정
|Name|Desc|
|---|-----|
|listen|HTTP Request를 받을 Port|
|default_server|모든 웹서버 Request를 받는다는 명시적 표시|
|2열의 listen|IPv6 포트 설정|
|root|html파일의 경로|
|server_name|Request를 받을 Domain name|
|location|주소에 따라 응답하기 위한 경로설정을 위한 설정|

> 설정 변경후 아래 Command를 사용해 nginx restart
``` bash
service nginx restart
```

## nginx reverse proxy

### Proxy Server
 : Client가 다른 네트워크 서비스에 접속할수 있게 만들어 주는 서버

### Forward Proxy
 : Client가 외부 네트워크에 직접 접근하지 않고, Proxy에 접근 요청을 하고, Proxy Server가 외부에 대신 접속하여 Client에 전달하는 서버

 > 클라이언트가 자주 접속하는 외부서비스 관련 데이터를 캐시에 저장하여 성능 향상에 기여한다.

### Reverse Proxy
 : Client가 Reverse Proxy에 요청하여, Proxy Server 내부 서버에 접속하여 결과를 Client에 전달하는 서버
> 내부 DB와 같이 보안이 중요한 서버에 대한 직접 접속을 막을 수 있어 보안에 유익하다.
> 요청 트래픽 관리를위한 Load Balancing 등에 유익함


### Nginx reverse proxy 01 : Port로 구분
+ nginx reverse proxy 서버에 Port를 2개 open하여, 각 내부서버에서 결과를 가져오도록 구성
    + 내부 서버는 또다른 web server(nginx/apache)로 구성
    + Docker Compose 파일
    ```yaml
    version: "3"
    # 3개의 Container를 포함하는 서비스
    services:
        #2개의 open port를 가지고 있는 nginx 서버     
        nginxproxy:
            image: nginx:1.18.0
            ports:
                - "8080:8080"
                - "8081:8081"
            restart: always
            volumes:
                - "./nginx/nginx.conf:/etc/nginx/nginx.conf"

        #외부에 open된 port가 없는 nginx 서버
        nginx:
            depends_on:
                - nginxproxy
            image: nginx:1.18.0
            restart: always

        #외부에 open된 port가 없는 apache 서버
        apache:
            depends_on:
                - nginxproxy
            image: httpd:2.4.46
            restart: always
    ```
    + nginx.conf 파일
        + upstream, server 설정 추가
        + default.conf 설정과 겹치지 않도록 함
    ``` conf
        user nginx;
    worker_processes  auto;

    error_log  /var/log/nginx/error.log warn;
    pid        /var/run/nginx.pid;

    events { 
        worker_connections 1024; 
    }

    http {
        # data type에 따라 적절한 동작을 하기 위한 설정 
        include       /etc/nginx/mime.types;
        # 기재되어있지 않는 type에 대해서는 표준포맷을 적용
        default_type  application/octet-stream;
        # log에 기재되는 값을 지정
        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';
        # 접속 기록
        access_log  /var/log/nginx/access.log  main;
        # Reponse 시 user 영역의 buffer가 아닌 kernel file buffer를 사용
        sendfile on;
        keepalive_timeout 65;
        #container의 내부 통신을 위해 port 설정
        upstream docker-nginx {
            server nginx:80;
        }
        #container의 내부 통신을 위해 port 설정
        upstream docker-apache {
            server apache:80;
        }

        server {
            # port에 
            listen 8080;

            location / {
                #upstream에서 지정한 이름(port)에 포워딩
                proxy_pass         http://docker-nginx;
                proxy_redirect     off;
                proxy_set_header   Host $host;
                proxy_set_header   X-Real-IP $remote_addr;
                proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Host $server_name;
            }
        }

        server {
            listen 8081;

            location / {
                #upstream에서 지정한 이름(port)에 포워딩
                proxy_pass         http://docker-apache;
                proxy_redirect     off;
                proxy_set_header   Host $host;
                proxy_set_header   X-Real-IP $remote_addr;
                proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Host $server_name;
            }
        }
    }
    ```
**참고 사항 : Nginx proxy HTTP 설정 이해**
 + reserved proxy와 내부 서버 사이에 http 통신을 하면, 외부 클라이언트 정보가 누락되어 이상 동작을 할 수 있음
 + proxy header에 정보를 기입하여 이상 동작을 방지 
 ``` conf
proxy_set_header   Host $host;
proxy_redirect     off; # 서버 응답 헤더의 주소 변경 
proxy_set_header   X-Real-IP $remote_addr; # 실제 Client의 ip
proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for; # proxy 거쳐온 server ip 리스트
proxy_set_header   X-Forwarded-Host $server_name; # Client host 이름
proxy_set-header   X-Forwarded-Proto $scheme; # Client와 reserved proxy 접속시 사용한 프로토콜 설정
 ```


### Nginx reverse proxy 02 : 경로로 구분

+ docker-compose.yml ports 경로 제한
    ``` yaml
    services:
        nginxproxy:
            image: nginx:1.18.0
            ports:
                - "80:80"
            volumes:
                - "./nginx/nginx.conf:/etc/nginx/nginx.conf"
    ```
+ nginx.conf 파일 설정 변경
    ``` conf
    server {
        listen 80:

        location /blog {
            nginx 설정
        }
        
        location /community {
            apache 설정
        }
    }
    ```
+ docker-nginx 설정 변경
  + nginx Container 접속
    ``` bash
    docker exec [nginx Container이름] /bin/bash
    ```
  + Container 내부에서 설정파일을 찾아 변경
    ``` bash
    cd /usr/share/nginx/html/
    mkdir blog # 하부 폴더 생성
    ```

+ docker-apache 설정 변경
  + apche Container에 접속
    ``` bash
    docker exec [apahce Container 이름] /bin/bash
    ```
  + httpd.conf 에서 root 경로 확인
    ``` bash
    cd conf/
    vim httpd.conf # Server root 파악
    cd /usr/local/apache2/htdocs
    ``` 
  + root에 하부폴더 생성하여 연결
    ``` bash
    mkdir community
    vim test.html
    ``` 