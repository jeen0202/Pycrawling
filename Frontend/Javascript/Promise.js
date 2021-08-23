const testPromise = new Promise(
    (resolve,reject)=>{ 
        setTimeout(()=>{
            let num = 10;
            if(num>=9){
                resolve(num);
            }else{
                reject("error");
            }
        },100);
    }
);

const testPromise2 = new Promise(
    (resolve,reject)=>{ 
        setTimeout(()=>{
            resolve("500ms")
        },500);
    }
);
testPromise
.then(
    (item)=>{
        console.log('success', item);
        throw new Error("error"); 
        return 2;
    })
.then((num)=>{
    console.log("Sejing", num)
})
.finally(()=>{
    console.log('finally')
})
.catch((er) => {    
    console.log("error");
    })

Promise.all([testPromise, testPromise2]).then((data) => {
    console.log(data);
})

Promise.race([testPromise,testPromise2]).then((data)=>{
    console.log("race",data)
})