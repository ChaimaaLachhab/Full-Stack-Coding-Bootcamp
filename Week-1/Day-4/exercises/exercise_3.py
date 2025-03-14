# 🌟 Exercise 3: Dogs Domesticated

from exercise_2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

# ✅ Creating a PetDog instance
pet_dog = PetDog("Buddy", 3, 15)

# ✅ Training the dog and performing tricks
pet_dog.train()
pet_dog.do_a_trick()
pet_dog.play("Max", "Bella", "Rocky")
