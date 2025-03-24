// 🌟 Daily challenge GOLD: Bubble Sort

console.log("=== Challenge 3: Bubble Sort ===");

const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];
console.log("Original array:", numbers);

console.log("\n- Array to String -");
console.log("toString():", numbers.toString());
console.log("join():", numbers.join());
console.log("join('+'):", numbers.join("+"));
console.log("join(' '):", numbers.join(" "));
console.log("join(''):", numbers.join(""));

console.log("\n- Bubble Sort Descending Order -");

let sortedNumbers = [...numbers];
let n = sortedNumbers.length;

for (let i = 0; i < n - 1; i++) {
  for (let j = 0; j < n - 1 - i; j++) {
    if (sortedNumbers[j] < sortedNumbers[j + 1]) {
      let temp = sortedNumbers[j];
      sortedNumbers[j] = sortedNumbers[j + 1];
      sortedNumbers[j + 1] = temp;
    }
  }
  console.log(`After pass ${i + 1}:`, sortedNumbers);
}

console.log("Sorted array (descending):", sortedNumbers);