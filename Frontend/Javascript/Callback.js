console.log('안녕하세요');
function desc(callback) {
    setTimeout( () => {
    console.log('Sejing 입니다.')
    callback();
}, 3000);
}
let callback= ()=> {
    console.log('잔잔바리코딩입니다.')
}

desc(callback);