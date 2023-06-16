from config import * 

from generate import * 

from fitness import * 

from sort import *

from crossover import * 

from mutation import * 

from cut import * 

print('BEGIN') 

print() 

tries = 0 

found = False 

perfectanswer = None 

print('First Generation Population:', genesis) 

print() 

samples = firstgen(genesis, size_n) 

print(samples) 

print()

print('Calculating Members\' Fitness:') 

print() 

samplesdata = fitness(samples, size_n, max_fitness) 

print(samplesdata) 

print() 

print('Sorting Members By Survival Chance:') 

print() 

analitycs = sortdata(samplesdata, max_fitness) 

print(analitycs) 

print() 

while not found: 
    
    tries += 1

    print('Crossover Phase Number', tries) 

    print() 

    print('Crossover Phase With The Masks: ') 

    print() 

    newsamples = [] 

    for i in range(0, len(analitycs), 2):

        r = random.random()

        parent1 = list(filter(lambda x: x if r >= x[6][0] and r <= x[6][1] else None,  analitycs))[0][0] 

        r = random.random() 

        parent2 = list(filter(lambda x: x if r >= x[6][0] and r <= x[6][1] else None,  analitycs))[0][0] 

        newsamples += crossover(parent1, parent2, size_n) 

    print('New Members:') 

    print() 

    print(newsamples) 

    print() 

    print('Mutation Phase Number', tries) 

    print() 

    scrambledsamples = scramble(newsamples, size_n) 

    print('Mutant Samples:') 

    print() 

    print(scrambledsamples) 

    print() 

    print('Adding New Members To Pupolation And Calculate Fitnees:') 

    print() 

    samples += scrambledsamples 

    samplesdata = fitness(samples, size_n, max_fitness) 

    print(samplesdata) 

    print() 

    print('Sorting New Members By Survival Chance:') 

    print() 

    analitycs = sortdata(samplesdata, max_fitness) 

    print(analitycs) 

    print() 

    print('Searching For Perfecr Answer:')

    print()  

    for element in analitycs: 

        if element[1] == max_fitness: 

            found = True 

            perfectanswer = element[0] 

            print('Pefect Answer Found!') 

            print() 

            print('After', tries, 'Generation And', len(analitycs), 'Members.') 

            print() 

            print(perfectanswer) 

            print() 

            print('END') 

            print() 

            break 

    else:

        print('Perfect Answer Not Found!') 

        print() 

        print('Elitism Phase Number', tries) 

        print() 

        print('Reducing Members To', int(len(samples) * cutshare), 'By Survival Chance:') 

        print() 

        print('Current Population:', len(analitycs)) 

        print() 

        samples = elitism(analitycs, cutshare) 

        print('Picked Members:') 

        print() 

        print(samples) 

        print() 

        