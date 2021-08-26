//동적 반응
window.addEventListener('dragend', processTouchEnd);
window.addEventListener('mouseup', processTouchEnd);


let touchstartX;
let currentClassList;
let currentImg;
let currentActiveLi;
let nowActiveLi;
let mouseStart;

function processTouchStart(event){
    mouseStart = true;

    event.preventDefault();
    touchstartX = event.clientX;
    currentImg = event.target;

    currentImg.addEventListener('mousemove',processTouchMove);
    currentImg.addEventListener('mouseup', processTouchEnd);

    currentClassList = currentImg.parentElement.parentElement;
    currentActiveLi = currentClassList.getAttribute('data-position');

}

function processTouchMove(event) {

}

function processTouchEnd(event){

}

const classImgList = document.querySelectorAll('ul li img');
for (let i =0; i<classImgList.length ; i++){
    classImgList[i].addEventListener('mousedown', processTouchStart);       
}
