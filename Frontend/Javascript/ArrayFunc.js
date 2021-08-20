const data = [1,2,3,4,5]
data2 =data.join('*')
console.log(data2)
data.forEach(item => {
    console.log(item)
})

const data3 = data.map(item=>item*2);
console.log(data3);

