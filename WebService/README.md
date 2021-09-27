# 실제 활용 가능한 Website 작성

## Website 구성
+ docker compose로  nginx+mysql+wordpress 활용
+ nginx reverse proxy를 활용하여 내부 nginx 서버와 wordpress 서버 연결
+ Workpress로 Blog 구현, nginx로 Backend 구현, DB server 구현
+ 보안을 위해 https 서비스 지원

> **참고 : Wordpress** <br>
> 개인 블로그를 위한 웹페이지 구성을 위해 가장 많이 사용되는 서버

### wordpress docker 구축
``` yaml

version: "3"

services:
  nginxproxy: # proxy 서버 설정
    depends_on: # 다른 서버들이 실행된 이후에 실행
      - nginx
      - db
      - wordpress
    image: nginx:latest
    ports: # 외부에 port open
      - "80:80"
    restart: always
    volumes: # 포위딩을 위해 volume 설정
      - "./nginx/nginx.conf:/etc/nginx/nginx.conf"

  nginx: # 웹 서버
    image: nginx:latest
    restart: always

  db: # DB 서버
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress: # wordpress 서버
    depends_on:
      - db # db가 실행되면 실행
    image: wordpress:5.7.0
    ports: # 테스트를 위해 open
      - "8080:80"
    restart: always
    environment: # db와의 연결을 위한 환경변수 설정
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
```
### 하부폴더 생성후 nginx.conf 작성
``` conf
user nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events { 
    worker_connections 1024; 
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" "$request_uri" "$uri"'
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;    
    sendfile on;
    keepalive_timeout 65;

    upstream docker-wordpress {
        server wordpress:80;
    }

    upstream docker-web {
        server nginx:80;
    }

    server {
        location /blog/ {
            #포워딩시 내부경로를 없애버릴 경우 경로간 간섭이 생길수있기때문에 rewrite 옵션을 사용하지 않는다.
            #rewrite ^/blog(.*)$ $1 break; 
            proxy_pass         http://docker-wordpress;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
        }
        
        location / {
            proxy_pass         http://docker-web;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
        }
    }
}
```
### Wordpress bash에 접속하여 폴더 변경
``` bash
mkdir blog
mv * blog
```

### wordpress 설치 주소 접속
