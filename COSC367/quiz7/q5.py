def roulette_wheel_select(population, fitness, r):


if __name__ == "__main__":
    population = ['a', 'b']

    def fitness(x):
        return 1 # everyone has the same fitness

    for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))