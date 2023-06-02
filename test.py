import config, generate, fitness, sort, crossover, mutation, cut

cs = generate.firstgen(config.genesis, config.size_n)

cs.append([2, 5, 7, 1, 3, 0, 6, 4])
cs.append([1, 0, 2, 3, 7, 5, 6, 4])

data = (fitness.fitness(cs, config.size_n, config.max_fitness))

print(data, "\n\n\n")

table = sort.sortdata(data, config.max_fitness)

print(table)

print(cs)

print(crossover.crossover(cs, config.size_n))

print(mutation.scramble(cs, config.size_n))

print(cut.elitism(table, config.cutshare))