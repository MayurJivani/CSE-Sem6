const nodemailer = require('nodemailer');
let mailTransporter = nodemailer.createTransport ({
service: 'gmail',
auth: {
user: 'mayurjivani365@gmail.com',
pass: 'qxplqqsezbsfwicw'
}
});

let mailDetails = {
from: 'mayurjivani365@gmail.com',
to: 'ritwik.gce20@sot.pdpu.ac.in',
subject: 'Bonjour :D',
text: 'Chupapi Muniyanniyo'
};

mailTransporter.sendMail(mailDetails, function(err, data) {

if(err) {
console.log('Error Occurs');
} else {

console.log('Email sent successfully');
}
});