import random 

def scramble(chroms, size_n): 

    for chrom in chroms: 

        low = random.randrange(size_n) 

        up = random.randrange(size_n) 

        if low > up: 

            temp = up 

            up = low 

            low = temp 

        print('Mutation Index Range:', low, ':', up) 

        sample = chrom[low:up] 

        random.shuffle(sample) 

        chrom[low:up] = sample 

    print() 

    return chroms

