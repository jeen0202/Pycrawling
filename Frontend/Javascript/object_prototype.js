function User(age,name){
    this.age = age;
    this.name = name;
}

User.prototype.message = function(){
    return "Hello!!"
}

User.prototype.hobby = "coding";

const sejing = new User(28, "Sejing");
console.log(sejing.age, sejing.name, sejing.message(), sejing.hobby);