let client = "John";

const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
};


const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
};

displayGroceries();


const cloneGroceries = () => {

    let user = client; 
    client = "Betty";
    console.log("Client:", client);
    console.log("User:", user);


    let shopping = groceries;
    shopping.totalPrice = "35$";
    console.log("Groceries totalPrice:", groceries.totalPrice);

    shopping.other.paid = false;
    console.log("Groceries paid status:", groceries.other.paid);
};


cloneGroceries();