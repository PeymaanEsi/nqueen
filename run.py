from config import * 

from generate import * 

from fitness import * 

from sort import *

from crossover import * 

from mutation import * 

from cut import * 

tries = 0 

found = False 

perfectanswer = None 

print('First Generation Population:', genesis) 

print() 

samples = firstgen(genesis, size_n) 

print('Generation Number', tries) 

print(samples) 

print()

print('Calculating Members\' Fitness:') 

samplesdata = fitness(samples, size_n, max_fitness) 

print('Fitness:') 

print(samplesdata) 

print() 

print('Sorting Members By Survival Chance:') 

analitycs = sortdata(samplesdata, max_fitness) 

print('Population:') 

print(analitycs) 

print() 

while not found: 
    
    tries += 1

    print('Crossover Phase With The Mask: ', end='') 

    newsamples = crossover(samples, size_n)

    print('New Members:') 

    print(newsamples) 

    print() 

    print('Mutation Phase:') 

    scrambledsamples = scramble(newsamples, size_n) 

    print('Mutant Samples:') 

    print(scrambledsamples) 

    print('Adding New Members To Pupolation And Calculate Fitnees And Survival Chance...') 

    samples += scrambledsamples 

    samplesdata = fitness(samples, size_n, max_fitness) 

    print('Fitness:') 

    print(samplesdata) 

    print() 

    print('Sorting New Members By Survival Chance:') 

    analitycs = sortdata(samplesdata, max_fitness) 

    print('Population:') 

    print(analitycs) 

    print() 

    print('Searching For Perfecr Answer...') 

    for element in analitycs: 

        if element[1] == max_fitness: 

            found = True 

            perfectanswer = element[0] 

            print('Pefect Answer Found!') 

            print() 

            print('After', tries, 'Generation.') 

            print() 

            print(perfectanswer) 

            print() 

            break 

        else:

            print('Perfect Answer Not Found!') 

            print() 

            print('Elitism Phase:') 

            print() 

            print('Reducing Members To', int(len(samples) * cutshare), 'By Survival Chance...') 

            print() 

            samples = elitism(analitycs, cutshare) 

            print('Picked Members:') 

            print(samples)