def fitness(chroms, size_n, max_fitness): 

    data = list() 

    for chrom in chroms: 

        conflicts = 0 
        
        for e in chrom: 

            if chrom.count(e) > 1: 

                conflicts += chrom.count(e) - 1 

        for i in chrom: 
            
            for j in chrom: 

                diff = abs(chrom.index(i) - chrom.index(j)) 

                if diff != 0 and diff == abs(i - j): 

                    conflicts += 1 

        conflicts //= 2 

        fitness_value = max_fitness - conflicts 

        data.append([chrom, fitness_value]) 

    return data 

