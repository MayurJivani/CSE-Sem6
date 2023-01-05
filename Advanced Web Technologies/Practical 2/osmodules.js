console.log("OS Modules");
console.log("Enrollment: 20BCP311D")
console.log("Name: Mayur Jivani")
const os = require("os");

console.log("Architecture: " + os.arch())
console.log("Hostname: " + os.hostname());
console.log("Total Memory in GB: " + os.totalmem()/1024/1024/1034);
console.log("Available Memory in GB: " + os.freemem()/1024/1024/1024);
console.log("Current tmpdir: " + os.tmpdir())
console.log("Platform: " + os.platform())
console.log("OS Type: " + os.type())