# 🌟 Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if self_strength > other_strength:
            return f"{self.name} wins the fight!"
        elif self_strength < other_strength:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"

# ✅ Creating three dogs
dog1 = Dog("Max", 5, 20)
dog2 = Dog("Bella", 4, 18)
dog3 = Dog("Rocky", 6, 25)

# ✅ Testing the methods
print(dog1.bark())
print(f"{dog2.name} runs at {dog2.run_speed()} speed.")
print(dog1.fight(dog3))
