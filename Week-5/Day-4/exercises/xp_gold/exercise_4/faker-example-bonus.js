const prompt = require('prompt-sync')();
const users = [];

function addRealUser() {
  const name = prompt('Name: ');
  const street = prompt('Street: ');
  const country = prompt('Country: ');

  users.push({ name, street, country });
  console.log(users);
}

addRealUser();
