from random import shuffle 

def firstgen(chroms, size_n): 

    samples = [] 

    for i in range(chroms): 

        samples.append(list(range(size_n))) 

        shuffle(samples[i]) 

    return samples 

