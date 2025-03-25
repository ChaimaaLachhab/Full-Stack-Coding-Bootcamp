const userInput = prompt("Entrez plusieurs mots séparés par des virgules :");

const words = userInput.split(",").map(word => word.trim());

const maxLength = Math.max(...words.map(word => word.length));

const border = "*".repeat(maxLength + 4);

console.log(border);
words.forEach(word => {
    console.log(`* ${word.padEnd(maxLength)} *`);
});
console.log(border);
