console.log("Mayur Jivani - 20BCP311D")
const { Console } = require('console');
const http = require('http');
const port = process.env.PORT || 3000

const server = http.createServer((req, res) => {
    console.log(req);
    req.statusCode = 200;
    res.setHeader('Content-Type','text/html');
    res.end('<h1>Status 200</h1><p>This is a status code</p>')
})

server.listen(port, () =>{
    console.log(`Server is running on port ${port}`);
})