const robots = [
    { id: 1, name: 'Leanne Graham', email: 'Sincere@april.biz', image: 'https://robohash.org/1?set=set1' },
    { id: 2, name: 'Ervin Howell', email: 'Shanna@melissa.tv', image: 'https://robohash.org/2?set=set1' },
    { id: 3, name: 'Clementine Bauch', email: 'Nathan@yesenia.net', image: 'https://robohash.org/3?set=set1' },
    { id: 4, name: 'Patricia Lebsack', email: 'Julianne@kory.org', image: 'https://robohash.org/4?set=set1' },
    { id: 5, name: 'Chelsey Dietrich', email: 'Lucio@annie.ca', image: 'https://robohash.org/5?set=set1' },
    { id: 6, name: 'Dennis Schulist', email: 'Karley@jasper.info', image: 'https://robohash.org/6?set=set1' },
    { id: 7, name: 'Kurtis Weissnat', email: 'Telly@billy.biz', image: 'https://robohash.org/7?set=set1' },
    { id: 8, name: 'Nicholas Runolfsdottir', email: 'Sherwood@rosamond.me', image: 'https://robohash.org/8?set=set1' },
    { id: 9, name: 'Glenna Reichert', email: 'Chaim@dana.io', image: 'https://robohash.org/9?set=set1' },
    { id: 10, name: 'Clementina DuBuque', email: 'Rey@karina.biz', image: 'https://robohash.org/10?set=set1' }
];

const robotContainer = document.getElementById("robotContainer");
const searchBox = document.getElementById("searchBox");
const toggleMode = document.getElementById("toggleMode");

function displayRobots(filteredRobots) {
    robotContainer.innerHTML = "";

    filteredRobots.forEach(robot => {
        const card = document.createElement("div");
        card.classList.add("card");

        card.innerHTML = `
            <img src="${robot.image}" alt="${robot.name}">
            <h2>${robot.name}</h2>
            <p>${robot.email}</p>
        `;

        robotContainer.appendChild(card);
    });
}

displayRobots(robots);

searchBox.addEventListener("input", () => {
    const searchTerm = searchBox.value.toLowerCase();
    const filteredRobots = robots.filter(robot => 
        robot.name.toLowerCase().includes(searchTerm)
    );
    displayRobots(filteredRobots);
});

toggleMode.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
});
