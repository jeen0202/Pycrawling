const data = {
    name: 'Sejing',
    age : 28,
    brand : 'fun-coding',
    getMessage : function() {
        return "Hello world!!";
    }
}

//console.log(Object.entries(data))
//console.log(Object.keys(data))
//console.log(Object.values(data))

for (let property in data) {
    //console.log(property)
    console.log(data[property])
}