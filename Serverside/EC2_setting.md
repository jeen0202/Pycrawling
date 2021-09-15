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
