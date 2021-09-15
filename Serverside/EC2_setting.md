# AWS 계정 가입

# EC2 인스턴스 생성(서버생성)
## 1. EC2 인스턴스 생성을 위한 리전 설정
+ 서울로 설정
  + 타지역으로 설정시 변경이 어려움
## 2. EC2 인스턴스 생성
## 3. 접속키 생성 및 저장
+ 분실시 인스턴스 삭제 필요
## 4. 인스턴스 시작
## 5. 탄력적 IP 생성 및 인스턴스와 연결
+ IP 미할당시 과금실행

# Windows에서 접속
    https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/putty.html 참고
## 1. putty & puttyGen 설치
## 2. puttyGen에서 생성된 접속키 변환
## 3. putty 설정
+ Session - Host Name 
  + 사용자명@[할당된 IP 주소]
  + port 번호 22
+ SSH - Auth
  + Private Key file for autentication
    + 변환했던 접속키 browse
+ 설정 저장 및 실행

# Docker 사용을 위한 Linux 쉘 사용법
## Linux와 File
+ 모든 것을 파일로 취급
  + 모든 인터렉션은 파일을 일고, 쓰는 방식처럼
  + 모든 디바이스 관련 기술도 파일처럼 다룬다.

## Shell
+ Shell(쉘) : 사용자와 하드웨어/OS 간 인터페이스 
  + 사용자의 입력을 해석하여, 커널에 요청
  + System Call을 사용해 프로그래밍되어있음
  + 리눅스 명령어 = 쉘 명령어
    + 리눅스 기본 쉘 = bash
### Linux Shell 종류
+ Bourne-Again Shell (bash) : GNU 프로젝트의 하나로 개발된 사실상 기본 쉘
+ Bourne Shell(sh)
+ C Shell (csh)
+ Korn Shell (Ksh) : 유닉스에서 주로 사용

## Linux Shell 명령어
### whoami : 로그인된 User ID를 출력
``` bash
whoami
```
  >Linux의 super관리자 : root
### sudo option : root 권한으로 실행
+ root계정으로 로그인하지 않고도 super 권한으로 명령 실행
### pwd : 현재 위치 출력
``` bash
pwd
``` 
### ls : 폴더내 파일 목록 출력
``` bash
ls 
ls -al # 숨긴 파일및 소유자,history 표현 
```

## 리눅스와 권한
+ OS는 사용자/리소스 권한 관리
+ 리녹스는 사용자/그룹으로 권한 관리
+ 파일마다 소유자/소유 그룹/모든 사용자 에 대해 읽기/쓰기/실행 권한 관리

### 파일 권한
+ 사용자
  + 소유자 : 소유자의 권한
  + 그룹 : 소유자가 속해있는 그룹의 권한
  + 공개 : 모든 사용자에 대한 권한
+ 권한 종류
  + 읽기(r)
  + 쓰기(w)
  + 실행(x)

### chmod : 파일 권한 변경
+ 숫자 사용시
  + 세자리 숫자(소유자,그룹,기타)를 사용하여 2진법의 원칙사용
  + 읽기 : 4, 쓰기 : 2, 실행 : 1
  + 전체 권한및 자리수의 합으로 권한 부여
``` bash
#모든 사용자에게 권한부여
chmod 777 myfile.md
# r-xr-xr-x
chmod 555 
```
### cat : 파일 내용 확인
``` bash
cat myfile.cnf
# myfile.cnf의 내용 출력
```
### rm : 파일 및 폴더 삭제
+ 주 사용 형식 : rm -f 폴더명
+ 사용 사용하는 옵션
  + r : 하위디렉토리를 포함하는 모든 파일 삭제
  + f : 강제 삭제
``` bash
rm myfile.cnf
```
> Linux에는 휴지통이 없다.

## Linux의 Redirect와 Pipe
### Standard Stream (표준 입출력)
+ command 로 실행되는 process의 3가지 stream 유형
  + 표준 입력 - stdin(standard input stream)
  + 표준 출력 - stdout(standard output stream)
  + 오류 출력 - stderr(standard error stream)
+ 모든 스트림은 plain text로 console에 출력

## Redirection (리다이렉션)
+ 표준 스트림 흐름을 바꿀 수 있다.
  + ```>,<``` 기호를 사용하여 표준출력을 파일에 저장할 때 주로 사용한다.
  ``` bash
  ls > file.txt
  # ls로 출력되는 표준출력 스트림을 file.txt로 이동(저장)
  head < file.txt
  # 파일 첫부분부터 10라인 까지 출력해주는 명령 head를 file.txt에 적용
  ```
## Pipe(파이프)
+ ```|```기호를 사용하여 두 프로세스간 출력 스트림을 다른 프로세스의 입력 스트림으로 사용 할때 사용
``` bash
ls -al | grep bash
# 폴더내의 모든 파일을 출력하고 이 결과에서 bash가 들어간 파일 검색
```

### grep : 검색 명령어
  + option
    + -l : 대소문자 미구분
    + -v : pattern을 포함하지 않는 라인 출력
    + -n : 검색 결과의 각 행 선두에 행 번호 입력
    + -l : 파일명만 출력
    + -c : 일치하는 라인의 개수 출력
    + -r : 하위 디렉토리까지 검색

## Linux Process Management
### Process vs Binary
  + 코드 이미지 또는 Binary : 실행파일
  + 실행중인 프로그램 : 프로세스
    + 가상/물리 메모리 정보
    + 리소스 관련 정보 
### 리눅스의 실행 환경
+ Linux는 기본적으로 다양한 프로세스 실행
+ 유닉스 철학 : 여러 프로그램이 서로 유기적으로 각자의 수행하여 전체 시스템이 동작하도록 하는 원리

### Foreground & Background
+ foreground process : Shell 에서 해당 프로세스 실행을 명령할 경우 사용자가 다른 입력을 하지 못하는 프로세스
+ background process : 사용자 입력과 상관없이 실행되는 프로세스
  + process 실행 명령 종단에 &를 추가하여 실행
```bash
#사용 예시
find / -name "*.py" > list.txt &
```
> foreground process 제어
> ```[CTRL]+C``` : 프로레스 작업 취소 및 종료

### process 상태확인 -ps 명령어
+ 사용법 ps [option(s)]
  -a : 시스템을 사용하는 모든 사용자의 프로세스 출력<br/>
  -u : 프로세스 소유자에 대한 상세 정보 출력 <br>
  -l : 프로세스 관련 상제 정보 출력 <br>
  -x : 터미널에 로그인한 후 실행한 프로세스가 아닌 데몬 프로세스도 포함하여 출력 <br>
  -e : 해당 프로세스와 관련된 환경 변수까지 출력<br>
  -f : 프로세스간 관계 정보 출력
  > daemon process(데몬 프로세스 ) : 사용자 모르게 시스템 관리를 위해 실행되는 프로세스

### 프로세스 중지
+ kill 명령어
  + 사용법
    1. kill % 작업번호
    2. kill 프로세스ID
    3. 작업 강제 종료 옵션 -9

## Linux Shell 사용법 (Hard-link/Soft-link)
+ cp 명령어 : 파일 복사
  + cp 원본 복제본 : 원본과 복제본은 각각 물리적으로 다른 파일로 저장
  + 하위폴더 포함 복사
+ Hard link : ln A B
  + A와B는 동일한 파일을 가르킨다.
  + 동일한 파일을 지칭하는 이름을 추가로 만드는 방식
  + 전체 파일 용량은 달라지지 않는다.
+ Soft(Symbolic) link : ln-s A B
  + Windows의 바로가기와 동일
  + ls -al하면 Soft link 확인 가능
  + rm으로 원본을 삭제하면 해당 파일 접근 불가

## Ubuntu 패키지 관리
### Ubuntu 배포판
+ Debian 배포판을 기반으로 Canonical 사가 ubuntu 배포판 개발
  + Debian 배포판은 apt 프로그래믕ㄹ 이요해 SW 설치/업데이트를 간편하게 한 패키지
+ ubuntu의 뜻 : 남아프리카 언어로 '네가 있으니 나도 있다'
  + ubuntu desktop 개포판 (X윈도우 기ㅏㅂㄴ, GUI 기본 제공))과 ubuntu server 배포판 을 제공
  + 지원기간이 5년인 LTS 버전이 그보다 짧은 일반 버전으로 나누어서 배포
### Ubuntu package Manager
+ CentOS나 Fedora와 같은 ReadHat 계열 : RPM을 패키징 시스템으로 사용
+ ubuntu와 같은 Debian 계열 : deb를 패키징 시스템으로 사용
+ 패키지와 그 정보를 가지고 있는 패키지 저장소라는 개념을 보유
## Ubuntu Package 관리 실무
+ ubuntu package index 정보 업데이트(배포판 버전에 따른 패키지 업데이트 버전 정보 등)
``` bash
sudo apt-get update
```
+ 설치된 ubuntu package 업그레이드(```주의 요망```)
``` bash
sudo apt-get upgrade
```
+ 패키지 설치
``` bash
sudo apt-get install 패키지명
```
+ 패키지 삭제(설정파일 제외)
``` bash
sudo apt-get remove 패키지명
```
+ 패키지 삭제(설정파일 포함)
``` bash
sudo apt-get --purge remove 패키지명
```


