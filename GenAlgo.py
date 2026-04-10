import math
import random

PopulationSize = 50
chromosome_length = 32
MaxGen = 100
CrossoverRate = 0.8
MutationRate = 0.1
Min = -10
Max = 10

def fitness_function(x1, x2):
    term1 = math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)
    term2 = 0.5 * math.exp(1 - math.sqrt(x2**2))
    return -(term1 + term2)

def population_initialization(size, length):
    population = []
    for _ in range(size):
        chromosome = [random.randint(0, 1) for _ in range(length)]
        population.append(chromosome)
    return population

def decode_chromosome(chromosome):
    mid = len(chromosome) // 2
    gen_x1 = chromosome[:mid]
    gen_x2 = chromosome[mid:]

    def binary_to_decimal(gen):
        decimal = 0
        for i, bit in enumerate(reversed(gen)):
            decimal += bit * (2 ** i)
        return decimal
    
    N = mid
    division = (2**N) - 1
    dec_x1 = binary_to_decimal(gen_x1)
    dec_x2 = binary_to_decimal(gen_x2)

    x1 = Min + ((Max - Min) / division) * dec_x1
    x2 = Min + ((Max - Min) / division) * dec_x2
    return x1, x2

def parent_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    best_index = tournament[0]

    for individual in tournament[1:]:
        x1_best, x2_best = decode_chromosome(best_index)
        xi_curr, x2_curr = decode_chromosome(individual)
        if fitness_function(xi_curr, x2_curr) < fitness_function(x1_best, x2_best):
            best_index = individual
    return best_index

def crossover(parent1, parent2, CrossoverRate ):
    if random.random() < CrossoverRate:
        point = random.randint(1, chromosome_length - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1, parent2
    
def mutation(chromosome, MutationRate):
    Mutated_chromosome = []
    for bit in chromosome:
        if random.random() < MutationRate:
            Mutated_chromosome.append(1 - bit)
        else:
            Mutated_chromosome.append(bit)
    return Mutated_chromosome

def run():
    population = population_initialization(PopulationSize, chromosome_length)
    for generation in range(MaxGen):
        new_population = []
        best_individual = min(population, key=lambda k: fitness_function(*decode_chromosome(k)))
        new_population.append(best_individual)

        while len(new_population) < PopulationSize:
            p1 = parent_selection(population)
            p2 = parent_selection(population)

            child1, child2 = crossover(p1, p2, CrossoverRate)

            child1 = mutation(child1, MutationRate)
            child2 = mutation(child2, MutationRate)

            new_population.append(child1)
            if len(new_population) < PopulationSize:
                new_population.append(child2)

        population = new_population

    best_chromosome = min(population, key=lambda k: fitness_function(*decode_chromosome(k)))
    x1, x2 = decode_chromosome(best_chromosome)
    min_value = fitness_function(x1, x2)

    return best_chromosome, x1, x2, min_value

if __name__ == "__main__":
    best_chromosome, x1, x2, min_value = run()
    print(f"Best Chromosome: {best_chromosome}")
    print(f"Decoded x1: {x1}")
    print(f"Decoded x2: {x2}")
    print(f"Minimum Value of f(x1, x2): {min_value}")
