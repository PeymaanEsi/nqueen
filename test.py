import config, generate, fitnessp

cs = generate.generate(100)

cs.append([7, 7, 7, 7, 5, 5, 0, 0])

fitnessp.fitness(cs)