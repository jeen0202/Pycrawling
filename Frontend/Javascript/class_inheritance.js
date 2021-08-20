class Animal {
    constructor(name) {
        this.name = name
    }
}

class User extends Animal {
    constructor(name,age) {
        super(name)
        this.age = age;
    }
}

const user1 = new User('sejing',28)

console.log(user1.name, user1.age)