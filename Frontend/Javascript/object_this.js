const user = {
    age : 10,
    name : "Sejing",
    details: {
        hobby : "coding",
        major : "electronics",
        getHobby : function() {
            return this.hobby;
        },
        /* 객체 내부의 화살표 함수의 this는 자신의 객체를 가르키지않고 window에 종속 된다.
        thisHobby : () => hobby,
        */
    }
};

console.log(user.details.getHobby());