function insertRow() {
    let table = document.getElementById("sampleTable");

    let newRow = table.insertRow();

    let cell1 = newRow.insertCell(0);
    let cell2 = newRow.insertCell(1);

    let rowIndex = table.rows.length;
    cell1.textContent = `Row${rowIndex} cell1`;
    cell2.textContent = `Row${rowIndex} cell2`;
}

let button = document.getElementById("jsstyle");

// button.addEventListener("click", function() {
//     button.style.backgroundColor = "blue";
//     button.style.color = "white";
//     button.style.fontSize = "20px";
//     button.textContent = "Clicked!";
// });

// button.addEventListener("mouseover", function() {
//     button.style.backgroundColor = "red";
//     button.style.transform = "scale(1.1)";
// });

// button.addEventListener("mouseout", function() {
//     button.style.backgroundColor = "";
//     button.style.transform = "scale(1)";
// });

let div = document.getElementById("container");

div.addEventListener("click", function() {
    alert("Div cliqué !");
    div.style.backgroundColor = "yellow";
});

button.addEventListener("click", function(event) {
    event.stopPropagation();
    button.style.backgroundColor = "blue";
    button.style.color = "white";
    button.style.fontSize = "20px";
    button.textContent = "Clicked!";
});

button.addEventListener("mouseover", function() {
    button.style.backgroundColor = "red";
    button.style.transform = "scale(1.1)";
});

button.addEventListener("mouseout", function() {
    button.style.backgroundColor = "";
    button.style.transform = "scale(1)";
});


document.getElementById("form1").addEventListener("submit", function(event) {
    event.preventDefault();

    let firstName = document.querySelector("[name='fname']").value;
    let lastName = document.querySelector("[name='lname']").value;

    console.log("First name:", firstName);
    console.log("Last name:", lastName);

    alert("First name: " + firstName + "\nLast name: " + lastName);
});
