const user = {
    name : "sejing",
    age : 28,
    getData: ()=> {
        return [user.name, user.age]
    }
};
//console.log(user, typeof user);
//console.log(user.age, user.name);
//user.name = "Sejing";
//console.log(user.name);
console.log(user.getData())

const emptyObject = {};
emptyObject.name = "Empty";
emptyObject.age = "30";
emptyObject.getData = () => {
    return 1+2;
}
// console.log(emptyObject.name)
// console.log(emptyObject.age)
// console.log(emptyObject.getData())

const player ={
    age : 10,
    name : "Player",
    details : {
        hobby : "coding",
        major : "electronics",
        getDetails : (item) => {
            return item *2;
        }
    }
}

//console.log(player.details.getDetails(3));

// 생성자 함수 방법

function User(age,name) {
    this.age = age,
    this.name = name;
    this.getName = function() {
        return this.age;
    }
}

const sejing = new User(20, "Sejing");
console.log(sejing.getName())