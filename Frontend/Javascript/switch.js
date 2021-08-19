let age = 12;

switch(age) {
    case 12:
        console.log('12세 입니다.')
        break;// break가 없으면 실행 이후 하위 판별문 실행 
    case 13:
        console.log('13세 입니다.')
        break;
    default :
        console.log('올바른 나이가 아닙니다.')
}