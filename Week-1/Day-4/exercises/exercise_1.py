# 🌟 Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# ✅ Creating a new Siamese class inheriting from Cat
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# ✅ Creating instances of different cats
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Leo", 4)
siamese_cat = Siamese("Nala", 2)

# ✅ Creating a list of cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# ✅ Creating Sara's pet instance
sara_pets = Pets(all_cats)

# ✅ Taking the cats for a walk
sara_pets.walk()
