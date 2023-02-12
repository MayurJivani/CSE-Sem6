const nodemailer = require('nodemailer');
let mailTransporter = nodemailer.createTransport ({
service: 'gmail',
auth: {
user: 'mayurjivani365@gmail.com',
pass: 'Zayn XD'
}
});

let mailDetails = {
from: 'mayurjivani365@gmail.com',
to: 'vedas.devas@gmail.com,ritwik.gce20@sot.pdpu.ac.in',
subject: 'Bonjour :D',
html: '<div style="text-align:center"><div style="background-color:#f2f1f6; padding:30px;"><h1 style="font-family:Roboto;">Forgot your Password</h1><p style="font-family:Oswald; font-size:20px;">Click for button to reset password XD.</p></div><button style="background-color:#36bdc6; color:white; padding:10px;margin-top:10px; border-radius:5px;">Reset Password</button></div>'
};

mailTransporter.sendMail(mailDetails, function(err, data) {

if(err) {
console.log('Error Occurs');
} else {

console.log('Email sent successfully');
}
});