const fs = require('fs')

fs.writeFile('file2.txt', " Why you wanna see how far I fall?", ()=>{
    console.log("Written to the file")
})

fs.readFile('file.txt', 'utf-8', (err, data)=>(
    console.log(data)
))

const z = fs.readFileSync('file.txt')
console.log(z.toString())