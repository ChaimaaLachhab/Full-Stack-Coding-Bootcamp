const products = require('./products.js');

function findProductByName(productName) {
  return products.find(p => p.name.toLowerCase() === productName.toLowerCase());
}

console.log(findProductByName('Laptop'));
console.log(findProductByName('Book'));
