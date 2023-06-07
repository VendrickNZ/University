def roulette_wheel_select(population, fitness, r):
    total_fitness = 0
    for individual in population:
        total_fitness += fitness(individual)
    rand = r * total_fitness
    running_total = 0
    for individual in population:
        running_total += fitness(individual)
        if running_total >= rand:
            return individual

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))