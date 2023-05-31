import config, generate, fitnessp

cs = generate.generate(100)

cs.append([5, 5, 2, 6, 3, 8, 4, 7])

print(fitnessp.fitness(cs))