// 🌟 Exercise 1: Find the numbers divisible by 23
function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    let numbers = [];
    
    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            numbers.push(i);
            sum += i;
        }
    }

    console.log(numbers.join(" "));
    console.log("Sum:", sum);
}
displayNumbersDivisible();

// 🌟 Exercise 2: Shopping List
const stock = { banana: 6, apple: 0, pear: 12, orange: 32, blueberry: 1 };
const prices = { banana: 4, apple: 2, pear: 1, orange: 1.5, blueberry: 10 };
const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;
    for (let item of shoppingList) {
        if (stock[item] > 0) {
            total += prices[item];
            stock[item]--;
        }
    }
    console.log("Total Bill:", total);
}
myBill();

// 🌟 Exercise 3: What’s in my wallet?
function changeEnough(itemPrice, amountOfChange) {
    const totalChange = amountOfChange[0] * 0.25 + amountOfChange[1] * 0.10 + 
                        amountOfChange[2] * 0.05 + amountOfChange[3] * 0.01;
    return totalChange >= itemPrice;
}
console.log(changeEnough(4.25, [25, 20, 5, 0]));

// 🌟 Exercise 4: Vacation Costs
function hotelCost(nights) {
    return nights * 140;
}

function planeRideCost(destination) {
    const costs = { London: 183, Paris: 220 };
    return costs[destination] || 300;
}

function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) cost *= 0.95;
    return cost;
}

function totalVacationCost() {
    const nights = parseInt(prompt("How many nights in the hotel?"));
    const destination = prompt("Enter your destination:");
    const days = parseInt(prompt("How many days renting a car?"));

    const total = hotelCost(nights) + planeRideCost(destination) + rentalCarCost(days);
    console.log(`The car cost: $${rentalCarCost(days)}, the hotel cost: $${hotelCost(nights)}, the plane tickets cost: $${planeRideCost(destination)}.`);
    console.log("Total vacation cost:", total);
}

totalVacationCost();

// 🌟 Exercise 5: Users
const divContainer = document.getElementById("container");
console.log(divContainer);

document.querySelector(".list li:nth-child(2)").textContent = "Richard";

document.querySelectorAll(".list")[1].children[1].remove();

document.querySelectorAll(".list li:first-child").forEach(li => li.textContent = "Chaimaa");

document.querySelectorAll(".list").forEach(ul => ul.classList.add("student_list"));
document.querySelector(".list").classList.add("university", "attendance");

divContainer.style.backgroundColor = "lightblue";
divContainer.style.padding = "20px";

document.querySelectorAll(".list li").forEach(li => {
    if (li.textContent === "Dan") li.classList.add("hidden");
});

document.querySelector(".list li:nth-child(2)").style.border = "1px solid black";

document.body.style.fontSize = "20px";

if (divContainer.style.backgroundColor === "lightblue") {
    alert("Hello John and Richard");
}

// 🌟 Exercise 6: Change the navbar
const navDiv = document.getElementById("navBar");
navDiv.setAttribute("id", "socialNetworkNavigation");

const newLi = document.createElement("li");
newLi.textContent = "Logout";
document.querySelector("#socialNetworkNavigation ul").appendChild(newLi);

const ul = document.querySelector("#socialNetworkNavigation ul");
console.log(ul.firstElementChild.textContent, ul.lastElementChild.textContent);

// 🌟 Exercise 7: My Book List
const allBooks = [
    {
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        image: "https://m.media-amazon.com/images/I/81af+MCATTL.jpg",
        alreadyRead: true
    },
    {
        title: "1984",
        author: "George Orwell",
        image: "https://m.media-amazon.com/images/I/71kxa1-0mfL.jpg",
        alreadyRead: false
    }
];

const listBooksSection = document.querySelector(".listBooks");

allBooks.forEach(book => {
    const bookDiv = document.createElement("div");
    bookDiv.innerHTML = `
        <p>${book.title} written by ${book.author}</p>
        <img src="${book.image}" alt="${book.title}">
    `;
    if (book.alreadyRead) bookDiv.style.backgroundColor = "lightgray";
    listBooksSection.appendChild(bookDiv);
});
