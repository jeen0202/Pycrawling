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
