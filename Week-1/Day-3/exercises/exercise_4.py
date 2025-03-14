class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        """Adds an animal to the zoo if it's not already in the list."""
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        """Prints all animals in the zoo."""
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        """Removes an animal from the zoo if it exists."""
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        """Sorts and groups animals by first letter."""
        self.animals.sort()
        grouped_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter in grouped_animals:
                grouped_animals[first_letter].append(animal)
            else:
                grouped_animals[first_letter] = [animal]

        return grouped_animals

    def get_groups(self):
        """Prints animals grouped by their first letter."""
        groups = self.sort_animals()
        for letter, group in groups.items():
            print(f"{letter}: {group}")

# Create the zoo
new_york_zoo = Zoo("New York Zoo")

# Add animals
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Cat")

# Print all animals
new_york_zoo.get_animals()

# Sell an animal
new_york_zoo.sell_animal("Lion")

# Print all animals after selling one
new_york_zoo.get_animals()

# Print sorted groups
new_york_zoo.get_groups()
