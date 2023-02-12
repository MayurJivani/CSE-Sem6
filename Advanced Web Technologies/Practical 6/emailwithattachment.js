const nodemailer = require('nodemailer');
let mailTransporter = nodemailer.createTransport ({
service: 'gmail',
auth: {
user: 'mayurjivani365@gmail.com',
pass: 'cayqnznmnxdaemrc'
}
});

let mailOptions = {
from: 'mayurjivani365@gmail.com',
to: 'ritwik.gce20@sot.pdpu.ac.in,mayurjivani365@gmail.com',
subject: 'Bonjour :D',
html: '<h1>Zayn Malik supremacy</h1> <p>Mind of Mine✨</p>',
attachment: [
    {
        filename: 'Sound.mp3',
        path: __dirname + '/Sound.mp3'
    }
]
};

mailTransporter.sendMail(mailOptions, function(err, data) {

if(err) {
console.log('Error Occurs');
} else {

console.log('Email sent successfully');
}
});