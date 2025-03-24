// 🌟 Daily challenge: Not Bad

console.log("=== Challenge 1: Not Bad ===");

// 1.
let sentence = "The movie is not that bad, I like it";

// 2.
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

// 3.
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {

    let beforeNot = sentence.slice(0, wordNot);

  let afterBad = sentence.slice(wordBad + 3);

  let result = beforeNot + "good" + afterBad;
  console.log(result);
} else {
  console.log(sentence);
}


// 🌟 Daily challenge: Stars
console.log("=== Challenge 2: Stars ===");

let stars = "";

// i

for (let i = 1; i <= 6; i++) {
  stars += "* ";
  console.log(stars);
}

// ii

for (let i = 1; i <= 6; i++) {
    let row = "";
    
    for (let j = 1; j <= i; j++) {
      row += "* ";
    }
    
    console.log(row);
  }
