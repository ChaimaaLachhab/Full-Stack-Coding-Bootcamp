let addressNumber = 55;
let addressStreet = "Qr Fatah";
let country = "Morocco";

let globalAddress = `I live in ${addressNumber} ${addressStreet}, in ${country}.`;

console.log(globalAddress);

document.getElementById("address-display").textContent = globalAddress;

table = ['cat','dog','fish','rabbit','cow'];

console.log(table[1]);

table.push("horse");

console.log(table);

let deletitem = table.splice(3, 1);

console.log(table.length)


