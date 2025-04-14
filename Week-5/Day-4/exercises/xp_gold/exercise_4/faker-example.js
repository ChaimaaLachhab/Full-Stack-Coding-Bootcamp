const { faker } = require('@faker-js/faker');

const users = [];

function addFakeUser() {
  users.push({
    name: faker.person.fullName(),
    street: faker.location.streetAddress(),
    country: faker.location.country(),
  });
}

addFakeUser();
addFakeUser();
console.log(users);
