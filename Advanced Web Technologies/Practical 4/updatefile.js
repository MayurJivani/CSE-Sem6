var fs = require('fs');

fs.appendFile('file.txt', ' Mayur Jivani', function(err){
    if(err) throw err;
    console.log('Updated');
});

fs.writeFile('file3.txt', ' 20BCP311D', function(err){
    if(err) throw err;
    console.log('Updated!!')
})