function returnNumbers(str) {
    return str.match(/\d/g).join('');
  }
  
  console.log(returnNumbers('k5k3q2g5z6x9bn')); // → 532569
  