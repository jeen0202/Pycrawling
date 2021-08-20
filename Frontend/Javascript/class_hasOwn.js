class Animal {
    constructor(name){
        this.name = name
    }
    getMessage(){
        return "Hello"
    }
}

Animal.prototype.age = 1;

const dave = new Animal('sejing')
console.log(dave.hasOwnProperty('name'));
console.log(dave.hasOwnProperty('getMessage'))
console.log(dave.hasOwnProperty('age'))