const prompt = require('prompt-sync')();

function validateName(fullName) {
  const regex = /^[A-Z][a-z]+ [A-Z][a-z]+$/;
  return regex.test(fullName);
}

const input = prompt('Enter full name (e.g., John Doe): ');
console.log('Is valid name?', validateName(input));
