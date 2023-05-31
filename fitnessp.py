def fitness(chroms):

    for chrom in chroms:

        conflicts = 0
        
        for e in chrom:

            if chrom.count(e) > 1:

                conflicts += chrom.count(e) - 1

        conflicts //= 2

        print(conflicts)