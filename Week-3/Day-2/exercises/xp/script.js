// 🌟 Exercise 1 : List of people
console.log("Exercise 1: List of people");

let people = ["Greg", "Mary", "Devon", "James"];

// Remove "Greg"
people.shift();
console.log(people);

// Replace "James" with "Jason"
people[people.indexOf("James")] = "Jason";
console.log(people);

// Add your name to the end
people.push("Chaimaa");
console.log(people);

// Log Mary's index
console.log("Mary's index is:", people.indexOf("Mary"));

// Make a copy without Mary and your name
let peopleCopy = people.slice(1, 3);
console.log("People Copy:", peopleCopy);

// Index of "Foo"
console.log(people.indexOf("Foo"));

// Variable last: last element of the array
let last = people[people.length - 1];
console.log("Last element:", last);

// Part II - Loops
console.log("Looping through people array:");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

console.log("Loop until Devon:");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") break;
}

console.log("--------");

// 🌟 Exercise 2 : Your favorite colors
console.log("Exercise 2: Your favorite colors");

const colors = ["Blue", "Red", "Green", "Purple", "Yellow"];

for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus: Add suffixes
const suffixes = ["st", "nd", "rd", "th", "th"];
for (let i = 0; i < colors.length; i++) {
  console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}

console.log("--------");

// 🌟 Exercise 3 : Repeat the question
console.log("Exercise 3: Repeat the question");

let userNumber = prompt("Enter a number:");
while (Number(userNumber) < 10) {
  userNumber = prompt("Enter a number bigger than 10:");
}

console.log("--------");

// 🌟 Exercise 4 : Building Management
console.log("Exercise 4: Building Management");

const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

// Log number of floors
console.log("Number of floors:", building.numberOfFloors);

// Apartments on floor 1 and 3
console.log("Apartments on 1st floor:", building.numberOfAptByFloor.firstFloor);
console.log("Apartments on 3rd floor:", building.numberOfAptByFloor.thirdFloor);

// Second tenant and their rooms
const secondTenant = building.nameOfTenants[1];
const roomsDan = building.numberOfRoomsAndRent.dan[0];
console.log("Second tenant:", secondTenant);
console.log("Rooms Dan has:", roomsDan);

// Check rent sum
const rentSarah = building.numberOfRoomsAndRent.sarah[1];
const rentDavid = building.numberOfRoomsAndRent.david[1];
const rentDan = building.numberOfRoomsAndRent.dan[1];

if (rentSarah + rentDavid > rentDan) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
  console.log("Dan's rent increased to 1200");
}

console.log(building.numberOfRoomsAndRent);

console.log("--------");

// 🌟 Exercise 5 : Family
console.log("Exercise 5: Family");

const family = {
  father: "John",
  mother: "Jane",
  son: "Jimmy",
  daughter: "Jenny"
};

// Keys
for (let member in family) {
  console.log("Key:", member);
}

// Values
for (let member in family) {
  console.log("Value:", family[member]);
}

console.log("--------");

// Exercise 6 : Rudolf
console.log("Exercise 6: Rudolf");

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
};

let sentence = "";
for (let key in details) {
  sentence += `${key} ${details[key]} `;
}

console.log(sentence.trim());

console.log("--------");

// Exercise 7 : Secret Group
console.log("Exercise 7: Secret Group");

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let societyName = names.map(name => name[0]).sort().join("");

console.log("Secret society name:", societyName);
