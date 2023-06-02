from config import * 

from generate import * 

from fitness import * 

from sort import *

from crossover import * 

tries = 0 

found = False 

perfectanswer = None 

while not found: 
    
    tries += 1

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

    print('Fitness:') 

    print(analitycs) 

    print() 

    print('Crossover Phase With The Mask: ', end='') 

    samples += crossover(samples, size_n)

    print('New Members:') 

    print(samples) 

    print() 

    print('Adding New Members To Pupolation And Calculate Fitnees And Survival Chance...') 

    samplesdata = fitness(samples, size_n, max_fitness) 

    print('Fitness:') 

    print(samplesdata) 

    print() 

    print('Sorting New Members By Survival Chance:') 

    analitycs = sortdata(samplesdata, max_fitness) 

    print('Fitness:') 

    print(analitycs) 

    print() 

    break