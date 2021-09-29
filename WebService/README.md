실제 활용 가능한 Website 작성
=====

Website 구성
--------
+ docker compose로  nginx+mysql+wordpress 활용
+ nginx reverse proxy를 활용하여 내부 nginx 서버와 wordpress 서버 연결
+ Workpress로 Blog 구현, nginx로 Backend 구현, DB server 구현
+ 보안을 위해 https 서비스 지원

> **참고 : Wordpress** <br>
> 개인 블로그를 위한 웹페이지 구성을 위해 가장 많이 사용되는 서버

### 1. wordpress docker 구축
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
### 2. 하부폴더 생성후 nginx.conf 작성
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
### 3. Wordpress bash에 접속하여 폴더 변경
``` bash
mkdir blog
mv * blog
```

### 4. wordpress 설치 주소 접속

탄력적IP주소/blog/wp-adming/install.php

volume 상세 관리 및 설정
--------
+ 특정 호스트PC와 연결하지 않고, 컨테이너 삭제시에도 volume을 유지하고 싶을 경우<br>
  docker-compose.yml 파일 내에서 volumes 설정을 해주는 것으로 해결 가능
```yaml
이름:Container내부경로

volumes:
  이름:
  이름:
```

+ volume 조회 명령
``` docker
docker volume ls # 볼름 조회
docker volume inspect 볼륨이름 # 상세 조회
```

+ volume 삭제 명령
``` docker
docker volume rm 볼륨이름 # 특정 볼륨 삭제
docker volume prune # 미사용 볼륨 삭제
```
> 사용중인 volume은 삭제되지 않는다.

### docker-compose.yml 개선
+ volume을 사용하여 보존/유지보수 되어야 할 폴더 설정
+ 사용자 지정 volume사용시 최하단에 volmue 이름 기재 필요
``` yaml
version: "3"

services:
  nginxproxy:
    depends_on:
      - nginx
      - db
      - wordpress
    image: nginx:latest
    container_name: proxy # exec 편의를 위해 이름 지정
    ports:
      - "80:80"
    restart: always
    volumes:
      - "./nginx/nginx.conf:/etc/nginx/nginx.conf" # file COPY 명령 대체

  nginx:
    image: nginx:latest
    container_name: myweb # exec 편의를 위해 이름 지정
    restart: always
    volumes:
      - "./myweb:/usr/share/nginx/html" # folder 연결

  db:
    image: mysql:5.7
    container_name: mysqldb # exec 편의를 위해 이름 지정
    volumes:
      - "mydb:/var/lib/mysql" # volume이름 지정하고, 할당
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:
    depends_on:
      - db
    build: # wordpress 동작을 위해 image를 따로 생성
      context: ./wp
      dockerfile: Dockerfile
    container_name: wp # exec 편의를 위해 이름 설정
    restart: always
    volumes:
      - "./html:/var/www/html"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

volumes: # 사용자 지정 볼륨 설정
  mydb:

```

### root 폴더에 wp 폴더 생성
``` bash
mkdir wp
```
### wordpress Dockerfile 작성
+ wordpress 최초 실행시의 원활한 작업을 위한 설정을 Dockerfile로 작성
``` dockerfile
FROM wordpress:5.7.0

RUN mkdir -p /usr/src/blog
RUN mkdir -p /usr/src/blog/wp-content/plugins
RUN mkdir -p /usr/src/blog/wp-content/uploads
RUN cp -rf /usr/src/wordpress/* /usr/src/blog
RUN mv /usr/src/blog /usr/src/wordpress/
RUN chown -R www-data:www-data /usr/src/wordpress # wordpress에 소유권한 부여
RUN find /usr/src/wordpress/blog/ -type d -exec chmod 0755 {} \; # 폴더를 찾아서 권한부여
RUN find /usr/src/wordpress/blog/ -type f -exec chmod 644 {} \; # 파일을 찾아서 권한부여
```

> 실행전에 하위폴더, 실행중인 container, 사용중인 volume이 없어야 한다.

**참고 wp-confing.php**<br/>
+ 웹상에서 플러그인과 테마 설치를 진행하기 위해 필요함

### wp-config.php 설정 추가 및 volume에 복사
> Container 최초 실행 이후에 생성되는 설정파일 wp-config.php은 직접 복사하는것이 편리하다.

+ wordpress docker 접속
``` bash
docker exec -it wp /bin/bash
```
+ wp-config.php 파일에 define line 추가
``` php

@package WordPress
define('FS_METHOD', 'direce');
```

+ blog 폴더에 복사 후 종료
``` bash
cp wp-config.php blog/
exit
```
# 서버에 접속하여 test
접속 주소 :
  + http://탄력적IP/blog/wp-admin/install.php