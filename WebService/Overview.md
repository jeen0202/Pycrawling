최종 Docker compose
------------

# Docker 구성
+ reverse proxy
+ Web(html/css/js) frontend server 
+ Flask Backend Server
+ Wordpress blog service
+ php service
+ Mysql Database service
+ Certbot https support

# 운영 방법
+ Web폴더의 변경사항 Frontend Server에 즉시 반영
+ Flask 코드 수정시 아래 명령으로 재실행 하여 반영
``` bash
docker-compose up -d --force-recreate --no-deps --build flask
```
+ crontab을 활용한 https인증서 자동 갱신
+ 모든 Container에 ```restart:always``` 옵션으로 안정성 개선

# 향후 DevOps 계획
> 다중 서버 동시동작과 무중단 배포가 가능하도록 구성

+ Python을 사용한 docker/server 설정 자동화
+ Cubernetes
+ 무중단 배포
