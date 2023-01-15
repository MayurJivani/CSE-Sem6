//Mayur Jivani - 20BCP311D
var fs = require('fs');

fs.rename('file3.txt','file2.txt', function(err){
    if (err) throw err;
    console.log('Renamed');
});

