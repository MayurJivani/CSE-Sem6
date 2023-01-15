var fs = require('fs');

fs.appendFile('file.txt', '20BCP311D', function(err){
    if (err) throw err;
    console.log('Saved..!!');
});

fs.open('file2.txt', 'w', function(err, file){
    if(err) throw err;
    console.log('Saved!!');
});

fs.writeFile('file3.txt', 'Mayur Jivani', function(err){
    if(err) throw err;
    console.log('Saved XD')
});