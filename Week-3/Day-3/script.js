function age (myAge) {
    var mum_age = myAge * 2;
    var dad_age = myAge * 1.2;

    console.log("may age is " + myAge + ", my mum age is " + mum_age + ", my dad age is " + dad_age)
}

age(20);

function age2 (myAge) {
    let mum_age = myAge * 2;
    return mum_age;
}

let mum_age = age2(23)
console.log(mum_age)

const calculator = (a, b, operator) => 
    operator === "+" ? a + b :
    operator === "-" ? a - b :
    operator === "*" ? a * b :
    operator === "/" ? (b !== 0 ? a / b : "Cannot divide by zero") :
    "Invalid operator";

console.log(calculator(10, 5, "+"));
console.log(calculator(10, 5, "-"));
console.log(calculator(10, 5, "*"));
console.log(calculator(10, 5, "/"));
console.log(calculator(10, 0, "/"));
console.log(calculator(10, 5, "%"));


const div1 = document.querySelector("div");
const div2 = document.body.firstElementChild;

console.log(div1, div2);


const li1 = document.querySelectorAll("li")[1];
const li2 = document.querySelector("ul").lastElementChild;

console.log(li1, li2);


const li11 = document.querySelectorAll("li")[1];
const li22 = document.querySelector("ul").lastElementChild;

console.log(li11, li22);


const div11 = document.getElementById("container");
const div22 = document.querySelector("#container");

console.log(div11, div22);


const ulList1 = document.querySelectorAll(".list");
ulList1.forEach(ul => {
    ul.querySelectorAll("li").forEach(li => console.log(li.textContent));
});

const ulList2 = document.getElementsByClassName("list");
for (let ul of ulList2) {
    for (let li of ul.children) {
        console.log(li.textContent);
    }
}



const firstLis1 = document.querySelectorAll(".list");
firstLis1.forEach(ul => console.log(ul.firstElementChild.textContent));

const firstLis2 = document.getElementsByClassName("list");
for (let ul of firstLis2) {
    console.log(ul.children[0].textContent);
}


