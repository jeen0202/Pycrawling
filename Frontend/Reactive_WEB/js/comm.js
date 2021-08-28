/* HTTP REST 방식 axios 기반 통신
    axios는 Promise API를 지원
*/

const getNewsGet = ()=> {
    axios("http://localhost:8085/news",{
        method : "get",
        params : {
            email : "test@test.com",            
        }
    }).then(response => {
        console.log(response.data['status'], response.data['info']);
        const newsMsg = document.querySelector('.news');
        newsMsg.innerText = response.data['info']
    }).catch((error) => {
        console.log(error);
    })
}

const getNewsPost = () => {
    axios('http://localhost:8085/news',{
        method : 'post',
        data:{
            email : "test@test.com"
        }
    }).then(response => {
        console.log(response.data['status'], response.data['info']);
        const newsMsg = document.querySelector('.news');
        newsMsg.innerText = "오늘의 뉴스\n"+response.data['info']
    }).catch((error) => {
        console.log(error);
    })
}
getNewsPost();