// Demande à l'utilisateur d'entrer des mots séparés par des virgules
const userInput = prompt("Entrez plusieurs mots séparés par des virgules :");

// Transforme l'entrée en un tableau en supprimant les espaces inutiles
const words = userInput.split(",").map(word => word.trim());

// Trouve la longueur du mot le plus long
const maxLength = Math.max(...words.map(word => word.length));

// Crée la ligne de bordure
const border = "*".repeat(maxLength + 4);

// Affiche le cadre dans la console
console.log(border);
words.forEach(word => {
    console.log(`* ${word.padEnd(maxLength)} *`);
});
console.log(border);
