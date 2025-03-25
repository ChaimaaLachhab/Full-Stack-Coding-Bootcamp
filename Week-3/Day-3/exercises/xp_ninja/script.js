// 🌟 Exercise 1: Random Number
let randomNum = Math.floor(Math.random() * 100) + 1;
console.log(`Random number: ${randomNum}`);

for (let i = 0; i <= randomNum; i += 2) {
    console.log(i);
}

// 🌟 Exercise 2: Capitalized Letters
function capitalize(str) {
    let evenCaps = str.split('').map((char, i) => i % 2 === 0 ? char.toUpperCase() : char).join('');
    let oddCaps = str.split('').map((char, i) => i % 2 !== 0 ? char.toUpperCase() : char).join('');
    return [evenCaps, oddCaps];
}

console.log(capitalize("abcdef"));

// 🌟 Exercise 3: Is Palindrome?
function isPalindrome(str) {
    return str === str.split('').reverse().join('');
}

console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));

// 🌟 Exercise 4: Biggest Number
function biggestNumberInArray(arr) {
    let numbers = arr.filter(item => typeof item === 'number');
    return numbers.length ? Math.max(...numbers) : 0;
}

console.log(biggestNumberInArray([-1, 0, 3, 100, 99, 2, 99]));
console.log(biggestNumberInArray(['a', 3, 4, 2]));
console.log(biggestNumberInArray([]));

// 🌟 Exercise 5: Unique Elements
function uniqueElements(arr) {
    return [...new Set(arr)];
}

console.log(uniqueElements([1, 2, 3, 3, 3, 3, 4, 5]));

// 🌟 Exercise 6: Calendar
function createCalendar(year, month) {
    let daysOfWeek = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"];
    let date = new Date(year, month - 1, 1);
    let lastDay = new Date(year, month, 0).getDate();

    let table = `<table><tr>${daysOfWeek.map(day => `<th>${day}</th>`).join('')}</tr><tr>`;
    
    let firstDay = (date.getDay() + 6) % 7;
    
    for (let i = 0; i < firstDay; i++) {
        table += `<td></td>`;
    }

    for (let day = 1; day <= lastDay; day++) {
        table += `<td>${day}</td>`;
        if ((firstDay + day) % 7 === 0) {
            table += `</tr><tr>`;
        }
    }

    table += `</tr></table>`;
    document.getElementById("calendar").innerHTML = table;
}

createCalendar(2024, 3);
