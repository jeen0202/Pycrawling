const user = {
    age : 10,
    name : "Dave Lee",

    get getAge() {
        return this.age
    },
    set setAge(value){
        this.age = value;
    }
};

console.log(user.getAge);
user.setAge = 20;
console.log(user.getAge);