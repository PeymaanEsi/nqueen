from config import size_n

def fitness(chroms):

    data = list()

    for chrom in chroms:

        conflicts = 0
        
        for e in chrom:

            if chrom.count(e) > 1:

                conflicts += chrom.count(e) - 1
            

        for i in chrom:
            
            for j in chrom:

                diff = abs(chrom.index(i) - chrom.index(j))

                if diff == 0:

                    pass 

                elif diff == abs(i - j):

                    conflicts += 1

        conflicts //= 2

        data.append((chrom, conflicts))

    return data