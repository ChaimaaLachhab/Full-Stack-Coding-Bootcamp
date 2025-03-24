// 🌟 Exercise 1 : Checking the BMI

// 1.
const person1 = {
    fullName: "John Doe",
    mass: 80,
    height: 1.8,
    calcBMI: function() {
      return this.mass / (this.height * this.height);
    }
  };
  
  const person2 = {
    fullName: "Jane Smith",
    mass: 70,
    height: 1.6,
    calcBMI: function() {
      return this.mass / (this.height * this.height);
    }
  };
  
  // 2.
  function compareBMI(p1, p2) {
    const bmi1 = p1.calcBMI();
    const bmi2 = p2.calcBMI();
  
    console.log(`${p1.fullName}'s BMI is ${bmi1.toFixed(2)}`);
    console.log(`${p2.fullName}'s BMI is ${bmi2.toFixed(2)}`);
  
    if (bmi1 > bmi2) {
      console.log(`${p1.fullName} has the largest BMI.`);
    } else if (bmi2 > bmi1) {
      console.log(`${p2.fullName} has the largest BMI.`);
    } else {
      console.log("Both have the same BMI!");
    }
  }
  
  // 3. 4.
  compareBMI(person1, person2);
  

  // 🌟 Exercise 2 : Grade Average

  function findAvg(gradesList) {
    let sum = 0;
  
    for (let i = 0; i < gradesList.length; i++) {
      sum += gradesList[i];
    }
  
    const avg = sum / gradesList.length;
    console.log(`Average grade is: ${avg}`);
  
    if (avg > 65) {
      console.log("You passed!");
    } else {
      console.log("You failed! You must repeat the course.");
    }
  }
  
  findAvg([70, 85, 60, 90, 50]);
  

