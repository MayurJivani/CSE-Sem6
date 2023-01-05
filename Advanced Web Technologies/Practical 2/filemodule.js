console.log("File Example")
console.log("Enrollment: 20BCP311D")
console.log("Name: Mayur Jivani")

const fs = require('fs');

//fs.readFile('file.txt','utf-8',(err,data) => {
//    console.log(err,data)
//})

const a = fs.readFileSync('file.txt')
console.log(a.toString())

console.log("Finished reading file")

fs.writeFileSync('file2.txt', "Why you wanna see how far I fall?", () => {
    console.log("Completed Writing")
})