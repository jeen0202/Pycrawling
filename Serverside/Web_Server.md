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