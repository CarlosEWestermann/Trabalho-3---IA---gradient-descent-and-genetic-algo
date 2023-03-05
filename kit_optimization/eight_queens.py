import random

def evaluate(individual):
    attacks = 0
    
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] == individual[j]:
                attacks += 1
            elif abs(individual[i] - individual[j]) == abs(i - j):
                attacks += 1
                
    return attacks

def tournament(participants):
    fitness_scores = [evaluate(individual) for individual in participants]

    best_index = fitness_scores.index(min(fitness_scores))

    return participants[best_index]

def crossover(parent1, parent2, index):
    
    offspring1 = parent1[:index] + parent2[index:]
    offspring2 = parent2[:index] + parent1[index:]

    return offspring1, offspring2

def mutate(individual, m):
    if random.random() < m:
        individual[random.randint(0, 7)] = random.randint(1, 8)
    return individual


def run_ga(g, n, k, m, e):
    population = [random.choices(range(1, 9), k=8) for i in range(n)]

    fitness = tournament(population)
    return population[fitness]


        
