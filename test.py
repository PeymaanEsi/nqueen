import config, generate, fitness, sort, crossover

cs = generate.generate(config.samples)

# cs.append([2, 5, 7, 1, 3, 0, 6, 4])
# cs.append([1, 0, 2, 3, 7, 5, 6, 4])

data = (fitness.fitness(cs))

print(sort.sortdata(data))

print(cs)

print(crossover.crossover(cs))