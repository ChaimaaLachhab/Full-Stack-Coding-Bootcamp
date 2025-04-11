const { people } = require("./data.js");

function calculateAverageAge(personArray) {
    // This function takes an array of people objects and calculates the average age.
    // Calculate the average age of people in the array using a forEach loop
    // and a reduce method. Return the average age. 
  let tot = 0;
  personArray.forEach((element) => {
    tot += element.age;
  });
  const total = personArray.reduce((sum, p) => sum + p.age, 0);
  return tot / personArray.length;
}

console.log("Average age:", calculateAverageAge(people));
