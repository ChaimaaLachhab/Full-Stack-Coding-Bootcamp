// 🌟 Exercise 1 : Scope

// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}
// Prediction: a will be 3 inside funcOne()
// If we use const instead of let, an error will occur because const variables cannot be reassigned.

funcOne();

// #2
let a = 0;
function funcTwo() {
    a = 5;
}
function funcThree() {
    alert(`inside the funcThree function ${a}`);
}
// Prediction:
// - First call to funcThree(): a is 0 (global scope)
// - funcTwo() changes a to 5
// - Second call to funcThree(): a is 5
// If a was declared with const, an error would occur since const cannot be reassigned.

funcThree();
funcTwo();
funcThree();

// #3
function funcFour() {
    window.a = "hello";
}
function funcFive() {
    alert(`inside the funcFive function ${a}`);
}
// Prediction: a will be set globally as "hello" and accessed inside funcFive()
funcFour();
funcFive();

// #4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}
// Prediction: a inside funcSix is local, so "test" will be displayed.
funcSix();
// If we use const instead of let, the result will be the same unless we try to reassign it.

// #5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);
// Prediction:
// - Inside the if block: 5 (block-scoped variable)
// - Outside: 2 (global scope)
// If we use const instead of let, the result is the same unless reassignment occurs.


// 🌟 Exercise 2 : Ternary operator
const winBattle = () => true;
const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);

// 🌟 Exercise 3 : Is it a string ?
const isString = value => typeof value === 'string';
console.log(isString('hello')); // true
console.log(isString([1, 2, 4, 0])); // false

// 🌟 Exercise 4 : Find the sum
const sum = (a, b) => a + b;
console.log(sum(3, 7));

// 🌟 Exercise 5 : Kg and grams
// Function declaration
function kgToGrams(kg) {
    return kg * 1000;
}
console.log(kgToGrams(5));

// Function expression
const kgToGramsExp = function(kg) {
    return kg * 1000;
};
console.log(kgToGramsExp(5));

// Function declaration is hoisted, function expression is not.

// One-line arrow function
const kgToGramsArrow = kg => kg * 1000;
console.log(kgToGramsArrow(5));

// 🌟 Exercise 6 : Fortune teller
((children, partner, location, job) => {
    document.body.innerHTML = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
})(2, 'Alice', 'Paris', 'developer');

// 🌟 Exercise 7 : Welcome
((username) => {
    const navbar = document.querySelector(".navbar");
    const userDiv = document.createElement("div");
    userDiv.innerHTML = `<img src='profile.jpg' alt='Profile'/> Welcome, ${username}`;
    navbar.appendChild(userDiv);
})("John");

// 🌟 Exercise 8 : Juice Bar
function makeJuice(size) {
    let ingredients = [];
    
    function addIngredients(ing1, ing2, ing3) {
        ingredients.push(ing1, ing2, ing3);
    }
    
    function displayJuice() {
        document.body.innerHTML += `The client wants a ${size} juice, containing ${ingredients.join(", ")}.`;
    }
    
    addIngredients("banana", "apple", "orange");
    addIngredients("mango", "strawberry", "pineapple");
    displayJuice();
}

makeJuice("large");
