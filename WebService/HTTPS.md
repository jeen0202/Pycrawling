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