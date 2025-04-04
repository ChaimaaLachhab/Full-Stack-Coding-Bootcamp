function isAnagram(str1, str2) {
  const cleanStr1 = str1.replace(/\s+/g, "").toLowerCase();
  const cleanStr2 = str2.replace(/\s+/g, "").toLowerCase();

  if (cleanStr1.length !== cleanStr2.length) return false;

  const sortedStr1 = cleanStr1.split("").sort().join("");
  const sortedStr2 = cleanStr2.split("").sort().join("");

  return sortedStr1 === sortedStr2;
}

console.log(isAnagram("Astronomer", "Moon starer")); // t
console.log(isAnagram("School master", "The classroom")); // t
console.log(isAnagram("The Morse Code", "Here come dots")); // t
console.log(isAnagram("Hello", "World")); // f

const isAnagram = (s1, s2) => {
  const normalize = (str) =>
    str.replace(/\s+/g, "").toLowerCase().split("").sort().join("");
  return normalize(s1) === normalize(s2);
};
