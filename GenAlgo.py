import math
import random

# btw chris comment ny jgn di hapus, untuk presentasi nanti, sama emg di minta di soal
PopulationSize = 50
chromosome_length = 32
MaxGen = 100            #Kriteria penghentian evolusi (loop)
CrossoverRate = 0.8     #Probabilitas Pc (80%) 
MutationRate = 0.1      #Probabilitas Pm (10%) 
Min = -10               #batas bawah domain  x1 dan x2
Max = 10                #batas atas domain  x1 dan x2
#yang di kasih soal itu -10 <= x1 <= 10, -10 <= x2 <= 10, jadi Min = -10 dan Max = 10

def fitness_function(x1, x2):
    #rumus yang di kasih soal
    term1 = math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)
    term2 = 0.5 * math.exp(1 - math.sqrt(x2**2))
    return -(term1 + term2)

def population_initialization(size, length):
    population = []
    for _ in range(size): #loop 50 kali
        #generate kromosom baru dengan random 0 dan 1 sebanyak 32 bit (16 untuk x1 dan 16 untuk x2)
        chromosome = [random.randint(0, 1) for _ in range(length)]
        population.append(chromosome)#masukin ke list population
    return population

def decode_chromosome(chromosome):
    #ambil titik tengah untuk memisahkan gen x1 dan x2
    mid = len(chromosome) // 2

    # List slicing operator (:). 
    gen_x1 = chromosome[:mid] #16 bit pertama
    gen_x2 = chromosome[mid:] #16 bit berikutnya

    #function bantuan mengubah gen biner ke desimal
    def binary_to_decimal(gen):
        decimal = 0
        for i, bit in enumerate(reversed(gen)):
            decimal += bit * (2 ** i)
        return decimal
    
    # N = jumlah bit untuk satu variabel (16)
    N = mid
    division = (2**N) - 1
    #Nilai maksimal dari 16 bit = 2^16 - 1 = 65535, 
    #ini untuk normalisasi nanti, biar hasilnya sesuai dengan domain yang di kasih soal (-10 sampai 10)

    dec_x1 = binary_to_decimal(gen_x1)
    dec_x2 = binary_to_decimal(gen_x2)

    #Rumus untuk normalisasi ke rentang [Min, Max]
    x1 = Min + ((Max - Min) / division) * dec_x1
    x2 = Min + ((Max - Min) / division) * dec_x2
    return x1, x2
    
def parent_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    #pilih 3 individu secara acak dari populasi untuk ikut dalam turnamen
    best_index = tournament[0]

    #bandingkan individu-individu dalam turnamen berdasarkan nilai fitness mereka
    for individual in tournament[1:]:
        x1_best, x2_best = decode_chromosome(best_index)
        x1_curr, x2_curr = decode_chromosome(individual)
        if fitness_function(x1_curr, x2_curr) < fitness_function(x1_best, x2_best):
            best_index = individual
    return best_index

def crossover(parent1, parent2, CrossoverRate ):

    #cek apakah crossover terjadi berdasarkan probabilitas yang ditentukan
    if random.random() < CrossoverRate:#80%
        point = random.randint(1, chromosome_length - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1, parent2
    
def mutation(chromosome, MutationRate):
    Mutated_chromosome = []
    for bit in chromosome:
        if random.random() < MutationRate:#10%
            Mutated_chromosome.append(1 - bit)
            #jika bit adalah 0, maka 1 - 0 = 1, jika bit adalah 1, maka 1 - 1 = 0
        else:
            Mutated_chromosome.append(bit)#bit tetap sama
    return Mutated_chromosome

def run():
    population = population_initialization(PopulationSize, chromosome_length)
    for generation in range(MaxGen):#100
        new_population = []
        best_individual = min(population, key=lambda k: fitness_function(*decode_chromosome(k)))
        #key parameter dalam fungsi bawaan Python
        #ubah biner k menjadi angka desimal, lalu hitung fitnessnya

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
            #pastikan kita tidak melebihi ukuran populasi saat menambahkan anak kedua
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
