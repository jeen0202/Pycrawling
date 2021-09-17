# Docker
: Container 기반의 가상화 플랫픔. Container에 서버를 셋업한 상태로 유지하여 항상 동일한 서버의 셋업을 도와주는 CI Tool의 역할을 한다.

## Docker의 기술기반
: Docker의 container의 구조는 Linux Container에서 시작되었음

###  Linux Containers(LXC)
+ 리눅스 OS에서, 다른 환경에 분리된 리눅스 시스템을 운영할 수 있는 커널 기술
+ OS Level에서 자원을 분리하여 별도의 시스템을 사용할 수 있도록 해주는 기술
+ Docker의 적용사례
    + Linux Container 생성
    + Container에 내부에 별로로 시스템 설정/실행
> 근래에는 LXC 기술을 응용하지 않고 별도의 Container 기술을 구현하여 동작됨

## Docker 주요 Elements

### Docker Engine
+ Docker는 Server/Clinet 구조
    + Server는 Docker daemon process 형태로 동작
    + Docker에서는 RestAPI를 사용하여 Docker daemon process와 통신
    + Docker command : Client와 같이 Server에 요청을 전송하는 역할을 수행
        + Docker command를 실행하여, 내부적 RestAPI를 통해 Docker daemon process를 호출
        + 각 Docker command는 주소를 가지고 있어서 openAPI를 호출하는것 처럼 명령을 실행하는것이 가능
### Docker Image
+ Docker Container 생성을 위한 명령을 보유하고 있는 Template
+ 여러 이미지를 쌓아올린 Layer로 원하는 형태의 이미지를 만들어 냄
### Docker Container
+ LXC 형태로 실행된 상태인 Docker Image를 의미
+ daemon 내부 커널에서 lxc로 container를 생성한 뒤, 해당 container에 docker image가 포함된 명령을 실행하여 docker container를 생성/실행
+ container는 분리된 공강이므로, docker daemon process를 통해 접속 가능하고, 내부의 코드수정/재실행 가능
> Docker : image / container 를 나누어서 작업 진행

### Docker System
1. Docker 설치
2. docker image 다운로드
3. 내려받은 image로 docker container 생성/실행
+ 모든 docker 명령은 CLI 형식으로 수행.
``` docker
docker 명령 옵션 선택자(Container/ImageID...)
```
+ image와 container 명령이 각각 별도로 존재

## Docker image Download
+ Docker hub를 사용해 image 다운로드
+ ```docker login``` 명령어를 사용해 docker hub 로그인
    + ```docker login``` 으로 로그아웃 가능
+ ```docker search``` 명령어를 사용해 image 검색
    ``` bash
    docker search [--limit=검색제한]이미지명[:태그]
    ```
    + 태그를 입력하지 않을경우 latest 태그가 기본적으로 붙는다.


## Docker image 주요 명령어
명시적 구분을 위해 image 옵션을 추가
``` bash
docker image 명령 옵션 ...
```
### Image Download
+ 태그가 없을 경우 latest태그 자동 적용
``` bash
docker pull 이미지명
```
### 내려받은 Image List 확인
``` bash
docker images
docker image ls # -q 옵션으로 id만 출력
```

### Image 삭제
``` bash
docker rmi 이미지ID/Repository 이름
docker image rm 이미지ID/Repository 이름
```

## Docker Container 주요 명령
> docker container 에서 자주 쓰이는 옵션을 포함한 command sets 가 존재한다.

### Container 생성
+ image를 container로 만들어야 실행이 가능해진다.
+ image/container는 각각 관리해야한다.
+ container 생성시, docker 프로그램에서 이름이 자동 부여된다.
``` bash 
docker create 이미지명[:태그]
# --name 옵션을 사용해 Container 이름 지정 가능
```
\
### 실행중인 container List 확인
``` bash
docker ps
``` 

### Container 삭제
``` bash
docker rm 컨테이너ID/이름
```

### Container 실행
``` bash
docker start Container이름
```
+ 새로 생성한 ubuntu container를 실행하면, 바로 중지됨
    + docker는 Container를 하나의 응용 프로그램으로 간주한다.
    + Container에서 실행하게 되어있는 프로그램의 실행이 끝나면, 해당 Container는 중지된다.
        + ubuntu container의 command는 /bin/bash이고 이는 STDIN이 가능하지 않으면 종료되는 터미널이다.
        + 별도 터미널과 표준 입력 연결 설정을 해주어야 한다.

### docker run 명령어
: Imgae를 Container로 만들면서 실행하는 명령어
``` bash
docker run 이미지ID/이름
```
**docker run options**<br>

    -i : STDIN(Container 입력)을 open
    -t : tty(가상터미널) 할당
    --name : Container 이름 설정
    -d : Container 백그라운드 실행
    -rm : container 종료시 자동 삭제
    -p : host와 container 포트 연결
    -v : host와 container directory 연결
**-it option의 의미**<br>
+ docker container의 표준 입력을 open
+ pseudo tty를 생성해서 표준입력을 연결<br>
```키보드 입력을 pseudo tty를 통해 container의 표준 입력으로 전달가능하도록 설정```
> pseudo tty<br>
> : teletypewriter의 약자로, Linux에서의 console/terminal을 의미<br/>
> tty를 통해 Linux에 input을 전달할 수 이쓰며, 다양한 터미널에서 접속을 지원하기 위해 2번쨰 tty부터는 pseudo(가상)의 tty를 지정해준다. 

**container 종료시 자동으로 삭제 해주는 옵션**
``` bash
docker run --it --rm --name 이름 image이름
```
**종료시 자동으로 삭제되는 container를 백그라운드로 실행**
``` bash
docker run --it --rm -d --name 이름 image이름
```

### Background에서 실행중인 container에 접속
``` bash
docker attach containerID/이름
```

### 실행중인 Container 중지(종료)
``` bash
# Background에서 실행중이 Container를 중지
docker pause Container이름
# 멈춰있는 상태의 Container를 이어서 실행
docker unpause Container이름
# Background로 실행한 Container를 종료
docker stop Container이름
# Contatiner 재실행
docker restart Container이름
```
 
## docker에서 Apache Web server 실행
``` bash
docker run -p 포트번호:80 --name apache httpd
# -p 옵션을 사용하여 지정한 포트번호에 apache서버를 연결
```
### 보안그룹에 포트 지정
1. EC2 인스턴스 메뉴 접속
2. 보안 메뉴 => 보안 그룹
3. 인바운드 규칙 편집
4. 포트 범위와 허용ip 지정

> 이후 탄력적 IP주소:포트번호로 접속시 it works 메시지 출력됨

### Docker continaer와 사용자 directory 연결
+ Docker는 이미지를 기반으로 만들어진 컨테이너이기 때문에, 컨테이너 종료시 내부에 존재하던 파일도 함께 사라짐
    + 이를 보완하기 위해 ```docker run```의 ```-v``` 옵션을 사용하여 Host  PC의 사용자 디렉토리를 바인딩(공유)하여 사용한다.
+ httpd Image의 apache 기본설정에 의해 포트포워딩옵션에 포트까지만 기재하였을때는 /usr/local/apache/htdocs 폴더의 index를 자동으로 실행한다.
    + 즉 실행되는 폴더를 변경하여서 다른 웹 페이지를 보여줄 수 있다.

### ftp를 사용하여 EC2 Server에 파일 업로드
1. FileZila Client 를 사용하여 파일 EC2 업로드
    - 사이트 관리자를 통해 서버에 연결
        - 프로토콜 : sftp
        - 호스트 : 탄력적 ip 주소
        - 로그온 유형 : 키파일
        - 사용자 : ubuntu
        - 키파일 : AWS 인증 pem 파일
    - index.html이 포함된 폴더 업로드
2. docker run의 -v 옵션을 활용해 directory 연결
``` bash
docker run -v 호스트PC에서의폴더경로/Container절대경로 httpd
```
> 편리한 접속을 위해 80 포트에서의 인바운드 옵션을 지정하면 포트입력없이 ip주소만으로도 접속 가능

### docker 저장매체 확인
``` bash
docker system df
```

### Docker와 Alpine
+ Docker Image는 여러개의 Image가 Layer로 쌓인 형태로 작성
    + 특정 응용프로그램의 실행을 목적으로 하는 Container의 경우, 다양한 기능을 포함하는것은 낭비가 될수있다.
+ 대부분의 Docker 이미지에서는 ubuntu 가아닌 alpine이 base image인 경우가 많다.
    + alpine
        - Embedded Linux를 위한 C/POSIX lib[musl lib] 와 운영 체제 운영이 필요한 기본 유틸리티[BusyBox]만 모아놓은 패키지
        - 대부분의 image에서 ```:alpine```태그로 불러올 수 있다.

### 실행중인 Container의 사용 리소스 확인
``` bash
docker container stats
```

### 실행중인 Container에 명령 실행
``` baseh
docker exec [options] containerID 명령인자
```
+ 실행중인 Container의 Shell 유형을 잘 확인해야한다.

### 실행중인 Container에 연결
+ 백그라운드에서 실행중인 Container에 들어갈때 주로 사용
``` bash
docker attach Container_ID
```

### 모든 Container 삭제 (+이미지 삭제)
> notepad에 기재해 놓고 Copy&Paste로 사용하는것이 일반적
```bash
    docker stop $(docker ps -a -q) # 모든 Container 중지
    docker rm $(docker ps -a -q) # 모든 Container 삭제
    docker rmi -f $(docker images -q) # 모든 Image 삭제
``` 
+ 정지된 Container 모두 삭제
``` bash
docker container prune # 정지된 container 삭제
docker image prune # 실행된 container image외의 모든 image 삭제
docker system prune # 정지된 container, 실행중인 container image 외의 모든 image, volume, network 삭제
```

## Dockerfile
: Docker image 작성을 위한 스크립트로 Dockerfile 문법으로 작성된 DockerFile을 기반으로 이미지를 생성/배포 하는게 활용된다.

## Dockerfile 기본 문법
+ text 파일 형식으로, 사용자가 원하는 다양한 데이터로 작성 가능
+ 기본 문법
    + command/parameter로 이루어져있다.
    + Command는 구분을 위해 통상적으로 대문자로 작성한다.
### Dockerfile 주요 명령
|명령|설명|
|---|---------|
|FROM|Base Image 지정|
|LABEL|Image 설명을 작성하기 위한 명령(버전정보,작성자...)|
|CMD|Container 시작시 실행할 Shell 명령을 지정|
|RUN|Shell 명령 시작|
|ENTRYPOINT|Container 시작시, 실행할 Shell 명령 지정, docker run 실행시에도 덮어씌워지지 않음|
|EXPOSE|Container 외부에 Open할 포트 설정|
|ENV|Container 내부에서 사용할 환경 변수 지정|
|WORKDIR|Container의 작업 디렉토리 설정|
|COPY|파일/디렉토리를 Container에 복사, URL지정 불가, 압축파일 자동 해제 미지원|
+ 참고 명령어

|명령|설명|
|---|--------|

+ Dockerfile에서는 주석 사용가능
``` bash
# Dockerfile 주석 : Line 단위
```

### FROM
+ Base Image 지정 명령
+ Dockerfile에 반드시 작성해야한다.
``` docker
FROM alpine
```
### Dockerfile 로 Image 작성
``` docker
docker bulid [option] Dockerfile_경로
```
+ 주요 옵션

|옵션|설명|
|---|--------|
|-t| --tag| 이미지 이름(Repository) 설정, 이름:태그 형식으로 태그 설정 가능(default:latest)|
|-f| image 빌드시 Dockerfile명으로 된 파일을 찾아 빌드실행
|--pull| image 생성시마다 새로 다운로드 --pull=true 형식으로 작성. base image를 수시로 업데이트할때 주로사용|

### LABEL
+ <key>=<value> 형식으로 dockerfile에 메타 데이터 삽입
+ 보통 저자, 버전, 설명, 작성일자 등을 기재할때 사용
``` docker
LABEL KEY이름 = value
```