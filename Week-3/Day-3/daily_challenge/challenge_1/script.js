const planets = [
    { name: "Mercury", moons: 0, color: "gray" },
    { name: "Venus", moons: 0, color: "yellow" },
    { name: "Earth", moons: 1, color: "blue" },
    { name: "Mars", moons: 2, color: "red" },
    { name: "Jupiter", moons: 79, color: "orange" },
    { name: "Saturn", moons: 82, color: "goldenrod" },
    { name: "Uranus", moons: 27, color: "lightblue" },
    { name: "Neptune", moons: 14, color: "blueviolet" }
];

function createSolarSystem() {
    const section = document.querySelector('.listPlanets');
    
    planets.forEach(planet => {
        const planetDiv = document.createElement('div');
        planetDiv.classList.add('planet');
        planetDiv.style.backgroundColor = planet.color;
        
        const planetName = document.createElement('span');
        planetName.textContent = planet.name;
        planetDiv.appendChild(planetName);

        for (let i = 0; i < planet.moons; i++) {
            const moonDiv = document.createElement('div');
            moonDiv.classList.add('moon');
            moonDiv.style.top = `${i * 40}px`;
            planetDiv.appendChild(moonDiv);
        }
        
        section.appendChild(planetDiv);
    });
}

createSolarSystem();
