import url from 'url';

const myURL = new URL('https://discord.style');
myURL.pathname = '/results';
myURL.search = '?q=code';

console.log(myURL)
console.log(myURL.href)