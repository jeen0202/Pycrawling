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
        //console.log(response.data['status'], response.data['info']);
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
        //console.log(response.data['status'], response.data['info']);
        const newsMsg = document.querySelector('.news');
        const newsList = document.querySelectorAll('.news-title')
        const newsLinks = document.querySelectorAll('.news-link')
        const newsImgs = document.querySelectorAll('.news-image')
        //const newsList = response.data['newsList'];
        //const newsLinks = response.data['newsLinks'];
        for(let i =0;i<newsList.length; i++){
            newsList[i].innerText=response.data['newsList'][i];
            newsLinks[i].href="https://news.naver.com" +response.data['newsLinks'][i];
            newsImgs[i].src = resopnse.data['newsImgs'][i];
        }
        newsMsg.innerText = "오늘의 뉴스"+response.data['info'];


               
    }).catch((error) => {
        console.log(error);
    })
}
getNewsPost();