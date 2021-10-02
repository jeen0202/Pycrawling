HTTPS 서비스
----
+ 최근 검색엔진은 보안강화를 위해 https를 지원하는 사이트를 우선 지원함
+ https를 지원하기 위해서는 인증서 발급이 필요하며, 연단위 비용이 청구됨

## Let's Encrypt와 certbot
+ 연단위 비용없이  http 인증서를 발급해주는 서비스
+ 90일 마다 갱신필요

## Let's Encrypt SSl 인증서 발급 명령 예시
+ 제공된 cerbot 프로그램에 옵션을 추가하여 인증서 발급
```
certbot certonly --cert-name cert --standalone -d domain.com,www.comain.com
```

## 테스트를 위한 사전 준비
> 테스트를 위해서는 고정 IP와 domain이 필요함.

### 1. domain 서비스 구입
+ 가비아(www.gabia.com) 이용
+ DNS 레코드에 고정IP 설정

### 2. certbot과  nginx 기본 설정
+ certonly 옵션
``` bash
certbot certonly --dry-run --webroiot --webroot-path=/usr/share/nginx/html --email test@test.com --agree-tos --no-eff-email --keep-until-expireing -d janjan-codong.site -d www.janjan-coding.site
```
+ certbot certonly : certonly는 certbot 프로그램의 플러그인으로 인증서를 받는 서브 명령
    + certbot/certbot image는 entrypoint가 certbot이기때문에, command certonly부터 작성한다.
    + certonly는 신규/갱신된 인증서를 받기만 하며, ```--webroot```를 함께사용해 알맞은 위치에 인증서를 설치
+ **--dry-run: 테스트시에 반드시 사용해야한다. 해당 옵션 없이 여러차례 테스트를 시행할 경우 에러 발생**
+ --webroot : 내 서버에 인증 정보를 입력하고, 이를 기반으로 인증서를 발급받겠다는 옵션(갱신을 위해 서버를 끌 필요가 없음)
+ --webroot-path : 인증 정보를 넣을 내 서버의 폴더 path 지정
+ --email : 인증서 복구를 위한 이메일 계정 등록
+ --agree-tos : ACME 서버 구독 동의
+ --no-eff-email : 이메일 주소 공유 거부
+ --keep-until-expiring : renew가 필요하지 않으면, 기존 인증서를 보존

### 참고: 433 Port
> HTTPS 테스트를 위해 ec2에서 443 port의 접근을 승인해야 한다.


### docker-compose.yml 코드
```yaml
version : "3"

services:
  webserver: # proxy server
    image: nginx:latest
    container_name : proxy
    restart : always
    ports:
      - "80:80"
      - "443:443" # https test를 위한 port open
    volumes :
      - ./myweb:/usr/share/nginx/html
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./certbot-etc:/etc/letsencrypt # volume 공유를 통해 인증 정보 공유

  nginx : # web server/ http로 통신
    image : nginx:latest
    container_name : myweb
    restart : always
    volumes : 
      - ./myweb:/user/share/nginx/html

  cerbot: # certbot container
    depends_on:
      - webserver # webroot option 충족을위해 webserver 동작 이후 동작
    image: certbot/certbot
    container_name : certbot
    volumes:
      - ./certbot-etc:/etc/letsencrypt
      - ./myweb:/usr/share/nginx/html
    command : certonly --dry-run --webroot --webroot-path=/usr/share/nginx/html --email test@test.com --agree-tos --noeff-email --keep-until-expiring -d janjan-coding.site -d www.janjan-coding.site
```
### nginx.conf code
```
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

    upstream docker-web {
        server nginx:80;
    }

    server {
        location ~ /.well-known/acme-challenge {
                allow all;
                root /usr/share/nginx/html;
                try_files $uri =404;
        }

        location / {
                allow all;
                root /usr/share/nginx/html;
                try_files $uri =404;
        }
    }
}

```

## 3. compose 실행 및 확인
``` bash
docker compose up -d
docker logs certbot
ping 사이트주소
```

> --dry-run 옵션을 제거하면 실제 인증서를 발급 받을 수 있다.

### 인증서 파일 확인 (실제, 인증서 발급후)

## 4. nginx.conf 재설정

``` conf
    server {
        listen 80; # 영구적인 redirection
        server_name fun-coding.xyz www.fun-coding.xyz;

        location ~ /.well-known/acme-challenge {
                allow all;
                root /usr/share/nginx/html;
                try_files $uri =404;
        }

        location / {
                return 301 https://$host$request_uri;
        }    
    }
     server {
        listen 443 ssl; ## 보안을 위해 443port에서 ssl 프로토콜 처리
        server_name fun-coding.xyz www.fun-coding.xyz;
        
        ssl_certificate /etc/letsencrypt/live/fun-coding.xyz/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/janjan-coding.site/privkey.pem;
        include /etc/letsencrypt/options-ssl-nginx.conf; # 보안 강화를 위한 옵션 추가
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;   # 보안 강화를 위한 옵션 추가

        location / {
            proxy_pass         http://docker-web;       # docker-web 컨테이너로 포워딩
            proxy_redirect     off;                     # 서버 응답 헤더의 주소 변경 (불필요)
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
	    proxy_set_header   X-Forwarded-Proto $scheme;
        }
    }
```

## 5. 보안 옵션 개선을 위한 파일 다운로드
> certbot-etc 폴더에 options-ssl-nginx.conf 와 ssl-dhparams.pem을 다운로드한다.

## 6. docker-compose 실행후 접속하여 확인
``` https://domain 이름```



HTTPS 웹페이지 및 Wordpress 블로그 Service 구현
------
### 필요 Server Container
+ Nginx Proxy server (HTTPS Service)
+ 내부 Nginx Server (Web Service)
+ 내부 wordpress Server (Wordpress)
+ 내부 Dataabse Server (Mysql server)
  + 추가적으로 certbot을 수행하는 Container까지 필요

### 1. 4개의 Server 사용을 위한 설정개선
+ Docker-compose 파일 개선
``` yaml
...

  nginxproxy: # Proxyserver Container
    depends_on:
      - nginx
      - db
      - wordpress
    image: nginx:alpine
    container_name: proxyserver 
    restart: always 
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./certbot-etc:/etc/letsencrypt
      - ./myweb:/usr/share/nginx/html

  nginx: # Web Service Container
    image: nginx:latest
    container_name: mywebserver 
    restart: always
    volumes:
      - ./myweb:/usr/share/nginx/html

  db:
    image: mysql:5.7 # Mysql Server Container
    container_name: mysqldb 
    volumes:
      - mydb:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress: # Wordpress Container
    depends_on:
      - db
    build:
      context: ./wp
      dockerfile: Dockerfile
    container_name: wp
    restart: always
    volumes:
      - ./html:/var/www/html
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

  certbot: # certbot 설정
    depends_on:
      - nginxproxy 
    image: certbot/certbot
    container_name: certbot
    volumes:
      - ./certbot-etc:/etc/letsencrypt
      - ./myweb:/usr/share/nginx/html
    command: certonly --webroot --webroot-path=/usr/share/nginx/html --email jhleeroot@gmail.com --agree-tos --no-eff-email --keep-until-expiring -d [사용자 사이트 주소]

volumes:
  mydb:
```
+ nginx.conf wordpress 추가
``` conf

...

http {

....

    upstream docker-wordpress {
        server wordpress:80;
    }
server {
	listen 80;
	listen [::]:80;


 location /blog/ {           
            proxy_pass         http://docker-wordpress;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
            proxy_set_header   X-Forwarded-Proto $scheme;
        }
```
+ wordpress 폴더 생성 후 dockerfile 작성

``` dockerfile
FROM wordpress:5.7.0

RUN mkdir -p /usr/src/blog
RUN mkdir -p /usr/src/blog/wp-content/plugins
RUN mkdir -p /usr/src/blog/wp-content/uploads
RUN cp -rf /usr/src/wordpress/* /usr/src/blog
RUN mv /usr/src/blog /usr/src/wordpress/
RUN chown -R www-data:www-data /usr/src/wordpress
RUN find /usr/src/wordpress/blog/ -type d -exec chmod 0755 {} \;
RUN find /usr/src/wordpress/blog/ -type f -exec chmod 644 {} \;

```

+ wp Container에 접속하여 설정 수정
``` bash
docker exec -it wp /bin/bash
apt-get update
apt-get install vim
vim wp-config.php
```

``` php
...
@package WordPress
*/

define('FS_METHOD', 'direct');
```
``` bash
cp wp-config.php blog/
```

### 2. Wordpress 접속후 초기 설정
> 접속주소<br/>
> 사용자 주소/blog/wp-admin/install.php

인증서 자동갱신을 위한 crontab 사용법
-----

+ certbot은 인증서 확인후 Conatiner 실행 중지
+ cerrbot Container를 주기적으로 실행하여 인증서 재발급 자동화

+ 1. docker-compose certbot container 설정 변경
  + --keep-until-expiring 옵션을 --force-renewal 옵션으로 변경
  + --dry-run 옵션으로 테스트 후, --force-renewal 적용
``` yaml
  certbot :
    depends_on :
      - nginxproxy
    image : certbot/certbot
    container_name : certbot
    volumes :
      - ./certbot-etc:/etc/letsencrypt
      - ./myweb:/usr/share/nginx/html
    command : certonly --webroot --webroot-path=/usr/share/nginx/html --email jeen0202@korea.ac.kr --agree-tos --no-eff-email -d janjan-coding.site www.janjan-coding.site --force-renewal
```
+ 2. crontab 설정
  + crontab 주요 명령
``` bash
crontab -e # crontab 설정 입력 파일
crontab -l # crontab에 설정 되어있는 내용 확인
```
crontab 설정
```
*       *       *       *       * 
분(~59) 시(~23) 일(31)  월(~12) 요일(~7)
```
+ 예시
  + 특정 시간 실행
  ```
  40 6 * * 1 [실행명령] 
  # 매주 월요일 6시 40분에 실행
  ```
  + 반복 실행
  ```
  0,20,40 * * * * [실행명령]
  # 매일 매시간 0분 20분 40분에 실행
  ``` 
  + 범위 실행
  ```
  10-40 6 * * * [실행명령]
  # 매일 오전 6시10분 부터 40분까지 매분 실행
  ``` 
  + 간격 실행
  ```
  */20 * * * * [실행명령]
  # 매 20분 마다 실행
  ``` 
+ crontab 설정 변경
  + 테스트 코드
  ``` vim
  PATH=/usr/local/bin # 경로 설정
  * * * * * docker-compose -f /home/ubuntu/파일경로/docker-compose.yml restart certbot >> /home/ubuntu/파일경로/cron.log 2>&1
  # 매분 재실행후 cron.log파일에 결과 저장
  ```
  + 설정 변경
  ```
  * * 2 * * docker-compose -f /home/ubuntu/파일경로/docker-compose.yml restart certbot >> /home/ubuntu/파일경로/cron.log 2>&1 
  # 매달 2일마다 재실행
  ```
**참고사항**
> cron.log에 로그가 많이 쌓이면 저장공간 에러가 날 수 있으므로, 주기적으로 삭제 필요