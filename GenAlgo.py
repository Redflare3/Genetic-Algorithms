import math
import random

PopulationSize = 50
chromosome_length = 32
MaxGen = 32
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