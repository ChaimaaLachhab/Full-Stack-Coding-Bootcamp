import random
import time  # For adding a delay

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        self.value = 1 if self.value == 0 else 0

    def __str__(self):
        return str(self.value)

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __str__(self):
        return '\n'.join(str(chromosome) for chromosome in self.chromosomes)

class Organism:
    def __init__(self, dna, mutation_probability):
        self.dna = dna
        self.mutation_probability = mutation_probability

    def mutate(self):
        if random.random() < self.mutation_probability:
            self.dna.mutate()

    def is_all_ones(self):
        return self.dna.is_all_ones()

    def __str__(self):
        return str(self.dna)

# Simulation
def simulate_evolution(organisms, max_generations=1000):
    generations = 0
    while generations < max_generations:
        generations += 1
        print(f"\n--- Generation {generations} ---")
        
        for i, organism in enumerate(organisms):
            organism.mutate()
            print(f"Organism {i + 1} DNA:")
            print(organism)
            
            if organism.is_all_ones():
                print(f"\nOrganism {i + 1} has fully mutated to all 1s!")
                return generations, organism
        
        # Add a delay to slow down the simulation
        time.sleep(1)  # 1-second delay between generations
        
        # Optional: Add a stopping condition to inspect progress
        if generations % 10 == 0:  # Pause every 10 generations
            print(f"\nStopping after {generations} generations to inspect progress...")
            input("Press Enter to continue...")  # Pause for user input
    
    print(f"\nReached maximum generations ({max_generations}) without a fully mutated organism.")
    return generations, None

# Create organisms
organisms = [Organism(DNA(), 0.5) for _ in range(10)]

# Run simulation
generations, successful_organism = simulate_evolution(organisms)

if successful_organism:
    print(f"\nGenerations taken: {generations}")
    print("Successful Organism DNA:")
    print(successful_organism)
else:
    print("No organism reached full mutation within the maximum generations.")