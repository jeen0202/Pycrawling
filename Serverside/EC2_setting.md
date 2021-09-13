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
