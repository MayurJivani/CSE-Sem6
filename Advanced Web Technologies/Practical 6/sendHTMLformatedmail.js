const nodemailer = require('nodemailer');
let mailTransporter = nodemailer.createTransport ({
service: 'gmail',
auth: {
user: 'mayurjivani365@gmail.com',
pass: 'cayqnznmnxdaemrc'
}
});

let mailDetails = {
from: 'mayurjivani365@gmail.com',
to: 'ritwik.gce20@sot.pdpu.ac.in',
subject: 'Bonjour :D',
html: '<h1>Zayn Malik supremacy</h1> <p>Mind of Mine✨</p>'
};

mailTransporter.sendMail(mailDetails, function(err, data) {

if(err) {
console.log('Error Occurs');
} else {

console.log('Email sent successfully');
}
});