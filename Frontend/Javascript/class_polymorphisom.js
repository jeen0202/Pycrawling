class Animal {
    constructor(name) {
        this.name = name
    }

    getMessage(){
        return 'Hello';
    }
}

class User extends Animal{
    constructor(name,age){
        super(name)
        this.age = age;
    }
    getMessage(){
        return "Hello Stranger";
    }
}

const user1 = new User("sejing")
console.log(user1.getMessage())
