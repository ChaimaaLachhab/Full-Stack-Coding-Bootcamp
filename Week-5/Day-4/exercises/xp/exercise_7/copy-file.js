const fs = require('fs');

fs.copyFileSync('source.txt', 'destination.txt');
console.log('File copied!');
