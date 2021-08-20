class User1 {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    getMessage() {
        return 'Hello'
    }
}

const sejing = new User1('Sejing',28)
console.log(typeof sejing, sejing.name, sejing.age)
console.log(sejing.getMessage())