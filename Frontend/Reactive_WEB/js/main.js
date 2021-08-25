const backToTop = document.getElementById('backtotop')

function checkScroll() {
    // 브라우저에서 Page를 얼마나 Scroll확인했는지 확인할 수 있는 함수
    let pageYOffSet= window.pageYOffset;

    if(pageYOffSet !==0){
        backToTop.classList.add('show');
    }else{
        backToTop.classList.remove('show');
    }
}

function moveBackToTop() {
    if (window.pageYOffset >0){
        window.scrollTo({
            top :0,
            behavior: "smooth"
        })
    }
}

window.addEventListener('scroll',checkScroll);
backToTop.addEventListener('click', moveBackToTop);

